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

#研究仓库
print("\n Selected information about each repostory:")
for repo_dict in repo_dicts:
    print("\n name:", repo_dict['name'])
    print("owner:", repo_dict['owner']['login'])
    print("start:", repo_dict['stargazers_count'])
    print('repository:', repo_dict['html_url'])
    print('Description:', repo_dict['description'])