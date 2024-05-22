from functions import dictgen
from Customer import Customer
import random as rd


class Department:
    def __init__(self, name):
        self.__name = name
        self.__products = []
        self.__cashiers = []
        self.__customers = []
        self.__average_customers = 0
        self.__average_purchase_amount = 0
        self.__prods_not_wait = []

    def getprods(self):
        return self.__products

    def findCashierWithMinQueueLength(self):
        minlen = self.__cashiers[0]
        for i in self.__cashiers:
            if i.getlenqueue() < minlen.getlenqueue():
                minlen = i
        return minlen

    def addcashiers(self, *cashier):
        self.__cashiers.extend(cashier)

    def getcashiers(self):
        return self.__cashiers

    def addCustomers(self, count):
        names = ['Sarah Elliott', 'George Dennis', 'June Lawrence', 'Gladys Smith', 'Wesley Maxwell', 'Raymond Snyder', 'Hugh Martin', 'Jill Hall', 'Beth Glover', 'Linda Harris']
        for i in range(count):
            if self.__name == 'Техника':
                self.__customers.append(Customer(rd.choice(names), 1000, dictgen(["микроволновка", "сушилка для продуктов", "клавиатура", "телевизор"])))
            elif self.__name == "Продукты":
                self.__customers.append(Customer(rd.choice(names), 1000, dictgen(['хлеб', 'молоко', 'кефир', 'йогурт'])))
            elif self.__name == "Одежда":
                self.__customers.append(Customer(rd.choice(names), 1000, dictgen(["юбка", "шорты", "шапка биффало", "утепленные джинсы"])))

    def getCustomers(self):
        return self.__customers

    def delcustomers(self):
        self.__customers = []

    def setProducts(self, *prods):
        self.__products.extend(prods)

    def addProducts(self):
        for i in self.__products:
            i.setCount(rd.randint(0, 5))

    def getname(self):
        return self.__name

    def getprodsnotwait(self):
        return self.__prods_not_wait

    def addprodsnotwait(self, prod):
        self.__prods_not_wait.append(prod)

