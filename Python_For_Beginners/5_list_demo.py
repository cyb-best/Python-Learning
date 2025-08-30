# list 数据结构 append添加元素 remove移除元素
# list支持添加不同数据类型的元素
shopping_list = ["键盘", "鼠标"]
print(shopping_list)
shopping_list.append("显示器")
print(shopping_list)
shopping_list.remove("鼠标")
print(shopping_list)
print(len(shopping_list))
shopping_list.append(12)
print(shopping_list)
print(type(shopping_list))
list_length = len(shopping_list)
print(type(shopping_list[list_length - 1]))
print(type(shopping_list[0]))