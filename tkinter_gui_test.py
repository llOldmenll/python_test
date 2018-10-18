import tkinter
from tkinter import *

window = tkinter.Tk()


labelFrame = LabelFrame(window, text="It's LABEL!!!")
labelFrame.pack(fill=BOTH, expand="yes")

left = Label(labelFrame, text="Inside label!!!!")
left.pack()

window.mainloop()
