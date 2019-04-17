import threading

# 锁对象  让部分执行的代码上锁，先上锁没有解锁就不能进行执行该段代码，直到释放后才能进行使用
lock = threading.Lock()
num = 100
def run(n):
    global num
    for i in range(1000000):
        # num = num + n
        # num = num - n
        # 加个锁，避免数据被篡改，但这种将会是单线程执行，速度很慢，而且死锁几率很大
        # lock.acquire()
        # try:
        #     num = num + n
        #     num = num - n
        # 最终一定要关闭锁，不然如果上面两行代码执行出错将会一直不会往下执行，造成死锁
        # finally:
        #     lock.release()
        # 这种方式的锁，能更大程度上的降低死锁的几率
        with lock:
            num = num + n
            num = num - n


if __name__=='__main__':
    t1 = threading.Thread(target=run,args=(4,))
    t2 = threading.Thread(target=run,args=(8,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('num=',num)