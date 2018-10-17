import tkinter
from tkinter import *

window = tkinter.Tk()

cv = IntVar()
cb = Checkbutton(window, text="Click Me", variable=cv, onvalue=1, offvalue=0, height=30, width=20, bg="purple")
cb.pack()

window.mainloop()
