import time
import pygame
file=r'F:\Notes\sublime\Python\music\shuangsheng.mp3'
pygame.mixer.init()
print("播放音乐1")
track = pygame.mixer.music.load(file)

pygame.mixer.music.play()
time.sleep(10)
pygame.mixer.music.stop()