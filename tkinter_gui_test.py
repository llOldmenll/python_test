import tkinter
from tkinter import *

window = tkinter.Tk()

menubar = Menu(window)

menu1 = Menu(menubar)
menu1.add_command(label="New")
menu1.add_separator()
menu1.add_command(label="Exit", command=window.quit())
menubar.add_cascade(label="Section1", menu=menu1)

menu2 = Menu(menubar)
menu2.add_command(label="Add")
menubar.add_cascade(label="Section2", menu=menu2)

window.config(menu=menubar)
window.mainloop()
