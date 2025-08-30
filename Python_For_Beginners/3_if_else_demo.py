# 条件控制语句[注意缩进]
isHappy = True
if isHappy:
    print("你今天很开心")
else:
    print("你今天不开心")
isHappy = False
if isHappy:
    print("你今天很开心")
else:
    print("你今天不开心")

# 判断今晚打游戏，对象是否会生气
mood_index = float(input("对象今天的心情指数是: "))
if mood_index >= 60:
    print("恭喜今天，应该可以打游戏😄")
else:
    print("你惨咯，敢打游戏试试呢？？？")