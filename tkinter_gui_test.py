import tkinter
from tkinter import messagebox


def ShowPopUp():
    msg = messagebox.showinfo("Test title", "My unique message")


window = tkinter.Tk()
buttonWidget = tkinter.Button(window, text="Click me", command=ShowPopUp)
buttonWidget.place(x=25, y=100)
window.mainloop()
