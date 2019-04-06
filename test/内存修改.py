import win32con
import win32gui
import win32api
import ctypes
import win32process

# 设置最高权限
PROCESS_ALL_ACCESS = (0x000F0000|0x100000|0xFFF)

#找窗体
win = win32gui.FindWindow('TXGuiFoundation','TIM')

# 根据窗体找到进程号
hid,pid = win32process.GetWindowThreadProcessId(win)

# 以最高权限打开进程
p = win32api.OpenProcess(PROCESS_ALL_ACCESS,False,pid)

# 加载内核模块
md = ctypes.windll.LoadLibrary("C:\\Windows\\WinSxS\\wow64_microsoft-windows-kernel32_31bf3856ad364e35_10.0.17134.556_none_7fb3165ce0c63558\\kernel32")
data = ctypes.c_long()

# 读取内存
md.ReadProcessMemory(int(p),69351900,ctypes.byref(data))
newData = ctypes.c_long(10000)
md.ReadProcessMemory(int(p),69351900,ctypes.byref(newData),4,None)
