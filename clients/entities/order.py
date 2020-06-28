class Order:
    def __init__(self, client, order_date, value, status, observations,
                 products):
        self.__client = client
        self.__order_date = order_date
        self.__value = value
        self.__status = status
        self.__observations = observations
        self.__products = products

    @property
    def client(self):
        return self.__client

    @client.setter
    def client(self, client):
        self.__client = client

    @property
    def order_date(self):
        return self.__order_date

    @order_date.setter
    def order_date(self, order_date):
        self.__order_date = order_date

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        self.__status = status

    @property
    def observations(self):
        return self.__observations

    @observations.setter
    def observations(self, observations):
        self.__observations = observations

    @property
    def products(self):
        return self.__products

    @products.setter
    def products(self, products):
        self.__products = products
