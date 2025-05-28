from tkinter import *
from tkinter import ttk

def show():
    input = int(e1.get())
    
    if (input % 2) ==0:
        result_label.config(text= "Given Number is an Even Number : " + str(input))
    else:
        result_label.config(text="Given Number is an odd Number : " + str(input))

if __name__ == "__main__":
    root = Tk()
    root.configure(background="white")
    root.title("Even and Odd Number")
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
