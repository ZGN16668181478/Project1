import tkinter
from tkinter import ttk

win = tkinter.Tk()
win.geometry('800x400+300+100')

# 定义图
tree = ttk.Treeview(win)
tree.pack()

# 添加一级树枝
treeF1 = tree.insert('',0,'China',text='China',values=('F1'))
treeF2 = tree.insert('',1,'USA',text='USA',values=('F2'))
treeF3 = tree.insert('',2,'UK',text='UK',values=('F3'))
# 添加二级树枝
treeF1_1 = tree.insert(treeF1,0,text='长沙')
treeF1_2 = tree.insert(treeF1,1,text='郑州')
treeF1_3 = tree.insert(treeF1,2,text='上海')
treeF1_4 = tree.insert(treeF1,3,text='厦门')
# 添加三级树枝
treeF1_1_1 = tree.insert(treeF1_1,0,text='湘阴')
treeF1_1_2 = tree.insert(treeF1_1,1,text='杨林寨')
treeF1_1_3 = tree.insert(treeF1_1,2,text='南湖')
treeF1_1_4 = tree.insert(treeF1_1,3,text='新泉')
win.mainloop()