import tkinter
from tkinter import ttk

win = tkinter.Tk()
win.geometry('800x400+300+100')

tree = ttk.Treeview(win)
tree.pack()

#定义列  是个元组
tree['column'] = ('name','age','height','weight')
# 设置列  即设置每列有间距
tree.column('name',width=100)
tree.column('age',width=100)
tree.column('height',width=100)
tree.column('weight',width=100)

# 设置表头信息
tree.heading('name',text='name')
tree.heading('age',text='age')
tree.heading('height',text='height')
tree.heading('weight',text='weight')

# 插入数据
tree.insert('',0,text='line1',values=('tom',21,167,122))
tree.insert('',1,text='line2',values=('nick',18,187,112))
tree.insert('',3,text='line3',values=('tina',101,171,131))

win.mainloop()