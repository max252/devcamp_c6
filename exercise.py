#!/usr/bin/python3


class User:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password

    def get_username(self):
        return self.__username


user = User("max", "superpassword")

print(user.get_username())
