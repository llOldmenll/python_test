import tkinter
from tkinter import *

window = tkinter.Tk()

scrollBar = Scrollbar(window)
scrollBar.pack(side=RIGHT, fill=Y)

list = Listbox(window, yscrollcommand=scrollBar.set)
for line in range(1000):
    list.insert(END, "Row: " + str(line + 1))
list.pack()

scrollBar.config(command=list.yview)

window.mainloop()
