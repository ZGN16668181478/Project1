import win32api
import win32con
import time

# 鼠标放到某个位置就会进行双击
# 设置鼠标的位置
win32api.SetCursorPos([1300,800])
time.sleep(0.1)

# 鼠标左键按下
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0)
# 鼠标左键抬起
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0)