__author__ = 'Administrator'
from tkinter import *
root = Tk()
def changeText():
    if b['text'] == 'text':
        v.set('change')
    else:
        v.set('text')
v = StringVar()
b = Button(root,textvariable = v,command = changeText)
v.set('text')
b.pack()
root.mainloop()