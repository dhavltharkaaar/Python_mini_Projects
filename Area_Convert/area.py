from tkinter import *
from tkinter import ttk

def show():
    result_label.config(text="")
    try:
        area = float(e1.get())
    except ValueError:
        result_label.config(text="Invalid input. Please enter a valid numeric value.")
        return

    choice = cb.get()
    conversion_factors = {
        'Square Meter': 1/10.764,
        'Square Kilometer': 1/10760000,
        'Square Mile': 1 / 27880000,
        'Square Yard': 1 / 9,
        'Square Inch': 144,
        'Acre': 1/43560
    }

    if choice in conversion_factors:
        a = area * conversion_factors[choice]
        result_label.config(text="Area conversion is: {:.8f} {}".format(a, choice))
    else:
        result_label.config(text="Invalid choice. Please select a valid unit.")

if __name__ == "__main__":
    root = Tk()
    root.configure(background="white")
    root.title("Area Converter")
    root.geometry("450x200")
    root.resizable(False, False)
    
    hd = Label(root, text="Area Conversion")
    hd.place(x=130, y=5)

    l1 = Label(root, text="Enter Area in Square Foot : ")
    l1.place(x=20, y=30)

    e1 = Entry(root)
    e1.place(x=200, y=30)

    l2 = Label(root, text="Select your Choice")
    l2.place(x=20, y=70)

    cb = ttk.Combobox(root, values=['Square Meter', 'Square Kilometer', 'Square Mile', 'Square Yard', 'Square Inch', 'Acre'], height=10, width=20)
    cb.place(x=200, y=70)

    bt = Button(root, text="Submit", command=show)
    bt.place(x=80, y=100)

    result_label = Label(root, text="")
    result_label.place(x=20, y=130)

    root.mainloop()
