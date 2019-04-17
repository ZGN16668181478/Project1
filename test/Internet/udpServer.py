import socket
# UDP协议和ip协议！！！
server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

server.bind(("169.254.179.36",8024))

while True:
    data,addr = server.recvfrom(1024)
    print("data和addr：",data,'|'*10,addr)
    print(data.decode('utf-8'))
    content = input('input what you say:')
    server.sendto(content.encode('utf-8'),addr)
    print('发送成功！')