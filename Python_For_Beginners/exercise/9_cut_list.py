players = ['stephen', 'john', 'jack', 'tom', 'lucy', 'bella', 'xy']
print("列表前三个元素为: " + str(players[:3]))
list_len = int(len(players) / 2)
print("列表中间的三个元素为：" + str(players[list_len : list_len + 3]))
print("列表最后三个元素分别为：" + str(players[-3:]))
