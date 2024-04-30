#!/usr/bin/python3


class User:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password

    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password


user = User("max", "superpassword")

print(user.get_username())
print(user.get_password())
