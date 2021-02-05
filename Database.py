from User import User
from collections import defaultdict


class Database:
    def __init__(self):
        self.database = defaultdict(User)
        self.number_of_users = 0

    @staticmethod
    def valid_password(password):
        capital = 0
        small = 0
        number = 0
        special_char = list("!@#$%^&*()_+=-`~/\"|';:>.<,\\")
        special = 0
        for c in password:
            if c.isnumeric():
                number += 1
            elif c.isupper():
                capital += 1
            elif c.islower():
                small += 1
            elif c in special_char:
                special += 1
        return bool(capital) and bool(small) and bool(number) and bool(special) and (len(password) >= 6)

    def add_user(self, username, password, *args):
        if not Database.valid_password(password):
            raise Exception("Password is not valid!")
        if username in self.database[username]:
            raise Exception("Username already exists!")
        self.database[username] = User(username, password, kwargs)
        return
