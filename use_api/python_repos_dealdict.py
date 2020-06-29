import requests

# 执行API 调用 并存储响应
url = "https://api.github.com/search/repositories?q=language:python&sort=starts"
r = requests.get(url)
print("Status code:", r.status_code)

#将 API响应存储在一个变量中
requests_dict = r.json()
print("Total respositories:", requests_dict['total_count'])

# 探索有关仓库信息
repo_dicts = requests_dict['items']
print("Repositories returned:", len(repo_dicts))

#研究第一个仓库
repo_dict = repo_dicts[0]
print("\n Keys:", len(repo_dict))
for key in sorted(repo_dict.keys()):
    print(key)
print("\n Selected information about first repostory:")
print("Name:",repo_dict['name'])
print("Owner:", repo_dict['owner']['login'])