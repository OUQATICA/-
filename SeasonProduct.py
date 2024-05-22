import math

from Product import Product


class SeasonProduct(Product):
    def __init__(self, name, price, product_type, seasonal_coefficient):
        super().__init__(name, price, product_type)
        self.__seasonal_coefficient = seasonal_coefficient
        self.__price = super().stats()[1]
        self.__is_changed = False

    def stats(self):
        return *super().stats(), self.__seasonal_coefficient

    def seasonprice(self, t):
        if super().stats()[0] == 'юбка' or super().stats()[0] == "шорты":
            if 10 > t%20 > 0:
                if not self.__is_changed:
                    super().setprice(round(super().stats()[1]*self.__seasonal_coefficient))
                    self.__is_changed = True
            else:
                super().setprice(self.__price)
                self.__is_changed = False
        elif super().stats()[0] == 'утепленные джинсы' or super().stats()[0] == "шапка биффало":
            if 20 > t%20 > 10:
                if not self.__is_changed:
                    super().setprice(round(super().stats()[1]*self.__seasonal_coefficient))
                    self.__is_changed = True
            else:
                self.__is_changed = False
                super().setprice(self.__price)

    def ischanged(self):
        return self.__is_changed
