import socket
import threading
# 绑定协议
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 绑定ip端口
server.bind(("169.254.179.36",8021))
# 监听
server.listen(5)
# 等待连接
clientSocket, clientAddress = server.accept()
# while True:
#
#     t = threading.Thread()
#     t.start()
print("服务器启动成功..........")
# while True:
#     data = clientSocket.recv(1024)
#     print("收到"+str(clientSocket)+"的数据"+data.decode('utf-8'))
