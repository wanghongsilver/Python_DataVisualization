import matplotlib.pyplot as plt

x_value = list(range(1,1001))
y_value = [x**2 for x in x_value]

plt.scatter(x_value, y_value, c=y_value, cmap=plt.cm.Blues, edgecolors='none', s=40)

#设置图标标题，并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

#设置刻度标记大小
plt.tick_params(axis='both', which='major', labelsize=14)

#设置每个坐标轴的取值范围git
plt.axis([0, 1100, 0, 1100000])

#自动保存图标
plt.savefig('squares_plot.png', bbox_inches='tight')
plt.show()