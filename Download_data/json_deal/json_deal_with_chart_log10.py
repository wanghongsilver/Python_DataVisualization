import json
import pygal
import math

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

#绘制收盘价折线图
line_chart = pygal.Line(x_label_rotation=20, show_minor_x_lables=False)
line_chart.title = '收盘价对数变换(￥)'
line_chart.x_labels = dates
N = 20
line_chart.x_labels_major = dates[::N]
close_logs = [math.log10(_) for _ in closes]
line_chart.add('收盘价', close_logs)
line_chart.render_to_file('./outputsvg/收盘价对数折线图￥.svg')