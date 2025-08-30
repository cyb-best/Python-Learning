# 持续拍照片，从天空亮度为510开始，直至天空亮度低于500，停止拍照
# measure_brightness = 510 # 模拟天空亮度
# while measure_brightness >= 500:
#     print("拍照，此时天空亮度为: " + str(measure_brightness)) # 模拟拍照动作
#     measure_brightness -= 1
# print("拍照结束，此时天空亮度为：" + str(measure_brightness))

# 设计一个求平均值的程序
total = 0.0
count = 0
user_input = input("请输入数字(完成所有数字输入后，输入q退出): ")
while user_input != "q":
    count = count + 1
    total += float(user_input)
    user_input = input("请输入数字(完成所有数字输入后，输入q退出): ")
# 防止除0操作
if count == 0:
    result = 0
else:
    result = total / count
print("平均值为：" + str(result))