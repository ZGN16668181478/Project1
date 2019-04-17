import threading

# 协程主要是利用了生成器，生成器yield之后的代码不会再进行执行了，之后代码代码包括 n =
def product(c):
    # 往customer发送任意一个数据来接下生成器之后的代码开始执行
    c.send(None)
    for i in range(5):
        print('生产者生产了%d'%i)
        # 往消费者接着执行生成器之后代码
        r = c.send(str(i))
        print('消费者消费了数据%s'%r)
    c.close()
def customer():
    data = ""
    while True:
        n = yield data
        if not n:
            return
        # 这里的n直接是上面传过来的，即生成器执行之后的数据
        print('消费者消费了%s'%n)
        data = "200"

c = customer()
product(c)