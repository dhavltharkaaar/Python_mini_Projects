from tkinter import *
import math

def show():
    try:
        height = float(e1.get())
        weight = float(e2.get())
        bmi = weight / (height ** 2)
        result_label.config(text="Your calculated BMI is: {:.2f}".format(bmi))
        if 18.5 < bmi < 24.9:
            result.config(text="You are a healthy person")
        elif bmi >= 25.0:
            result.config(text="You are an overweight person! Take proper diet and exercise.")
        else:
            result.config(text="You are an unhealthy or extremely thin person! Gain some more weight")
    except ValueError:
        result_label.config(text="Invalid input. Please enter valid numerical values.")

if __name__ == "__main__":
    root = Tk()
    root.configure(background="white")
    root.title("BMI Calculator")
    root.geometry("450x250")
    root.resizable(False, False)

    l1 = Label(root, text="Enter Height in m:")
    l1.place(x=20, y=30)

    e1 = Entry(root)
    e1.place(x=130, y=30)

    l2 = Label(root, text="Enter Weight in KG:")
    l2.place(x=20, y=60)

    e2 = Entry(root)
    e2.place(x=130, y=60)

    bt = Button(root, text="Submit", command=show)
    bt.place(x=100, y=90)

    result_label = Label(root, text="")
    result_label.place(x=20, y=120)

    result = Label(root, text="")
    result.place(x=20, y=150)

    root.mainloop()
