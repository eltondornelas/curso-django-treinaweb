class Address:
    def __init__(self, street, number, complement, district, city, country):
        self.__street = street
        self.__number = number
        self.__complement = complement
        self.__district = district
        self.__city = city
        self.__country = country

    @property
    def street(self):
        return self.__street

    @street.setter
    def street(self, street):
        self.__street = street

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number):
        self.__number = number

    @property
    def complement(self):
        return self.__complement

    @complement.setter
    def complement(self, complement):
        self.__complement = complement

    @property
    def district(self):
        return self.__district

    @district.setter
    def district(self, district):
        self.__district = district

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, city):
        self.__city = city

    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, country):
        self.__country = country
