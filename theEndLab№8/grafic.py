import matplotlib.pyplot as plt

a_price = [1.2000, 1.0462, 1.0370]
b_price = [1.1667, 1.0294, 1.0714]
c_price = [1.0147, 1.0444, 1.0020]
j_price = [1.1594, 1.0213, 1.0176]
year = ["2003", "2004", "2005" ]

plt.plot(year,a_price,label = "Зміни $ на 1.11 INKO")
plt.plot(year,b_price,label = "Зміни $ на 1.12 INKO")
plt.plot(year,c_price,label = "Зміни ФРН на 1.11 INKO")
plt.plot(year,j_price,label = "Зміни ФРН на 1.12 INKO")
plt.xlabel("Дата")
plt.ylabel("Ціна")
plt.legend()
plt.grid(True)

def showplot():
    plt.show()