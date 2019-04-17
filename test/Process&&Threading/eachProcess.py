from multiprocessing import Process,Queue
import time,os

# 通过在两个进程中使用队列来存储并相互传递数据，达到通信的效果
def write(q):
    print('进程write开始了....',os.getpid())
    nameList = ['shit','damn','fucker']
    for name in nameList:
        q.put(name)
    print('namelist插入成功！')
    print('进程write完成！')

def read(q):
    print('进程read开始了....',os.getpid())
    # 用一个死循环来进行获取结果
    while True:
        value = q.get(True)
        print('value=',value)
    print('进程read完成！')

if __name__=='__main__':
    print('父进程开始了....',os.getpid())
    q = Queue()
    start = time.time()
    pw = Process(target=write,args=(q,))
    pr = Process(target=read,args=(q,))
    end = time.time()
    pw.start()
    pr.start()
    pw.join()
    # pr.join()

    # if (end-start) > 6 :
    pr.terminate()
    print('父进程完成！')
