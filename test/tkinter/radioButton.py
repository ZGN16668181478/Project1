import tkinter

win = tkinter.Tk()
win.geometry('400x400+500+100')

def update():
    # 这里是因为上面有创建了变量r，才能这样进行调用
    print(r.get())

r = tkinter.IntVar()
# 这里绑定不绑定都可以进行显示单选，绑定变量是为了让绑定函数进行正常显示
rb1 = tkinter.Radiobutton(win,text='money',value=1,variable=r,command=update)
rb1.pack()
rb2 = tkinter.Radiobutton(win,text='power',value=2,variable=r,command=update)
rb2.pack()





win.mainloop()