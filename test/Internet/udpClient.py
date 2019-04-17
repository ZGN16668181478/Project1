import socket

client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
    content = input('input what you say:')
    client.sendto(content.encode('utf-8'),("169.254.179.36",8024))
    print('发送成功！')
    data = client.recv(1024).decode('utf-8 ')
    print("服务器：",data)