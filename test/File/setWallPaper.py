import win32api
import win32gui
import win32con

# 从注册表中user中WallPaper进行修改桌面背景的属性
def setWallPaper(path):
    # 打开注册表
    reg_key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,"Control Panel\\Desktop",0,win32con.KEY_SET_VALUE)

    # 设置背景属性 2拉伸  0居中 6适应  10填充
    win32api.RegSetValueEx(reg_key,'WallPaperStyle',0,win32con.REG_SZ,'6')

    #设置墙纸   SPIF_SENDWININICHANGE设置立即生效
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER,path,win32con.SPIF_SENDWININICHANGE)

    print('It\'s OK')
path = r'C:\Users\Asus\Pictures\Saved Pictures\这人\1464130047194_ep_slim.jpeg'
setWallPaper(path)