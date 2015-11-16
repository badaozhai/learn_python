__author__ = 'Administrator'
import tkinter

top = tkinter.Tk()
label = tkinter.Label(top,text='hello1')
label.pack()
# bitmap使用内置位图error
label = tkinter.Label(top, bitmap='error')
label.pack()
tkinter.mainloop()


from tkinter import *
root = Tk()
#创建三个Label，分别显示red,blue,yellow
#注意三个Label的大小，它们均与文本的长度有关
Label(root,text = 'red',bg = 'red').pack()
Label(root,text = 'blue',bg = 'blue').pack()
Label(root,text = 'yellow',bg = 'yellow').pack()

#再创建三个Label，与上次不同的是这三个Label均使用width和heigth属性
#三个Label的大小由width和height指定
Label(root,bg = 'red',width = 10,height = 3).pack()
Label(root,bg = 'blue',width = 10,height = 3).pack()
Label(root,bg = 'yellow',width = 10,height = 3).pack()
root.mainloop()