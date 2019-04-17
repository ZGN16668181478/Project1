import threading, time

# 进行线程调度
cond = threading.Condition()
def run1():
    with cond:
        for i in range(0,10,2):
            print(threading.current_thread().name,i)
            time.sleep(0)
            cond.wait()
            cond.notify()

def run2():
    with cond:
        for i in range(1,10,2):
            print(threading.current_thread().name,i)
            time.sleep(0)
            cond.notify()
            cond.wait()
if __name__=="__main__":
    threading.Thread(target=run1).start()
    threading.Thread(target=run2).start()