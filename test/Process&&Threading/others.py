import threading

# 控制执行线程数
s = threading.Semaphore(2)
# 凑够线程数再进行执行
bar = threading.Barrier(3)

def run():
    print('oh shit mother fucker!')
if __name__=='__main__':
    t = threading.Timer(3,run)
    t.start()