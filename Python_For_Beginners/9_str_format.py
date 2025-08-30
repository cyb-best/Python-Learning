gpa_dict = {"cyb": 3.132, "xy": 4.123, "awx": 3.111}
for name, gpa in gpa_dict.items():
    # print("{0}您好， 您当前的绩点为：{1:.2f}".format(name, gpa))
    print(f"{name}您好，您当前的绩点为：{gpa:.2f}")