import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

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
names, starts = [], []
print("\n Selected information about each repostory:")
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    starts.append(repo_dict['stargazers_count'])

#可视化
my_style = LS('#333366', base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Python Project on Github'
chart.x_labels = names
chart.add('', starts)
chart.render_to_file('./outputsvg/python_repos.svg')