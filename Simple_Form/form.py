from tkinter import *
from tkinter import ttk
w=Tk()
def display():
          s1=e1.get()
          print("Your Name is ",s1)
          l8=Label(w,text="Your Name is "+s1)
          l8.place(x=50,y=320)
          s2=e2.get()
          print("Your Address is ",s2)
          l9=Label(w,text="Your Address is "+s2)
          l9.place(x=50,y=340)
          s3=v.get()
          if s3==1:
                    print("You are Male")
                    l10=Label(w,text="Your Gender is Male")
                    l10.place(x=50,y=360)
             
          if s3==2:
                    print("You are Female")
                    l10=Label(w,text="Your Gender is Female")
                    l10.place(x=50,y=360)

          s4=v1.get()
          s5=v2.get()
          s6=v3.get()
          if s4==1:
                    print("Your Favourite Game is Cricket")
                    l11=Label(w,text="Your Favourite Game is Cricket ")
                    l11.place(x=50,y=380)

          if s5==1:
                    print("Your Favourite Game is Football")
                    l11=Label(w,text="Your Favourite Game is Football " )
                    l11.place(x=50,y=380)

          if s6==1:
                    print("Your Favourite Game is Tennis")
                    l11=Label(w,text="Your Favourite Game is Tennis ")
                    l11.place(x=50,y=380)
          s7=sb.get()
          print("Your Favourite Food is ",s7)
          l12=Label(w,text="Your Favourite Food is "+s7)
          l12.place(x=50,y=400)

          s12=lb.get(ACTIVE)
          if lb.get(ACTIVE):
              l21=Label(w,text="your favourite language is : " +s12)
              l21.place(x=50,y=420)
          

          s8=cb.get()
          print("Your Favourite Movie is ",s8)
          l14=Label(w,text="Your Favourite Movie is "+s8)
          l14.place(x=50,y=440)

l1=Label(w,text="Enter your Name")
l1.place(x=20,y=30)
e1=Entry(w)
e1.place(x=130,y=30)
l2=Label(w,text="Enter your Address")
l2.place(x=20,y=60)
e2=Entry(w)
e2.place(x=130,y=60)
l3=Label(w,text="Select your gender")
l3.place(x=20,y=90)

v=IntVar()
r1=Radiobutton(w,text="Male",variable=v, value =1)
r2=Radiobutton(w,text="Female",variable=v, value =2)
r1.place(x=130,y=90)
r2.place(x=190,y=90)

l4=Label(w,text="Select your favourite sport")
l4.place(x=20,y=120)
v1=IntVar()
v2=IntVar()
v3=IntVar()
c1=Checkbutton(w,text="Cricket",variable=v1)
c2=Checkbutton(w,text="Football",variable=v2)
c3=Checkbutton(w,text="Tennis",variable=v3)
c1.place(x=135,y=120)
c2.place(x=200,y=120)
c3.place(x=280,y=120)
l6=Label(w,text="Select your Favourite Food")
l6.place(x=20,y=150)
sb=Spinbox(w,value=['Chinese','Indian','Continental','Italian'])
sb.place(x=200,y=150)
l5=Label(w,text="Select your Favourite Language")
l5.place(x=20,y=180)
lb=Listbox(w,height=2,width=20,selectmode='SINGLE')
lb.insert(0,'Python')
lb.insert(1,'Java')
lb.insert(2,'C++')
lb.insert(3,'C')
lb.place(x=200,y=180)
l7=Label(w,text="Select your Favourite Movie")
l7.place(x=20,y=230)
cb=ttk.Combobox(w,values=['Avengers','Harry Potter','Home Alone','3 Idiots'],height=10,width=20)
cb.place(x=200,y=230)
bt=Button(w,text="Submit",command=display)
bt.place(x=150,y=270)

w.mainloop()
