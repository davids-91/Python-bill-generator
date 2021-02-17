from tkinter import *
from operations import *

window = Tk()
window.geometry("600x400")

welcome(window)

Label(window, text='Nazwa produktu:').place(x=200, y=50)
product = Entry(window)
product.place(x=295, y=50)

Label(window, text='Ilość:').place(x=200, y=70)
count = Entry(window)
count.place(x=235, y=70)

Label(window, text='Cena jednostkowa (kropka zamiast przecinka):').place(x=40, y=90)
price = Entry(window)
price.place(x=290, y=90)

# Add a grid
mainframe = Frame(window)
mainframe.grid(column=0,row=0, sticky=(N,W,E,S) )
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)
mainframe.pack(pady = 110, padx = 100)

# Create a Tkinter variable
payment = StringVar(window)

# Dictionary with options
choices = { 'Gotówka','Karta'}
payment.set('Gotówka') # set the default option

popupMenu = OptionMenu(mainframe, payment, *choices)
Label(mainframe, text="Płatność").grid(row = 1, column = 1)
popupMenu.grid(row = 1, column =2)

# # on change dropdown value
# def change_dropdown(*args):
#     refresh(window)
#
# # link function to change dropdown
# payment.trace('w', change_dropdown)

if (payment.get() == 'Gotówka'):
    Label(window, text='Gotówka:').place(x=200, y=140)
    money = Entry(window)
    money.place(x=250, y=140)

b1 = Button(window, text='Dodaj', command=lambda: saveProduct(window, product, count, price, total))
b1.place(x=220, y=160)
b2 = Button(window, text='Zakończ', command=lambda: save(company, cash, products, total, payment, money))
b2.place(x=270, y=160)


window = mainloop()