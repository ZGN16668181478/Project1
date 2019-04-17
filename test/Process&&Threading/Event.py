import threading, time

# 进行事件触发可以像视频暂停接着播放一般
def func():
    # 事件对象
    event = threading.Event()
    def run():
        for i in range(5):
            # 阻塞，等待事件触发
            event.wait()
            # 事件清零
            event.clear()
            print('oh shit mother fucker!%d'%i)
    t = threading.Thread(target=run).start()
    return event

if __name__=="__main__":
    e = func()
    # 进行触发事件
    for i in range(5):
        time.sleep(1)
        e.set()