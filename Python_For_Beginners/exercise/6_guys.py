invite_guys = ['xy', 'awx', 'zjy']
print(invite_guys)
print(invite_guys[1] + "无法参加聚会")
invite_guys[1] = 'ly'
print(invite_guys)
print("我找到了一个更大餐桌，可以再邀请三位好友前来聚餐")
invite_guys.insert(0, 'xjh')
invite_guys.insert(int(len(invite_guys) / 2), 'dsf')
invite_guys.append('lll')
print(invite_guys)
print("很抱歉，餐桌无法及时送达，只能保留两位嘉宾")
while len(invite_guys) != 2:
    print(invite_guys[-1] + "很遗憾，您无法参加聚餐")
    invite_guys.pop()
print(invite_guys)
del invite_guys[0]
del invite_guys[0]
print(invite_guys)

