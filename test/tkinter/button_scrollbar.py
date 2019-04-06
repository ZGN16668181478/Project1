import tkinter

win = tkinter.Tk()
win.geometry("400x250+400+100")
win.title('这是黎婧怡')
# 添加Label控件
label = tkinter.Label(win,text='黎婧怡',fg='green',font=('宋体',20))
label.pack()
# 添加Entry控件,绑定变量并给变量添加进去

e = tkinter.Variable()
entry = tkinter.Entry(win,textvariable=e)
entry.pack()
e.set('黎婧怡是个好女孩！')
print(e.get(),entry.get())
# 添加Button控件,点击进行控件

def showConfirm():
    print(entry.get())
def showNotConfirm():
    win2 = tkinter.Tk()
    win2.geometry("200x40+510+200")
    label2=tkinter.Label(win2,text='吃屎吧你',fg='red',font=('宋体',20))
    label2.pack()
button = tkinter.Button(win,text='那绝对是',command=showConfirm)
button2 = tkinter.Button(win,text='好像不是',command=showNotConfirm)
button.pack()
button2.pack()

# 多行文本控件Text

label3 = tkinter.Label(win,text='关于黎婧怡',anchor='ne')
label3.pack()
scroll = tkinter.Scrollbar()
text = tkinter.Text(win,width=100,height=4)
str = '''While The Python Language Reference describes the exact syntax and semantics of the Python language, this library reference manual describes the standard library that is distributed with Python. It also describes some of the optional components that are commonly included in Python distributions.
Python’s standard library is very extensive, offering a wide range of facilities as indicated by the long table of contents listed below. The library contains built-in modules (written in C) that provide access to system functionality such as file I/O that would otherwise be inaccessible to Python programmers, as well as modules written in Python that provide standardized solutions for many problems that occur in everyday programming. Some of these modules are explicitly designed to encourage and enhance the portability of Python programs by abstracting away platform-specifics into platform-neutral APIs.'''
text.insert(tkinter.INSERT,str)

scroll.pack(side=tkinter.RIGHT,fill=tkinter.Y)
text.pack(side=tkinter.LEFT,fill=tkinter.Y)
# 关联个进度条
scroll.config(command=text.yview)
text.config(yscrollcommand=scroll.set)
win.mainloop()