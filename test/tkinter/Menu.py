import tkinter

win = tkinter.Tk()
win.geometry('400x400+500+100')

# 创建菜单条
menubar = tkinter.Menu(win)
win.config(menu=menubar)

def update():
    print('xxxxxx')
# 创建menubar,不能pack
menu1 = tkinter.Menu(menubar,tearoff=False)
list = ['Python','C','JQuery','JS','OC','Java','PHP','NodeJS','AngularJS','Shell','退出']
for item in list:
    if item == '退出':
        # 加个分割线
        menu1.add_separator()
        menu1.add_command(label=item,command=win.quit)
    else:
        menu1.add_command(label=item,command=update)

# 给主菜单添加菜单选项
menubar.add_cascade(label='语言',menu=menu1)

# 再加个颜色选项
color = tkinter.Menu(menubar,tearoff=False)
color.add_command(label='red',command=update)
color.add_command(label='green',command=update)
menubar.add_cascade(label='颜色',menu=color)

# 鼠标右键再加一个菜单选项

menubar2 = tkinter.Menu(win)
# win.config(menu=menubar2)

menu2 = tkinter.Menu(menubar2,tearoff=False)
list2 = ['语文','数学','英语','物理','生物','化学','政治','地理','历史']
for item in list2:
    menu2.add_command(label=item,command=update)
menubar2.add_cascade(label='科目',menu=menu2)

def showData(event):
    menubar2.post(event.x_root,event.y_root)
win.bind("<Button-3>",showData)
win.mainloop()