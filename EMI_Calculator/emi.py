from tkinter import *
from tkinter import ttk

def show():
    P = float(e1.get())
    ir = float(e2.get())
    y = float(e3.get())
    R = (ir/(12*100)) # Monthly Interest Rste
    N = y*12 # Loan Tenure in Months
    a = ((1+R)**N)
    b =(((1+R)**N)-1)
    emi = ((P*R)*a/b) # monthly emi
    yr = emi*12 # yearly
    result_label.config(text="Your Monthly EMI is: {:.2f}".format(emi))
    Yearly.config(text="Your Yearly EMI is: {:.2f}".format(yr))
    
 
if __name__ == "__main__":
    root = Tk()
    root.configure(background="white")
    root.title("EMI Calculator")
    root.geometry("450x350")
    root.resizable(False, False)
    
    hd = Label(root, text="EMI Calculator")
    hd.place(x=130, y=5)

    l1 = Label(root, text="Enter Loan Amount : ")
    l1.place(x=20, y=30)

    e1 = Entry(root)
    e1.place(x=200, y=30)


    l2 = Label(root, text="Enter Interest Rate : ")
    l2.place(x=20, y=70)

    e2 = Entry(root)
    e2.place(x=200, y=70)

    l3 = Label(root, text="Enter the Duation in Years : ")
    l3.place(x=20, y=110)

    e3 = Entry(root)
    e3.place(x=200, y= 110)

    bt = Button(root, text="Submit", command=show)
    bt.place(x=80, y=150)

    result_label = Label(root, text="")
    result_label.place(x=20, y=190)

    Yearly = Label(root, text="")
    Yearly.place(x=20, y=240)

    root.mainloop()
