import locale
import random
import tkinter as tk
from tkinter import ttk
from Store import Store
from Product import Product
from PerishableProduct import PerishableProduct
from SeasonProduct import SeasonProduct
from Department import Department
from Customer import Customer
from Cashier import Cashier


class ShopSimulationApp:
    def __init__(self, root):
        self.__t = 0
        self.__time_stop = False
        self.__root = root
        self.__root.title("Магазин")
        self.__root.geometry("900x620")

        self.__store = Store()
        self.__store.addDepartments(Department('Техника'), Department('Продукты'), Department('Одежда'))
        self.__store.getDepartments()[0].setProducts(Product('микроволновка', 60, 'домашняя техника'),
                                                     Product('сушилка для продуктов', 70, 'домашняя техника'),
                                                     Product('клавиатура', 50, 'компьютерная техника'),
                                                     Product('телевизор', 120, 'домашняя техника'))
        self.__store.getDepartments()[0].addcashiers(Cashier(self.__store, 0), Cashier(self.__store, 0))
        self.__store.getDepartments()[1].setProducts(PerishableProduct('хлеб', 4, 'хлебобулочные изделия', 120),
                                                     PerishableProduct('молоко', 6, 'молочные изделия', 120),
                                                     PerishableProduct('кефир', 7, 'молочные изделия', 240),
                                                     PerishableProduct('йогурт', 7, 'молочные изделия', 120))
        self.__store.getDepartments()[1].addcashiers(Cashier(self.__store, 1), Cashier(self.__store, 1))
        self.__store.getDepartments()[2].setProducts(SeasonProduct('юбка', 40, 'летняя одежда', 1.2),
                                                     SeasonProduct('шорты', 60, 'летняя одежда', 1.3),
                                                     SeasonProduct('шапка биффало', 70, 'зимняя одежда', 1.1),
                                                     SeasonProduct('утепленные джинсы', 70, 'зимняя одежда', 1.8))
        self.__store.getDepartments()[2].addcashiers(Cashier(self.__store, 2), Cashier(self.__store, 2))

        self.__info_label = tk.Label(root)
        self.__info_label.config(width=900, justify='right')
        self.__time_label = tk.Label(self.__info_label, font=("Arial", 12))
        self.__info_button = tk.Button(self.__info_label, text='Статистика', command=self.open_info_window)

        self.__info_button.pack(side='left', anchor='nw', padx=10, pady=10)
        self.__time_label.pack(side="right", anchor="ne", padx=10, pady=10)

        self.__cashiers_label = tk.Label(root, text="Кассы:")
        self.__cashiers_tree = ttk.Treeview(root, columns=("Name", "Status", "Show"), show="headings")
        self.__cashiers_tree.heading("Name", text="Отдел")
        self.__cashiers_tree.heading("Status", text="Статус")
        self.__cashiers_tree.heading("Show", text="Выручка")

        self.__rev_label = tk.Label(root, text='Выручка')
        self.__rev_tree = ttk.Treeview(root, columns=('Name', 'Revenue'), show='headings')
        self.__rev_tree.heading("Name", text='Отдел')
        self.__rev_tree.heading("Revenue", text='Выручка')

        self.update()

    def revenuetable(self):
        self.__rev_tree.delete(*self.__rev_tree.get_children())
        all_revenue = 0
        for i in self.__store.getDepartments():
            revenue = 0
            for prod in i.getprods():
                revenue += prod.stats()[3]
            all_revenue += revenue
            self.__rev_tree.insert('', 'end',  values=(i.getname(), revenue))
        self.__rev_tree.insert('', 'end', values=("Всего", all_revenue))
        self.__rev_tree.pack(padx=20, pady=5)

    def cashierstable(self):
        self.__cashiers_tree.delete(*self.__cashiers_tree.get_children())
        for i in self.__store.getDepartments():
            for j in i.getcashiers():
                self.__cashiers_tree.insert('', 'end', values=(i.getname(), 'занят' if j.getIsBusy() else 'покупатели обслужены', j.getrevenue()))
        self.__cashiers_tree.pack(padx=20, pady=5)

    def open_info_window(self):
        self.stop()
        info_window = tk.Toplevel()
        info_window.title("Статистика")
        info_window.geometry('850x400')
        info_frame = tk.Frame(info_window)
        info_frame.pack(padx=10, pady=10)
        options = ["Товары", "Виды товаров", "Скоропортящиеся товары", "Сезонные товары", "Покупатели"]

        self.__dropdown = tk.StringVar(info_frame)
        self.__dropdown.set(options[0])
        dropdown_menu = tk.OptionMenu(info_frame, self.__dropdown, *options)
        dropdown_menu.pack()

        show_table_button = tk.Button(info_frame, text="Показать таблицу", command=self.show_table)
        show_table_button.pack()
        self.__table_frame = tk.Frame(info_frame)
        self.__table_frame.pack()
        info_window.protocol("WM_DELETE_WINDOW", lambda: (info_window.destroy(), self.resume()))

    def stop(self):
        self.__time_stop = True

    def resume(self):
        self.__time_stop = False
        self.update()

    def show_table(self):
        selected_value = self.__dropdown.get()
        if self.__table_frame.winfo_children():
            for widget in self.__table_frame.winfo_children():
                widget.destroy()

        scrollbar = tk.Scrollbar(self.__table_frame)
        scrollbar.pack(side="right", fill="y")

        if selected_value == "Товары":
            columns = ("Название", "Цена", 'Кол-во в магазине', "В магазине на")
            data = []
            for i in self.__store.getDepartments():
                for j in i.getprods():
                    data.append((j.stats()[0], j.stats()[1], j.getlenCount(), j.getlenCount() * j.stats()[1]))

        elif selected_value == "Виды товаров":
            columns = ("Название", "Продано на", "Кол-во в магазине", 'В магазине на')
            data = []
            prodtypes = set()
            counts = {}
            for i in self.__store.getDepartments():
                for j in i.getprods():
                    if j.stats()[2] not in prodtypes:
                        data.append([j.stats()[2]])
                        prodtypes.add(j.stats()[2])
                        counts[j.stats()[2]] = [j.stats()[3], j.getlenCount(), j.getlenCount() * j.stats()[1]]
                    else:
                        counts[j.stats()[2]][0] += j.stats()[3]
                        counts[j.stats()[2]][1] += j.getlenCount()
                        counts[j.stats()[2]][2] += j.getlenCount() * j.stats()[1]

            for i in data:
                i.extend(counts[i[0]])
        elif selected_value == "Скоропортящиеся товары":
            def gendataforPerishableProducts():
                data = []
                for i in self.__store.getDepartments():
                    if i.getname() == 'Продукты':
                        for j in i.getprods():
                            l = [0, 0]
                            if isinstance(j, PerishableProduct):
                                for c in j.Count():
                                    if int(c) <= int(self.__steps.get()):
                                        l[0] += 1
                                        l[1] += j.stats()[1]
                                data.append((j.stats()[0], j.stats()[1], *l))

                for child in self.__table.get_children():
                    self.__table.delete(child)

                for col in columns:
                    self.__table.heading(col, text=col)
                for row in data:
                    self.__table.insert("", "end", values=row)
                self.__table.pack()

            data = []
            text = tk.Label(self.__table_frame, text='В магазине имеется скоропортящегося товара со сроком хранения не более введенного числа шагов по времени:')
            text.pack(anchor='ne')
            self.__steps = tk.Entry(self.__table_frame, width=10)
            self.__steps.insert(0, '200')
            vcmd = self.__table_frame.register(self.validate_input)
            self.__steps.config(validate="key", validatecommand=(vcmd, '%P'))
            self.__steps.pack(padx=10, pady=10, anchor='ne')
            columns = ("Название", "Цена", "Кол-во в магазине", "В магазине на")
            steps_button = tk.Button(self.__table_frame, text='Показать', command=gendataforPerishableProducts)
            steps_button.pack(padx=10, pady=10, anchor='ne')

        elif selected_value == "Сезонные товары":
            columns = ("Название", "Цена", "Измененная Цена")
            data = []
            for i in self.__store.getDepartments():
                if i.getname() == 'Одежда':
                    for j in i.getprods():
                        if isinstance(j, SeasonProduct):
                            data.append((j.stats()[0], j.stats()[1], "Да" if j.ischanged() else 'Нет'))

        elif selected_value == "Покупатели":
            columns = ('№ шага', 'Ср. Кол-во за шаг по времени', "Ср. сумма покупки", 'Кол-во недождавшихся очереди')
            data = [(self.__t, self.__store.getaveragecustomers(), self.__store.getaveragepurchaseamount(), self.__store.getnotwait())]

        self.__table = ttk.Treeview(self.__table_frame, yscrollcommand=scrollbar.set, columns=columns, show="headings")

        for col in columns:
            self.__table.heading(col, text=col)

        for row in data:
            self.__table.insert("", "end", values=row)

        self.__table.pack(pady=10, expand=True, fill="both")

    def validate_input(self, new_value):
        return new_value.isdigit() or new_value == ""


    def update(self):
        if not self.__time_stop:
            self.__time_label.config(text=f'Текущее время: {self.__t}')
            self.__info_label.pack()
            self.__cashiers_label.pack(pady=10)
            self.cashierstable()
            self.__rev_label.pack(pady=10)
            self.revenuetable()
            self.priceupdate()
            self.spawncustomers()
            self.service()
            self.spawnproducts()
            self.__root.after(1000, self.update)
            self.__t += 1

    def priceupdate(self):
        for i in self.__store.getDepartments():
            if i.getname() == 'Одежда':
                for j in i.getprods():
                    if isinstance(j, SeasonProduct):
                        j.seasonprice(self.__t)
    def spawncustomers(self):
        aver_cust = []
        aver_purch_amount = []
        for i in self.__store.getDepartments():
            rand = random.randint(0, 4)
            aver_cust.append(rand)
            i.addCustomers(rand)
            for j in i.getCustomers():
                j.topUpCart(i.getprods())
                res = 0
                for prod_c in j.getstats()[3].items():
                    for prod in i.getprods():
                        if prod_c[0] == prod.stats()[0]:
                            res += prod_c[1]*prod.stats()[1]
                aver_purch_amount.append(res)
                if i.findCashierWithMinQueueLength().getlenqueue() < j.getmaxqueuelen():
                    i.findCashierWithMinQueueLength().addInQueue(j)
                else:
                    i.addprodsnotwait(j.getstats()[3])
                    self.__store.addnotwait(1)
            i.delcustomers()
        self.__store.setaveragecustomers(aver_cust)
        self.__store.setaveragepurchaseamount(aver_purch_amount)

    def spawnproducts(self):
        for i in self.__store.getDepartments():
            if len(i.getprodsnotwait()) != 0:
                for prodnw in i.getprodsnotwait():
                    for prod in i.getprods():
                        for prods in prodnw.items():
                            if prod.stats()[0] == prods[0]:
                                prod.setCount(prods[1])
            if random.randint(0, 2) == 0:
                i.addProducts()

    def delperishableproducts(self):
        for i in self.__store.getDepartments():
            if i.getname() == 'Продукты':
                for j in i.getprods():
                    if isinstance(j, PerishableProduct):
                        for prod in range(j.getlenCount()):
                            if int(j.Count()[prod]) > 0:
                                j.Count()[prod] = str(int(j.Count()[prod])-1)
                        j.delcountelem()

    def service(self):
        for i in self.__store.getDepartments():
            for j in i.getcashiers():
                j.service()
