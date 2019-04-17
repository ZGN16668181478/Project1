import socket
import sys
sk = socket.socket()
sk.connect(("127.0.0.1", 8888))  # 主动初始化与服务器端的连接
send_data = input("输入发送内容：")
sk.sendall(bytes(send_data, encoding="utf8"))
accept_data = sk.recv(1024)
print(str(accept_data, encoding="utf8"))
sk.close()

s.close()

print(msg.decode("utf-8"))
print(msg3.decode("utf-8"))