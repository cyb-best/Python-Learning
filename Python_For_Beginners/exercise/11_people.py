friend_0 = {
    'first_name': 'chen',
    'last_name': 'angang',
    'age': 18,
    'city': '杭州'
}
print(friend_0)

favorite_number = {
    'cyb': 7,
    'xy': 2,
    'awx': 3,
    'ly': 6
}

for name, number in favorite_number.items():
    print(f"{name} favorite number is {number}.")
for name in favorite_number.keys():
    print(name.title())
for number in favorite_number.values():
    print(number)