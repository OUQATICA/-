import random as rd
from functions import dictgen
from Customer import Customer


class Store:
    def __init__(self):
        self.__departments = []
        self.__average_customers = []
        self.__average_purchase_amount = []
        self.__not_wait = 0

    def addDepartments(self, *departments):
        self.__departments.extend(departments)

    def getDepartments(self):
        return self.__departments

    def getaveragecustomers(self):
        return round(sum(self.__average_customers)/len(self.__average_customers), 3)

    def setaveragecustomers(self, count):
        self.__average_customers.extend(count)

    def getaveragepurchaseamount(self):
        return round(sum(self.__average_purchase_amount)/len(self.__average_purchase_amount), 3)

    def setaveragepurchaseamount(self, count):
        self.__average_purchase_amount.extend(count)

    def getnotwait(self):
        return self.__not_wait

    def addnotwait(self, count):
        self.__not_wait += count