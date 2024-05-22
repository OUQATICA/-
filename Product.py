class Product:
    def __init__(self, name, price, product_type):
        self.__name = name
        self.__price = price
        self.__product_type = product_type
        self.__count = [''*10]
        self.__revenue = 0

    def stats(self):
        return self.__name, self.__price, self.__product_type, self.__revenue

    def addrevenue(self, rev):
        self.__revenue += rev

    def getlenCount(self):
        return len(self.__count)

    def Count(self):
        return self.__count

    def setCount(self, count):
        self.__count.append(''*count)

    def setprice(self, price):
        self.__price = price
