import tkinter


win = tkinter.Tk()
win.geometry('400x400+500+100')
# scale从哪到哪，tickinterval是每段间隔，orient是分布方式，length：垂直就是高度,水平就是宽度
scale = tkinter.Scale(win,from_=0,to=100,tickinterval=10,orient=tkinter.HORIZONTAL,length=200)
scale.pack()

def onclick():
    print(scale.get())

btn = tkinter.Button(win,text='button',command=onclick)
btn.pack()
win.mainloop()