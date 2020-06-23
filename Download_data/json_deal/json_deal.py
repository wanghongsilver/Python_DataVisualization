import json

#将数据加载到一个列表上
#采用相对路径
filename = './download_data/btc_json_2017.json'
with open(filename, 'r') as f_json:
    btc_data = json.load(f_json)
#打印每一天的信息
for btc_dir in btc_data:
    date = btc_dir['date']
    month = btc_dir['month']
    week = btc_dir['week']
    weekday = btc_dir['weekday']
    close = btc_dir['close']
    print("{} is month {} week {}, {}, the close price is {} RMB".format(date, month, week, weekday, close))