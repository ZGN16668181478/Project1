import pygame
import time

# 音乐路径
filepath = r'C:\Users\Asus\Music\双笙 - 大鱼.mp3'
filepath2 = r'C:\Users\Asus\Desktop\新建文件夹\test\1.mp3'
filepath = filepath.encode('utf-8')
# 初始化
pygame.mixer.init()
# 加载音乐
print('加载音乐')
track = pygame.mixer.music.load(filepath2)
# 播放

pygame.mixer.music.play(1,0.0)
#
time.sleep(1000









           )
# 暂停
pygame.mixer.music.stop()