import win32con
import win32api
import win32gui
import pygame
import time

def loadMusic():
    pygame.mixer.init()
    path = r'C:\Users\Asus\Desktop\新建文件夹\test'
    while True:
        for num in range(3):
            filePath = path + '\\' +str(num)+ '.mp3'
            print(filePath)
            pygame.mixer.music.load(filePath)
            pygame.mixer.music.play()
            time.sleep(10)
            pygame.mixer.music.stop()

def setWallPaper(path):
    reg_key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,'Control Panel\\Desktop',0,win32con.KEY_SET_VALUE)
    win32api.RegSetValueEx(reg_key,'WallPaperStyle',0,win32con.REG_SZ,'6')
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER,path,win32con.SPIF_SENDWININICHANGE)

def getLastName(path):
    import os,re
    list = []
    listPath = os.listdir(path)
    for end in listPath:
        if not end.__contains__('mp3'):
            list.append(end)
    # with open(path,'r') as f:
    #     list = os.listdir(f)
    return list

path = r'C:\Users\Asus\Desktop\新建文件夹\test'
print(getLastName(path))
import threading
music = threading.Thread(target=loadMusic,name='LoopThread')
music.start()
while True:
    for num in range(8):
        filePath = path + '\\'+str(getLastName(path)[num])
        print(filePath)
        setWallPaper(filePath)
        time.sleep(1)
