# 列表中嵌套字典
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'black', 'points': 10}
alien_2 = {'color': 'pink', 'points': 6}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

# 字典中嵌套列表
favorite_languages = {
    'cyb': ['Python', 'Java'],
    'xy': ['C++', 'Java'],
    'awx': ['PHP', 'MySQL']
}
for name, languages in favorite_languages.items():
    print(f"{name} favorite languages are:")
    for language in languages:
        print("\t" + language.title())

# 字典中嵌套字典
users = {
    'cyb': {
        'nick_name': 'chenangang',
        'age': 18,
        'gender': 'man'
    },
    'xy': {
        'nick_name': 'xiongjiujiu',
        'age': 18,
        'gender': 'woman'
    }
}
print(users)