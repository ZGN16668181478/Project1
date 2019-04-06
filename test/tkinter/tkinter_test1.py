import tkinter
from tkinter import ttk

win = tkinter.Tk()
win.title('PyCharm')
win.geometry('500x400+200+100')

# 创建上菜单
menubar = tkinter.Menu(win)
# 需要把menubar在win里进行配置,不进行配置不会在win里显示
win.config(menu=menubar)
menuList = ['File','Edit','Navigate','Code','Refactor','Run','Tool','VCS','Window','Help']

def update(event):
    print('xxxxxxx')
list_file = ['new','open','save','setting','import','export','exit']
list_edit = ['undo','paste','delete','copy','cut','find']
list_navigate = []
list_help = ['oh','shit','mother','fucker','辣鸡','滚吧']
# menuList添加到menubar作为每个menu的Label
for item in menuList:
    print(item)
    t = tkinter.Menu(menubar,tearoff=False)
    menubar.add_cascade(label=item,menu=t)
    if item=='File':
        for l_file in list_file:
            if l_file=='exit':
                t.add_separator()
                t.add_command(label=l_file,command=t.quit)
            else:
                t.add_command(label=l_file)
    if item=='Edit':
        for l_file in list_edit:
            t.add_command(label=l_file)
    if item=='Help':
        for l_file in list_help:
            t.add_command(label=l_file)
    print(t.info)
win.mainloop()