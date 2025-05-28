from tkinter import *
from tkinter import ttk

def show():
    height = float(e1.get())
    choice = cb.get()
    h = 0

    if choice == 'Centimeter':
        h = height * 100
    elif choice == 'Kilometer':
        h = height / 1000
    elif choice == 'Miles':
        h = height / 1609
    elif choice == 'Foot':
        h = height * 3.281
    elif choice == 'Inch':
        h = height * 39.37
    else:
        result_label.config(text="Invalid Input")
        return

    result_label.config(text="Height conversion is: {:.4f} {}".format(h, choice))

if __name__ == "__main__":
    root = Tk()
    root.configure(background="white")
    root.title("Height Converter")
    root.geometry("450x200")
    root.resizable(False, False)
    
    hd = Label(root, text="Height Conversion")
    hd.place(x=130, y=5)

    l1 = Label(root, text="Enter Height in Meter : ")
    l1.place(x=20, y=30)

    e1 = Entry(root)
    e1.place(x=200, y=30)

    l2 = Label(root, text="Select your Choice")
    l2.place(x=20, y=70)

    cb = ttk.Combobox(root, values=['Centimeter', 'Kilometer', 'Miles', 'Foot', 'Inch'], height=10, width=20)
    cb.place(x=200, y=70)

    bt = Button(root, text="Submit", command=show)
    bt.place(x=80, y=100)

    result_label = Label(root, text="")
    result_label.place(x=20, y=130)

    root.mainloop()
