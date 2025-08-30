# input函数返回的是字符串
# a = input("please input your age: ")
# print(a)

# BMI = 体重 / （身高 ** 2）
user_weight = input("请输入您的体重(kg)：")
user_height = input("请输入您的身高(m): ")
user_bmi = float(user_weight) / float(user_height) ** 2
print("您的BMI指数为：" + str(user_bmi))
