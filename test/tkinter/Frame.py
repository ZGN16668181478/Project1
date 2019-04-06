import tkinter

win = tkinter.Tk()
win.geometry('400x400+500+100')

frame = tkinter.Frame(win)
frame.pack()
frame_l = tkinter.Frame(frame)
tkinter.Label(frame_l,text='左上',bg='green').pack(side=tkinter.TOP)
tkinter.Label(frame_l,text='左下',bg='red').pack(side=tkinter.TOP)
frame_l.pack(side=tkinter.LEFT)
frame_r = tkinter.Frame(frame)
tkinter.Label(frame_r,text='右上',bg='blue').pack(side=tkinter.TOP)
tkinter.Label(frame_r,text='右上',bg='pink').pack(side=tkinter.TOP)
frame_r.pack(side=tkinter.RIGHT)

win.mainloop()