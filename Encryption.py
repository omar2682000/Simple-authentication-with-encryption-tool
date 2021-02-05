from cryptography.fernet import Fernet


class Encryption:
    def __init__(self, text: str):
        self.__key = Fernet.generate_key()
        self.__encrypt = Fernet(self.__key)
        text = text.encode()
        self.__encrypt_text = self.__encrypt.encrypt(text)

    def get_text(self):
        return self.__encrypt_text

    def decrypt(self):
        result = self.__encrypt.decrypt(self.__encrypt_text)
        return result
