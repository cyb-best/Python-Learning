# car = input("你想要买什么样的车：")
# print("我可以帮你找到你要的车【" + car +"】。")

# eat_count = int(input("您好，请问几个人就餐："))
# if eat_count <= 8:
#     print("有空桌，里面请")
# else:
#     print("抱歉，没有空桌")

number = int(input("请输入一个数字，我将告诉你是否为10的整数倍："))
if number % 10 == 0:
    print(f"数字{number}是10的整数倍")
else:
    print(f"数字{number}不是10的整数倍")