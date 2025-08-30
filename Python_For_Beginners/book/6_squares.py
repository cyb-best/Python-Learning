# 乘方运算
squares = []
for number in range(1, 11):
    # square = number ** 2
    # squares.append(square)
    squares.append(number ** 2)
print(squares)

# 列表解析 简化代码，语法格式如下
squares1 = [value ** 2 for value in range(1, 11)]
print(squares1)
