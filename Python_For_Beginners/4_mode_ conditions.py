# BMI = 体重 / （身高 ** 2）
user_weight = input("请输入您的体重(kg)：")
user_height = input("请输入您的身高(m): ")
user_bmi = float(user_weight) / float(user_height) ** 2
print("您的BMI指数为：" + str(user_bmi))

if user_bmi <= 18.5:
    print("您当前偏瘦，请注意饮食 ")
elif 18.5 < user_bmi <= 25.0:
    print("您当前的情况正常，请继续保持")
elif 25 < user_bmi <= 30.0:
    print("您当前的体重偏胖，请控制饮食")
else:
    print("危险！！！！！")

