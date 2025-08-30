# BMI = 体重 / （身高 ** 2）
# 1. 可以计算任意体重和身高的BMI值
# 2. 执行过程中打印一句话，“您的BMI分类为： xx”
# 3. 返回计算出的BMI值
def calculate_bmi(height, weight):
    user_bmi = float(weight) / float(height) ** 2
    if user_bmi <= 18.5:
        user_bmi_type = "偏瘦"
    elif user_bmi <= 25.0:
        user_bmi_type = "正常"
    elif user_bmi <= 30.0:
        user_bmi_type = "偏胖"
    else:
        user_bmi_type = "危险"
    print(f"您的BMI分类为: {user_bmi_type}")
    return user_bmi

user_bmi_1 = calculate_bmi(1.72, 60)
print("您的BMI指数为：" + str(user_bmi_1))