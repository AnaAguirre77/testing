# usuario.py
class Usuario:
    def __init__(self, id, username, DNI, password, email):
        self.__id = id
        self.__username = username
        self.__DNI = DNI  
        self.__password = password
        self.__email = email

    # get y set para id
    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    # get y set para username
    def get_username(self):
        return self.__username

    def set_username(self, username):
        self.__username = username

    # get y set para DNI
    def get_DNI(self):
        return self.__DNI

    def set_DNI(self, DNI):
        self.__DNI = DNI

    # get y set para password
    def get_password(self):
        return self.__password

    def set_password(self, password):
        self.__password = password

    # get y set para email
    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def __str__(self):
        return f"Usuario(ID: {self.__id}, Username: {self.__username}, DNI: {self.__DNI}, Email: {self.__email})"