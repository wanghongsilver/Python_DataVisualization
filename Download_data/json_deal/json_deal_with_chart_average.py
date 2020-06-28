import json
import pygal
import math
from itertools import groupby

def draw_line_average(x_data, y_data, title, y_legend):
    xy_map = []
    for x, y in groupby(sorted(zip(x_data, y_data)), key=lambda _:_[0]):
        y_list = [v for _, v in y]
        xy_map.append([x, sum(y_list) / len(y_list)])
    x_unique, y_mean = [*zip(*xy_map)]
    line_chart = pygal.Line()
    line_chart.title = title
    line_chart.x_labels = x_unique
    line_chart.add(y_legend, y_mean)
    line_chart.render_to_file('./outputsvg/'+title+'.svg')
    return line_chart

#将数据加载到一个列表上
#采用相对路径
filename = './download_data/btc_json_2017.json'
with open(filename, 'r') as f_json:
    btc_data = json.load(f_json)

#创建5个列表，存储信息
dates = []
months = []
weeks = []
weekdays = []
closes = []

#存储每一天的信息
for btc_dir in btc_data:
    dates.append(btc_dir['date'])
    months.append(int(btc_dir['month']))
    weeks.append(int(btc_dir['week']))
    weekdays.append(btc_dir['weekday'])
    closes.append(float(btc_dir['close']))

idx_month = dates.index('2017-12-01')
line_chart_month = draw_line_average(months[:idx_month], closes[:idx_month], '收盘价月日均值（￥）', '月日均值（￥）')
line_chart_month

idx_week = dates.index('2017-12-11')
wd = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
weeekdays_int = [wd.index(w) + 1 for w in weekdays[1:idx_week]]
line_chart_week = draw_line_average(weeekdays_int, closes[1:idx_week], '收盘价星期均值（￥）', '星期均值')
line_chart_week.x_labels = ['周一', '周二', '周三', '周四', '周五', '周六', '周天']
line_chart_week.render_to_file('./outputsvg/收盘价星期均值（￥）.svg')

