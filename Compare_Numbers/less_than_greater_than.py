from tkinter import *
from tkinter import ttk

def show():
    first = int(e1.get())
    second = int(e2.get())
    
    if first > second:
        result_label.config(text="First Number is Greater: " + str(first))
    else:
        result_label.config(text="Second Number is Greater: " + str(second))

if __name__ == "__main__":
    root = Tk()
    root.configure(background="white")
    root.title("Number Comparison Application")
    root.geometry("350x200")
    root.resizable(False, False)
    
    l1 = Label(root, text="Enter First Number")
    l1.place(x=20, y=30)
    e1 = Entry(root)
    e1.place(x=130, y=30)

    l2 = Label(root, text="Enter Second Number")
    l2.place(x=20, y=60)
    e2 = Entry(root)
    e2.place(x=130, y=60)

    bt = Button(root, text="Submit", command=show)
    bt.place(x=100, y=150)

    result_label = Label(root, text="")
    result_label.place(x=20, y=90)

    root.mainloop()
