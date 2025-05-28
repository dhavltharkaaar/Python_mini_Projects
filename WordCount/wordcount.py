from tkinter import *

def count():
    text = textBox.get("1.0", "end-1c")
    split = len(text.split())
    content.set(f"Word count: {split}")

if __name__ == "__main__":
    root = Tk()
    root.configure(background="white")
    root.title("Word Count Application")
    root.geometry("450x650")
    root.resizable(False, False)

    textBox = Text(root, height=30, width=50)
    textBox.pack()

    save = Button(root, height=2, width=10, text="Count", command=count)
    save.pack()

    content = StringVar()
    lb = Label(root, textvariable=content)
    lb.pack()

    root.mainloop()
