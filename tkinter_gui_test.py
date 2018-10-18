import tkinter
from tkinter import *
from tkinter import messagebox

window = tkinter.Tk()


def showMessage():
    messagebox.showinfo("Title", "Message")


btn = Button(window, text="Click me", command=showMessage)
btn.pack()

window.mainloop()
