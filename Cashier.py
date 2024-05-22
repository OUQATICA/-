class Cashier:
    def __init__(self, store, depname):
        self.__is_busy = False
        self.__queue = []
        self.__work_department = store.getDepartments()[depname]
        self.__store = store
        self.__revenue = 0

    def service(self):
        if len(self.__queue) != 0:
            if len(self.__queue[0].getstats()[3].items()) != 0:
                self.__is_busy = True
                for i in self.__queue[0].getstats()[3].items():
                    for j in self.__work_department.getprods():
                        if i[0] == j.stats()[0]:
                            self.__revenue += i[1]*j.stats()[1]
                            j.addrevenue(i[1]*j.stats()[1])
                self.__queue.pop(0)
            else:
                self.__queue.pop(0)
                self.__is_busy = False
        else:
            self.__is_busy = False

    def getlenqueue(self):
        return len(self.__queue)

    def addInQueue(self, customer):
        self.__queue.append(customer)

    def getIsBusy(self):
        return self.__is_busy

    def getrevenue(self):
        return self.__revenue