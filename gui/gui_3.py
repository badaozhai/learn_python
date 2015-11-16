__author__ = 'Administrator'

from tkinter import *


def helloBt():
    print('123')


root = Tk()
root.title('拔刀斋')
Button(root, text="点我", command=helloBt).pack()
Button(root,text = 'hello button',relief=FLAT).pack()
Button(root,text = 'hello button',relief=GROOVE).pack()
Button(root,text = 'hello button',relief=RAISED).pack()
Button(root,text = 'hello button',relief=RIDGE).pack()
Button(root,text = 'hello button',relief=SOLID).pack()
Button(root,text = 'hello button',relief=SUNKEN).pack()
root.mainloop()
