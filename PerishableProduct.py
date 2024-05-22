from Product import Product


class PerishableProduct(Product):
    def __init__(self, name, price, product_type, expiry_date):
        super().__init__(name, price, product_type)
        self.__expiry_date = expiry_date
        super()
        self.__count = [str(self.__expiry_date) for i in range(10)]

    def setCount(self, count):
        self.__count.extend(str(self.__expiry_date) for i in range(count))

    def getlenCount(self):
        return len(self.__count)

    def Count(self):
        return self.__count

    def delcountelem(self):
        res = []
        for i in self.__count:
            if i != '0':
                res.append(i)
        self.__count = res
