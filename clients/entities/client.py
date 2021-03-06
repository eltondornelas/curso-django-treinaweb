class Client:
    def __init__(self, name, lastname, sex, birthday, email, profession, address):
        self.__name = name
        self.__lastname = lastname
        self.__sex = sex
        self.__birthday = birthday
        self.__email = email
        self.__profession = profession
        self.__address = address

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def lastname(self):
        return self.__lastname

    @lastname.setter
    def lastname(self, lastname):
        self.__lastname = lastname

    @property
    def sex(self):
        return self.__sex

    @sex.setter
    def sex(self, sex):
        self.__sex = sex

    @property
    def birthday(self):
        return self.__birthday

    @birthday.setter
    def birthday(self, birthday):
        self.__birthday = birthday

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def profession(self):
        return self.__profession

    @profession.setter
    def profession(self, profession):
        self.__profession = profession

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address):
        self.__address = address
