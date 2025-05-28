from tkinter import *
from tkinter import ttk

def show():
    result_label.config(text="")
    try:
        weight = float(e1.get())
    except ValueError:
        result_label.config(text="Invalid input. Please enter a valid numeric value.")
        return

    choice = cb.get()
    conversion_factors = {
        'Gram': 1000,
        'Milligram': 1000000,
        'US ton': 1 / 907.2,
        'Stone': 1 / 6.35,
        'Pound': 2.205,
        'Ounce': 35.274
    }

    if choice in conversion_factors:
        w = weight * conversion_factors[choice]
        result_label.config(text="Weight conversion is: {:.4f} {}".format(w, choice))
    else:
        result_label.config(text="Invalid choice. Please select a valid unit.")

if __name__ == "__main__":
    root = Tk()
    root.configure(background="white")
    root.title("Weight Converter")
    root.geometry("450x200")
    root.resizable(False, False)
    
    hd = Label(root, text="Weight Conversion")
    hd.place(x=130, y=5)

    l1 = Label(root, text="Enter Weight in Kilogram : ")
    l1.place(x=20, y=30)

    e1 = Entry(root)
    e1.place(x=200, y=30)

    l2 = Label(root, text="Select your Choice")
    l2.place(x=20, y=70)

    cb = ttk.Combobox(root, values=['Gram', 'Milligram', 'US ton', 'Pound', 'Stone', 'Ounce'], height=10, width=20)
    cb.place(x=200, y=70)

    bt = Button(root, text="Submit", command=show)
    bt.place(x=80, y=100)

    result_label = Label(root, text="")
    result_label.place(x=20, y=130)

    root.mainloop()
