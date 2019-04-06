import tkinter

win = tkinter.Tk()
win.geometry('400x400+500+100')

# lb = tkinter.Listbox(win, selectmode=tkinter.BROWSE)
lb = tkinter.Listbox(win, selectmode=tkinter.SINGLE)
lb.pack()
# listbox进行添加
for item in ['jackylove','uzi','theshy','shit']:
    lb.insert(tkinter.END,item)
# 想要获取每个列表的值，需要给listbox绑定一个函数
def myPrint(event):
    print(lb.get(lb.curselection()))
lb.bind('<Alt-Button-1>',myPrint)
# 删除
lb.delete(1)
# 选中
lb.select_set(2)
# 取消选中
lb.select_clear(2)
print(lb.size())
# 取值
print(lb.get(2))
# 是否选中
print(lb.select_includes(2))
win.mainloop()