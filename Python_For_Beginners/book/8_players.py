# 切片
players = ['stephen', 'john', 'jack', 'tom', 'lucy', 'bella']
print(players[0:2])
print(players[1:3])
print(players[:3])
print(players[-3:])

for player in players[:3]:
    print(player)

copy_players = players[:]
print(copy_players)