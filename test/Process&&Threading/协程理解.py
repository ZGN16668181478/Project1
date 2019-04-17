import threading

def run():
    # 空变量，存储的作用data始终为空
    data = ""
    r = yield data
    print(1,r,data)
    r = yield data
    print(2,r,data)
    r = yield data
    print(3,r,data)

m = run()
# 启动生成器，即启动协程
print(m.send(None))
print(m.send('a'))
print(m.send('b'))
# print(m.send('c'))
# print(m.send('d'))
print('xxxxxx')