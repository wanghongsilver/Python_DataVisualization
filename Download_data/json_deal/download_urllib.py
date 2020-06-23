from urllib.request import urlopen
import json
import requests

#url下载文件报错，暂时不能执行

#url下载json文件
json_url = 'https://github.com/wanghongsilver/Python_DataVisualization/raw/master/Download_data/csv_del/input_data/death_valley_2014.csv'
response = urlopen(json_url)

#读取数据
req = response.read()

#将数据写入文件
filename = './download_data/btc_close_2017_urllib.json'
with open(filename, 'wb') as f:
    f.write(req)
#加载jsona格式
file_urllib = json.loads(req)
print(file_urllib)


# #requests下载json文件
# json_url = 'https://github.com/wanghongsilver/Python_DataVisualization/raw/master/Download_data/csv_del/input_data/death_valley_2014.csv'
#
# #读取数据
# req = requests.get(json_url)
#
# #将数据写入文件
# filename = './download_data/btc_close_2017_urllib.json'
# with open(filename, 'wb') as f:
#     f.write(req.txt)
# #加载jsona格式
# file_requestes= req.json()
# print(file_requestes)