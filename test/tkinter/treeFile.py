import tkinter
from tkinter import ttk
import os
from treeWindows import treeWindows
from infoWindows import infoWindows

win = tkinter.Tk()
win.geometry('600x400+200+50')
# path = r'D:\learn\Python\千锋python基础教程：第一章 python语言基础'
path = r'D:\learn'

'''想要点击treewin中tree获取数据到infoWin中，直接将infoWin传到treewin中，然后把treewin中
数据放到infoWin中Entry中就可以了'''

# infoWindows
infoWin = infoWindows(win)
# 树形文件列表
treewin = treeWindows(win,path,infoWin)
win.mainloop()