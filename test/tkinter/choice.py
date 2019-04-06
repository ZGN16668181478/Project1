import tkinter

win = tkinter.Tk()
win.geometry('300x200+400+100')

def CheckButton():
    message = ''
    if hobby1.get():
        message += 'money\n'
        print('money')
    if hobby2.get():
        message += 'power\n'
        print('power')
    if hobby3.get():
        message += 'women\n'
        print('women')
    print(message)
    # 这里0.0是下标为0的第0行，到最后一行。即从开始到最后都清除，然后在进行添加
    text.delete(0.0,tkinter.END)
    text.insert(tkinter.INSERT,message)
# 复选框
hobby1 = tkinter.BooleanVar()
btn1 = tkinter.Checkbutton(win,text='money',variable=hobby1,command=CheckButton)
btn1.pack()
hobby2 = tkinter.BooleanVar()
btn2 = tkinter.Checkbutton(win,text='power',variable=hobby2,command=CheckButton)
btn2.pack()
hobby3 = tkinter.BooleanVar()
btn3 = tkinter.Checkbutton(win,text='women',variable=hobby3,command=CheckButton)
btn3.pack()
text = tkinter.Text(win,width=100,height=5)
text.pack()
win.mainloop()