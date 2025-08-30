# 元组
# 列表中的元素是可以修改的，而元组中的元素是不可以修改的，即不可变的列表称为元组
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
# dimensions[1] = 100
# print(dimensions[1])
for dimension in dimensions:
    print(dimension)
print(dimensions)
# 不能修改元组中的元素，但可以给存储元组的变量赋值
dimensions = (77, 777)
print(dimensions)