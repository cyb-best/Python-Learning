# 列表 [] 用,隔开多个元素
colors = ['red', 'green', 'blue', 'yellow', 'purple', 'white']
print(colors)
print(colors[0])
print(colors[0].title())
# 返回列表中最后一个元素、倒数第二个元素
print(colors[-1])
print(colors[-2])

message = "My favorite color is " + colors[-1] + "."
print(message)
# 改
colors[0] = 'black'
print(colors[0])
# 增
colors.append('pink')
print(colors)
colors.insert(0, 'orange')
print(colors)
# 删
del colors[0]
print(colors)
del colors[-1]
print(colors)
colors.pop()
print(colors)
colors.pop(0)
print(colors)
colors.remove('blue')
# colors.remove('face')
print(colors)

# 列表排序
colors = ['red', 'green', 'blue', 'yellow', 'purple', 'white']
colors.sort()
print(colors)
# 反向排序
colors.sort(reverse=True)
print(colors)
# 临时排序
print(sorted(colors))
print(colors)

# 列表反转
colors.reverse()
print(colors)
print(len(colors))