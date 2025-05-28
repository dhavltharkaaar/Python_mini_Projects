from tkinter import *
import math

def show():
    year = int(e1.get())
    if (year % 400 == 0) and (year % 100 == 0):
        result_label.config(text=f"Year of "+ str(year) + " is a Leap Year")
    elif (year % 4 ==0) and (year % 100 != 0):
        result_label.config(text=f"Year of "+ str(year) + " is a Leap Year")
    else:
        result_label.config(text=f"Year of "+ str(year) + " is not a Leap Year")
    

if __name__ == "__main__":
    root = Tk()
    root.configure(background="white")
    root.title("Leap Year Calculator")
    root.geometry("350x200")
    root.resizable(False, False)

    l1 = Label(root, text="Enter Year")
    l1.place(x=20, y=30)

    e1 = Entry(root)
    e1.place(x=130, y=30)

    bt = Button(root, text="Submit", command=show)
    bt.place(x=100, y=60)

    result_label = Label(root, text="")
    result_label.place(x=20, y=90)  

    root.mainloop()
