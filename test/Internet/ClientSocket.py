import socket
# 1、创建一个socke  指定ip协议参数(这里是IpV4)，和使用面向流TCP协议
sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 2、建立连接 the address is a pair (host, port). 所以参数是个元组
sk.connect(("www.sina.com.cn",80))

# 发送请
# sk.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

sk.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

# 等待接收数据
data = []
while True:
    # 每次接收数据都是1024的整数倍
    tempData = sk.recv(1024)
    if tempData:
        data.append(tempData)
    else:
        break
dataStr = (b''.join(data)).decode('utf-8')
sk.close()
print(dataStr)
# dataStr = ''
# for ds in data:
#     dataStr.join('\n'+ds.decode('utf-8'))
# # soup = BeautifulSoup(dataStr)
# # print(data)
# # for a in data:
# #     print(a.decode('utf-8'))
# print(dataStr)