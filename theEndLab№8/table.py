from prettytable import PrettyTable

from data import dt

x = PrettyTable()

x.field_names = ["Код","Назва Банку","Рік","Зміни $ на 1.11","Зміни $ на 1.12","Курс $ на 1.12","Зміни ФРН на 1.11", "Зміни ФРН на 1.12","Курс ФРН на 1.12"]

for i in range(0, len(dt)):
    x.add_rows(
        [
            dt[i]
        ]
    )

def openTabble():
    print('\nАНАЛИЗ ЗМІНИ ЦІН')
    print(x)