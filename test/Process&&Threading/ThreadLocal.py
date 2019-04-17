import threading

num = 10
local = threading.local()

def run(x,n):
    x = x + n
    x = x - n
# 这里是对这个方法用两个线程进行使用，然后再进行对比
def func(n):
    local.x = num
    for i in range(1000000):
        run(local.x,n)
    print('%s-%d'%(threading.current_thread().name,local.x))

if __name__=="__main__":
    t1 = threading.Thread(target=func,args=(4,))
    t2 = threading.Thread(target=func,args=(7,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()