# 数据结构：字典 ==> k-v健值对 {}
phone_dict = {"cyb": 12345678910,
              "xy": 9876543210}
phone_dict["awx"] = 77829901000
phone_dict["zjy"] = 77829901001
phone_dict["dsf"] = 77829901002
phone_dict["ldl"] = 77829901003

query = input("请输入您要查询用户的姓名：")
if query in phone_dict:
    print("你查询的用户信息如下")
    print("姓名：" + query + "\n" + "电话：" + str(phone_dict[query]))
else:
    print("通讯录未查询到该用户信息：" + query)
    print("目前通讯录中的总个数为：" + str(len(phone_dict)) + "个。")

print("打印所有信息")
for key, value in phone_dict.items():
    print(key)
    print(value)