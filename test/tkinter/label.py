import tkinter

win = tkinter.Tk()
win.title('oh shit mother fucker')
win.geometry('400x400+500-200')

# 标签控件可以控制文本
label = tkinter.Label(win,text='黎婧怡,我要是早知道，我肯定怎样都要留住你',bg='blue',fg='green',font=('宋体',20),height=4,width=20,
                      wraplength=200,justify='right',anchor='center')
label.pack()
tkinter.mainloop()
