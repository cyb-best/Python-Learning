# w 只写，注意每次调用会先清空文件再写，如果需要追加写用a模式
with open("./poem.txt", "w", encoding="utf-8") as f:
    f.write("我欲乘风归去\n")
    f.write("又恐琼楼玉宇\n")
    f.write("高处不胜寒\n")

with open("./poem.txt", "a", encoding="utf-8") as f:
    f.write("起舞弄清影\n")
    f.write("何似在人间")