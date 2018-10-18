import tkinter
from tkinter import *

window = tkinter.Tk()

str = StringVar()
str.set("The huge message ever ever ever ever...")
msg = Message(window, textvariable=str)
msg.pack()

window.mainloop()
