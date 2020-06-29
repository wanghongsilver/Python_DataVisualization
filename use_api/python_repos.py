import requests

# 执行API 调用 并存储响应
url = "https://api.github.com/search/repositories?q=language:python&sort=starts"
r = requests.get(url)
print("Status code:", r.status_code)

#将 API响应存储在一个变量中
requests_dict = r.json()

#处理结果
print(requests_dict.keys())