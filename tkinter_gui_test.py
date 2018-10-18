import tkinter
from tkinter import *

window = tkinter.Tk()

spin = Spinbox(window, from_=0, to=10)
spin.pack()

window.mainloop()
