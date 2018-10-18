import tkinter
from tkinter import *

window = tkinter.Tk()

m1 = PanedWindow(window)
m1.pack(fill=BOTH, expand=1)

left = Entry(m1, bd=5)
m1.add(left)

m2 = PanedWindow(m1, orient=VERTICAL)
m1.add(m2)

top = Scale(m2, orient=HORIZONTAL)
m2.add(top)

btn = Button(m2, text="Click me")
m2.add(btn)

window.mainloop()
