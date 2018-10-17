import tkinter
from tkinter import *

window = tkinter.Tk()

frame = Frame(window)
frame.pack()

buttonWidget = tkinter.Button(window, text="Click me")
buttonWidget.pack(side=LEFT)

cv = IntVar()
cb = Checkbutton(window, text="Click Me", variable=cv, onvalue=1, offvalue=0, height=30, width=20, bg="purple")
cb.pack()

window.mainloop()
