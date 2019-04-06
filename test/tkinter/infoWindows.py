import tkinter
import os
from tkinter import ttk

class infoWindows(tkinter.Frame):
    def __init__(self,master):
        frame = tkinter.Frame(master)
        frame.grid(row=0,column=1)
        # frame.pack()

        self.ev = tkinter.Variable()
        self.entry = tkinter.Entry(frame,textvariable=self.ev)
        self.entry.pack()

        self.txt = tkinter.Text(frame   )
        self.txt.pack()