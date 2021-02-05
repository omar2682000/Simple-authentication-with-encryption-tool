from Encryption import Encryption


class User:
    def __init__(self, username=None, password=None, *args):
        self.username = username
        self.password = Encryption(password)
        self.extra_data = args
