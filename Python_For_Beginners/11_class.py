class User:
    def __init__(self, user_name):
        self.name = user_name

    def print_user_name(self):
        print(self.name)

user1 = User("cyb")
user2 = User("xy")
user1.print_user_name()
user2.print_user_name()
user1.name = "json"
user1.print_user_name()