import random


class Customer:
    def __init__(self, name, money, desired_products: dict):
        self.__name = name
        self.__cart = {}
        self.__desired_products = desired_products
        self.__money = money
        self.__max_queue_len = random.randint(5, 10)

    def getstats(self):
        return self.__name, self.__money, self.__desired_products, self.__cart

    def topUpCart(self, prods):
        for i in prods:
            for j in self.__desired_products:
                if j == i.stats()[0]:
                    if i.getlenCount() >= self.__desired_products[j]:
                        self.__cart[i.stats()[0]] = self.__desired_products[j]
                        i.setCount(-self.__desired_products[j])
                    elif i.getlenCount() == 0:
                        continue
                    else:
                        self.__cart[i.stats()[0]] = i.getlenCount()
                        i.setCount(-i.getlenCount())

    def getmaxqueuelen(self):
        return self.__max_queue_len
