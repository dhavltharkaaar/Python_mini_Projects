from tkinter import *
import math

def show():
    num = int(e1.get())
    fib_series = [0, 1]

    for i in range(2, num):
        fib_series.append(fib_series[i-1] + fib_series[i-2])

    result_label.config(text=f"Fibonacci series of {num} is: {fib_series}")

if __name__ == "__main__":
    root = Tk()
    root.configure(background="white")
    root.title("Fibonacci Calculator")
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
