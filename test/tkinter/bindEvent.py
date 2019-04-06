import tkinter

win = tkinter.Tk()
win.geometry('400x200+300+100')

def locate(event):
    print(event.x,event.y)
def update(event):
    print('event.char=',event.char)
    print('event.keycode',event.keycode)

label1 = tkinter.Label(win,text='Today')
# 绝对定位
# label1.place(x=100,y=100)
label1.pack()
label1.bind('<Button-1>',locate)

label2 = tkinter.Label(win,text='NextDay')
# 设置焦点
label2.focus_set()
label2.pack()
# label2.bind('<Key>',update)
label2.bind('<Shift_L>',update)

label3 = tkinter.Label(win,text='Three')
label3.pack()
label3.bind('<Enter>',locate)

label4 = tkinter.Label(win,text='Four')
label4.pack()
label4.bind('<ButtonReleased-1>',locate)
win.mainloop()
