__author__ = 'Administrator'
from tkinter import *


def cb1():
    print('111')


def cb2(event):
    print('222')


def cb3():
    print('333')


root = Tk()
b1 = Button(root, text='bt1', command=cb1)
b2 = Button(root, text='bt2', )
# b2.bind('<Return>', cb2) # Return == 回车
b2.bind('<Enter>', cb2)     #Enter == 鼠标mouseover 鼠标移上去
b3 = Button(root, text='bt3', command=cb3)
b1.pack()
b2.pack()
b3.pack()
b2.focus_set()
root.mainloop()

