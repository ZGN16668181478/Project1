import tkinter
from tkinter import ttk


win = tkinter.Tk()
win.geometry('400x400+500+100')

v = tkinter.StringVar()
com = ttk.Combobox(win,textvariable=v)
com.pack()

# 设置下拉数据
com['value'] = ('oh','shit','mother','fucker','damn it')
# 设置默认
com.current(1)

def update(event):
    print('v: ',v.get())
    print('get: ',com.get())
# 绑定事件
com.bind('<<ComboboxSelected>>',update)
win.mainloop()