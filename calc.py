from tkinter import *


root = Tk()
root.title("My simple Calculator")
e = Entry(root, width=35, borderwidth=10)
e.grid(row=0, column=0, columnspan=5)


def on_click(number):
    current = e.get()
    e.delete(0, END)

    e.insert(0, str(current) + str(number))


def clear_btn():
    e.delete(0, END)
def add_func():
    first_num=e.get()
    global f_num
    global operator
    operator="addition"
    f_num=float(first_num)
    e.delete(0,END)
def sub_func():
    first_num = e.get()
    global f_num
    global operator
    operator = "subtraction"
    f_num = float(first_num)
    e.delete(0, END)
def multiply():
    first_num = e.get()
    global f_num
    global operator
    operator = "multiplication"
    f_num = float(first_num)
    e.delete(0, END)
def divide():
    first_num = e.get()
    global f_num
    global operator
    operator = "division"
    f_num = float(first_num)
    e.delete(0, END)


def equal_to():
    global second_num
    second_num=e.get()
    e.delete(0,END)
    if operator == "addition":
        e.insert(0, float(f_num) + float(second_num))
    if operator == "subtraction":
        e.insert(0, float(f_num) - float(second_num))
    if operator == "multiplication":
        e.insert(0, float(f_num) * float(second_num))
    if operator == "division":
        try:
            e.insert(0, float(f_num) / float(second_num))
        except ZeroDivisionError:

            e.insert(0,"Undefined")

            e.delete(0,END)









# define btn
button_1 = Button(root, text="1", pady=20, padx=40, command=lambda: on_click(1))
button_2 = Button(root, text="2", pady=20, padx=40, command=lambda: on_click(2))
button_3 = Button(root, text="3", pady=20, padx=40, command=lambda: on_click(3))
button_4 = Button(root, text="4", pady=20, padx=40, command=lambda: on_click(4))
button_5 = Button(root, text="5", pady=20, padx=40, command=lambda: on_click(5))
button_6 = Button(root, text="6", pady=20, padx=40, command=lambda: on_click(6))
button_7 = Button(root, text="7", pady=20, padx=40, command=lambda: on_click(7))
button_8 = Button(root, text="8", pady=20, padx=40, command=lambda: on_click(8))
button_9 = Button(root, text="9", pady=20, padx=40, command=lambda: on_click(9))
button_0 = Button(root, text="0", pady=20, padx=40, command=lambda: on_click(0))
button_add = Button(root, text="+", pady=20, padx=40, command=lambda: add_func())
button_sub = Button(root, text="-", pady=20, padx=40, command=lambda : sub_func())
button_multiply = Button(root, text="*", pady=20, padx=40, command=lambda : multiply())
button_divide = Button(root, text="/", pady=20, padx=40, command=lambda : divide())

button_equalto = Button(root, text="=", pady=20, padx=40,command=lambda: equal_to() )
button_clear = Button(root, text="clr", pady=20, padx=40, command=lambda: clear_btn())

button_7.grid(row=1, column=1)
button_4.grid(row=2, column=1)
button_1.grid(row=3, column=1)

button_8.grid(row=1, column=2)
button_5.grid(row=2, column=2)
button_2.grid(row=3, column=2)

button_9.grid(row=1, column=3)
button_6.grid(row=2, column=3)
button_3.grid(row=3, column=3)

button_clear.grid(row=4, column=1)
button_0.grid(row=4, column=2)
button_equalto.grid(row=4, column=3)

button_add.grid(row=1, column=4)
button_sub.grid(row=2, column=4)
button_multiply.grid(row=3, column=4)
button_divide.grid(row=4, column=4)

root.mainloop()
