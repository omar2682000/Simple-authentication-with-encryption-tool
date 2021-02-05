from Database import Database


class Authentication:
    def __init__(self):
        self.__data = Database()

    def register(self):
        username = input("Type in your username: ")
        password = input("Type in your password: ")
        extra_data = []
        print("Have more data?")
        answer = (True if input() == "Yes" else False)
        if answer:
            data = input()
            while data != '' and data != '\n':
                extra_data.append(data)
                data = input()
        self.__data.add_user(username, password, (extra_data if len(extra_data) > 1 else None))
        return

    def login(self):
        username = input("Type in your username: ")
        password = input("Type in your password: ")
        if username not in self.__data.database.keys():
            raise Exception("User does not exist!")
        user = self.__data.database[username]
        if password == user.password.decrypt():
            print("Welcome!")
            return True
        else:
            print("Invalid data!")
            return False
