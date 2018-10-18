import tkinter
from tkinter import *


def getValue():
    value = "Value: " + str(var.get())
    label.config(text=value)


window = tkinter.Tk()

var = DoubleVar()
scale = Scale(window, variable=var)
scale.pack()

btn = Button(window, text="Receive value", command=getValue)
btn.pack()

label = Label(window)
label.pack()

window.mainloop()
