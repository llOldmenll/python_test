import tkinter
from tkinter import *

window = tkinter.Tk()

str = StringVar()
label = Label(window, textvariable=str)
str.set("Amazing test Label")
label.pack()

frame = Frame(window)
frame.pack()

buttonWidget = tkinter.Button(window, text="Click me")
buttonWidget.pack(side=LEFT)

cv = IntVar()
cb = Checkbutton(window, text="Click Me", variable=cv, onvalue=1, offvalue=0, height=30, width=20, bg="purple")
cb.pack()

list = Listbox(window)
list.insert(0, "Item 0")
list.insert(1, "Item 1")
list.insert(2, "Item 2")
list.insert(3, "Item 3")
list.insert(4, "Item 4")
list.insert(5, "Item 5")
list.pack()

window.mainloop()
