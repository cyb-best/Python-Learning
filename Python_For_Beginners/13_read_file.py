# f = open("./data.txt", "r", encoding="utf-8")
# content = f.read()
# print(content)
# f.close()

# with open() as xxx (这样定义就不需要自己手动关闭文件流了)
with open("./data.txt", "r", encoding="utf-8") as f:
    # print(f.read())
    # print(f.readline())
    # print(f.readline())
    # print(f.readlines())
    lines = f.readlines()
    for line in lines:
        print(line)