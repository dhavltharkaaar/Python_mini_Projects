from tkinter import *
import random

current_player =1

def rnd():
    global current_player
    roll = random.randint(1, 6)
    if current_player == 1:
        current_player = 2
        lb1.config(text="Player 2's Turn")
    else:
        current_player = 1
        lb1.config(text="Player 1's Turn")
    lb.config(text=f"Player {current_player} rolled a {roll}")

def exit():
    root.destroy()



if __name__ == "__main__":
	root = Tk()
	root.configure(background="White")
	root.title("Dice Roll")
	root.geometry("250x250")
	root.resizable(False,False)
	lb1 = Label(root, text = " ")
	lb1.pack()
	player = Button(root, height=1, width =10, text="Roll the Dice", command = rnd)
	player.pack()
	lb = Label(root, text = " ")
	lb.pack()
	exit = Button(root, height=1, width =10, text="Exit", command = exit)
	exit.pack()
	root.mainloop()
