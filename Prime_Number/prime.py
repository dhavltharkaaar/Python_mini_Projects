from tkinter import *
from tkinter import ttk
import math

def show():
    input_num = int(e1.get())
    flag = False 

    if input_num == 1:
        result_label.config(text="Input number is a prime number: " + str(input_num))
    elif input_num > 1:
        for i in range(2, int(math.sqrt(input_num)) + 1):
            if (input_num % i) == 0:
                flag = True
                break
        if flag:
            result_label.config(text="Input number is not a prime number: " + str(input_num))
        else:
            result_label.config(text="Input number is a prime number: " + str(input_num))

if __name__ == "__main__":
    root = Tk()
    root.configure(background="white")
    root.title("Prime Number Checker")
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
