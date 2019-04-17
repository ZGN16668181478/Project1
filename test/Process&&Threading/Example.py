from multiprocessing import Process
from time import sleep
import os

num = 100
def run():
    # while True:
    print('子进程开始....==', os.getpid())
    sleep(1.2)
    print('子进程结束...==')
def run2():
    global num
    num += 1
    print(num)

if __name__=='__main__':
    print('主进程开始了....==', os.getpid())
    sleep(1)
    p1 = Process(target=run)
    p1.start()
    # 设置join,父进程会执行完子进程再接着执行父进程
    p1.join()


    p2 = Process(target=run2)
    p2.start()
    p2.join()# 这里没有join就会先执行完后面的语句，然后执行这个进程
    print('主进程结束了!')

