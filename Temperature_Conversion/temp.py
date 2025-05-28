from tkinter import *
import math

def show():
    c = float(e1.get())
    temp, temp1 = 0, 0
    
    if v.get() == 1:
        temp = (c * 9/5) + 32
        result_label.config(text="Fahrenheit conversion is : {:.2f}".format(temp))
    elif v.get() == 2:
        temp1 = c + 273.15
        result_label.config(text="Kelvin conversion is : {:.2f}".format(temp1))

if __name__ == "__main__":
    root = Tk()
    root.configure(background="white")
    root.title("Temperature Converter")
    root.geometry("450x250")
    root.resizable(False, False)

    l1 = Label(root, text="Enter Temperature in Celsius")
    l1.place(x=20, y=30)

    e1 = Entry(root)
    e1.place(x=190, y=30)

    l2 = Label(root, text="Choose Converter : ")
    l2.place(x=20, y=60)
    
    v = IntVar()
    r1 = Radiobutton(root, text="Fahrenheit", variable=v, value=1)
    r2 = Radiobutton(root, text="Kelvin", variable=v, value=2)
    r1.place(x=150, y=60)
    r2.place(x=250, y=60)
    
    bt = Button(root, text="Submit", command=show)
    bt.place(x=100, y=90)

    result_label = Label(root, text="")
    result_label.place(x=20, y=120)

    root.mainloop()
