name = "ada lovelace"
# 将每个单词的首字母进行大写
print(name.title())
# 将所有字母大写
print(name.upper())
# 将所有字母小写
print(name.lower())

# 字符串拼接
first_name = "chen"
last_name = "angang"
full_name = first_name + " " + last_name
print(full_name)

# 制表符添加空白 \t  \n
print("\tchen angang\n is handsome!")

# 删除字符串多余的空白
my_string = " cyb"
my_string1 = "cyb  "
my_string2 = '  cyb    '
my_string = my_string.lstrip() # 去除左边多余的空白
print(my_string)
my_string1 = my_string1.rstrip() # 去除右边多余的空白
print(my_string1)
my_string2 = my_string2.strip() # 去除两边多余的空白
print(my_string2)