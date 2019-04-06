import tkinter
from tkinter import ttk
import os

class treeWindows(tkinter.Frame):
    # 所有实现都在__init__方法里实现
    def __init__(self,master,path,otherWin):
        # 创建一个框架
        frame = tkinter.Frame(master)
        # frame.pack(side=tkinter.RIGHT,fill=tkinter.Y)
        frame.grid(row=0, column=0)
        # otherWin
        self.otherWin = otherWin

        # 创建一个树状图
        self.tree = ttk.Treeview(master)
        self.tree.grid(row=0,column=0)

        # 树状图里添加目录
        root = self.tree.insert("",'end',text=treeWindows.getLastPath(path),open=True)

        #添加子树枝  需要遍历的父亲节点，以及遍历的目录
        self.loadTree(root,path)

        # 加个滚动条
        self.sy = tkinter.Scrollbar(frame)
        # 和树状图进行关联
        self.sy.config(command=self.tree.yview)
        self.tree.config(yscrollcommand=self.sy.set)
        self.sy.pack(side=tkinter.RIGHT,fill=tkinter.Y)
        # self.sy.grid(row=0, column=0, sticky='NS')

        # 绑定事件
        self.tree.bind("<<TreeviewSelect>>",self.update)

    def getLastPath(path):  # 这里不用self的原因是没有那种实例进行对它进行调用
        pathList = os.path.split(path)
        return pathList[-1]

    def loadTree(self,parent,parentPath):
        for fileName in os.listdir(parentPath):
            absPath = os.path.join(parentPath,fileName)
            # 插入到子树枝
            childTree = self.tree.insert(parent,'end',text=treeWindows.getLastPath(absPath))
            if os.path.isdir(absPath):
                self.loadTree(childTree,absPath)

    def update(self,event):
        self.v = event.widget.selection()
        for sv in self.v:
            file = self.tree.item(sv)['text']
            self.otherWin.ev.set(file)
            print(file)
        print('xxxxxxx')