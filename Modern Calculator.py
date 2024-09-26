from tkinter import *
from customtkinter import *

app = CTk()
app.title("Calculator by Saksham")
app.geometry("592x285+150+50")
app.resizable(False,False)

string = StringVar()
equation = ""

def show(n):
    global equation
    equation += n
    string.set(equation)

def clear():
    global equation
    string.set("")
    equation = ""

def equal():
    try:
        global equation
        result = str(eval(equation))
        string.set(result)
        equation = ""
    except:
        string.set("Invalid Operation")
        equation = ""

entry = CTkEntry(master=app, width=570, height=30, font=CTkFont("Comic", 30), justify = RIGHT, textvariable=string)
entry.place_configure(x=12, y=10)

divide_btn = CTkButton(master=app, font=CTkFont("Comic", 28), text="/", fg_color="blue", command=lambda: show("/"))
divide_btn.place_configure(x=12, y=60)

multiply_btn = CTkButton(master=app, font=CTkFont("Comic", 28), text="*", fg_color="blue", command=lambda: show("*"))
multiply_btn.place_configure(x=155, y=60)

power_btn = CTkButton(master=app, font=CTkFont("Comic", 28), text="**", fg_color="blue", command=lambda: show("**"))
power_btn.place_configure(x=298, y=60)

clear_btn = CTkButton(master=app, font=CTkFont("Comic", 28), text="C", fg_color="red", command=lambda: clear())
clear_btn.place_configure(x=441, y=60)

seven_btn = CTkButton(master=app, font=CTkFont("Comic", 28), text="7", fg_color="orange", command=lambda: show("7"))
seven_btn.place_configure(x=12, y=103)

eight_btn = CTkButton(master=app, font=CTkFont("Comic", 28), text="8", fg_color="orange", command=lambda: show("8"))
eight_btn.place_configure(x=155, y=103)

nine_btn = CTkButton(master=app, font=CTkFont("Comic", 28), text="9", fg_color="orange", command=lambda: show("9"))
nine_btn.place_configure(x=298, y=103)

plus_btn = CTkButton(master=app, font=CTkFont("Comic", 28), text="+", fg_color="blue", command=lambda: show("+"))
plus_btn.place_configure(x=441, y=103)

four_btn = CTkButton(master=app, font=CTkFont("Comic", 28), text="4", fg_color="orange", command=lambda: show("4"))
four_btn.place_configure(x=12, y=146)

five_btn = CTkButton(master=app, font=CTkFont("Comic", 28), text="5", fg_color="orange", command=lambda: show("5"))
five_btn.place_configure(x=155, y=146)

six_btn = CTkButton(master=app, font=CTkFont("Comic", 28), text="6", fg_color="orange", command=lambda: show("6"))
six_btn.place_configure(x=298, y=146)

minus_btn = CTkButton(master=app, font=CTkFont("Comic", 28), text="-", fg_color="blue", command=lambda: show("-"))
minus_btn.place_configure(x=441, y=146)

one_btn = CTkButton(master=app, font=CTkFont("Comic", 28), text="1", fg_color="orange", command=lambda: show("1"))
one_btn.place_configure(x=12, y=189)

two_btn = CTkButton(master=app, font=CTkFont("Comic", 28), text="2", fg_color="orange", command=lambda: show("2"))
two_btn.place_configure(x=155, y=189)

three_btn = CTkButton(master=app, font=CTkFont("Comic", 28), text="3", fg_color="orange", command=lambda: show("3"))
three_btn.place_configure(x=298, y=189)

point_btn = CTkButton(master=app, font=CTkFont("Comic", 28), text=".", fg_color="dark blue", command=lambda: show("."))
point_btn.place_configure(x=441, y=189)

zero_btn = CTkButton(master=app, font=CTkFont("Comic", 28), text="0", fg_color="orange", width=213, command=lambda: show("0"))
zero_btn.place_configure(x=12, y=232)

zero2_btn = CTkButton(master=app, font=CTkFont("Comic", 28), text="00", fg_color="orange", width=210, command =lambda: show("00"))
zero2_btn.place_configure(x=228, y=232)

equal_btn = CTkButton(master=app, font=CTkFont("Comic", 28), text="=", fg_color="green", command=lambda: equal())
equal_btn.place_configure(x=441, y=232)

app.mainloop()