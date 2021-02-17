from tkinter import *
from tkinter import messagebox
import datetime
import uuid

company = {
    'nazwa': 'FAQ - KOM',
    'miasto': '70-006 Szczecin',
    'ulica': 'ul. Cyfrowa 50',
    'typ': 'Sklep komputerowy',
    'NIP': 'NIP 054-845-34-81'
}

cash = {
    'Kasa:': '#01',
    'Kasjer:': '050'
}

bill_count = 0;

products = []
ilości = []
cenyJednostkowe = []
total = []


def welcome(window):
    Label(window, text=company['nazwa']).place(x=240, y=0)
    Label(window, text='PARAGON SOFT v1.0').place(x=218, y=20)


def saveProduct(window, productName, count, price, total):
    products.append(productName.get() + '  ' + count.get() + '*' + price.get() + ' PLN')
    ilości.append(float(count.get()))
    cenyJednostkowe.append(float(price.get()))
    total.append(float(count.get()) * float(price.get()))

    Label(window, text='DODANE PRODUKTY:').place(x=230, y=200)
    Label(window, text=products).place(x=100, y=220)

    Label(window, text='ŁĄCZNIE: ').place(x=450, y=300)
    Label(window, text=sum(total)).place(x=500, y=300)

    productName.delete(0, 'end')
    count.delete(0, 'end')
    price.delete(0, 'end')


# def time(paragon):
#     data = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     print(data)
#     Label(paragon, text=data).place(x=5, y=150)


def save(company, cash, products, total, payment, money):
    file = open('Paragon.txt', 'w', encoding='UTF-8')
    for key, value in company.items():
        file.write('\t\t  ' + value + '\n')
    file.write('''==================================================
                  PARAGON FISKALNY
==================================================\n''')
    file.write(datetime.datetime.now().strftime("%Y-%m-%d"))
    file.write(datetime.datetime.now().strftime("\t\t\t\t %H:%M:%S\n"))
    for key, value in cash.items():
        file.write(key + value + '\t\t\t\t')
    file.write('\n\n')
    n = 0
    s = 351
    for i in products:
        file.write(i)
        file.seek(s)
        file.write(str(total[n]) + ' A')
        n += 1
        s += 50
        file.write('\n')
    file.write('\n')
    file.write('SP.OP.A')
    file.seek(s)
    file.write(str(sum(total)))
    s+=50
    file.write('\n')
    file.write('PTU A 22%')
    file.seek(s)
    file.write(str(getTax()))
    s+=50
    file.write('\n')
    file.write('SUMA PTU')
    file.seek(s)
    file.write(str(getTax()))
    s+=50
    file.write('\n')
    file.write('SUMA')
    file.seek(s)
    file.write(str(getTax()+sum(total)))

    s+=50
    file.write('\n')
    file.write(payment.get().upper())

    if (payment.get() == 'Gotówka'):
        file.seek(s)
        file.write(money.get())
        s+=50
        file.write('\n\n')
        file.write('RESZTA')
        file.seek(s)
        file.write(str(calculateRest(money)))

    s+=50
    file.write('\n\n')
    file.write('P.fisk.')
    file.seek(s)
    ++bill_count
    file.write('Nr '+str(bill_count))
    s+=25
    file.write('\n\n')
    file.seek(s)
    file.write('AFN 563241561651563')

    file.close()


def getTax():
    return (sum(total) * 0.22);

def calculateRest(money):
    amount = float(money.get())
    return amount - sum(total)
