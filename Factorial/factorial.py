from tkinter import *
from tkinter.ttk import Combobox  # Import Combobox from tkinter.ttk
import math

def show():
    num = int(e1.get())
    fact = math.factorial(num)
    result_label.config(text=f"Factorial of {num} is: {fact}")
   

if __name__ == "__main__":
    root = Tk()
    root.configure(background="white")
    root.title("Factorial Calculator")
    root.geometry("350x200")
    root.resizable(False, False)

    l1 = Label(root, text="Enter Number")
    l1.place(x=20, y=30)

    e1 = Entry(root)
    e1.place(x=130, y=30)

    bt = Button(root, text="Submit", command=show)
    bt.place(x=100, y=60)

    result_label = Label(root, text="")
    result_label.place(x=20, y=90)  

    root.mainloop()
