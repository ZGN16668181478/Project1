import threading, time, random, queue

# 生产不息，消费不止，队列放了取，取了放
# 生产者
def product(id,q):
    while True:
        num = random.randint(0,10000)
        q.put(num)
        print('生产者%d生产了%d数据放入了队列'%(id,num))
        time.sleep(1)
    # 任务完成
    q.task_done()

def consumer(id,q):
    while True:
        # num = random.randint(0,10000)
        item = q.get()
        if item is None:
            break
        print('消费者%d消费了%d数据'%(id,item))
    # 任务完成
    q.task_done()

if __name__=="__main__":
    # 消息队列
    q = queue.Queue()
    # 启动生产者
    for i in range(4):
        threading.Thread(target=product,args=(i,q)).start()
    # 启动消费者
    for i in range(4):
        threading.Thread(target=consumer,args=(i,q)).start()