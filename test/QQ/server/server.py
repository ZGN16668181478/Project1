import tkinter
import threading
import socket

win = tkinter.Tk()
win.title('QQ服务器')
win.geometry('500x400+400+100')


# 进行交互,以及存储用户
user = {}
def run(clientSocket,clientAddress):
    print('xxxxxxxxxxxxxxxxxxxx')
    # 接收用户名
    userName = clientSocket.recv(1024)
    user[userName] = clientSocket
    print(user)

    # content.insert(tkinter.INSERT,userName)
    # print('客户端：',content.decode('utf-8'))
    # clientSocket.send('oh shit mother fucker!'.encode('utf-8'))
    # 对收到的数据进行处理,然后将数据发送另一个客户端
    while True:
        rData = clientSocket.recv(1024)
        StrData = rData.decode('utf-8')
        strList = StrData.split(':')
        user[strList[0]].send(strList[1].encode('utf-8'))

# 启动服务器
def start():
    ip = eip.get()
    port = eport.get()
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip, int(port)))
    server.listen(10)
    while True:
        clientSocket, clientAddress = server.accept()
        print('客户端连接......:',clientSocket)
        # 这里通过创建线程来进行服务器客户单进行同时交互
        t = threading.Thread(target=run, args=(clientSocket,))
        t.start()

def startServer():
    s = threading.Thread(target=start)
    s.start()

# 构建页面模型
labelIp = tkinter.Label(win,text="ip").grid(row=0,column=0)
labelPort = tkinter.Label(win,text="Port").grid(row=1,column=0)
eip = tkinter.Variable()
eport = tkinter.Variable()
entryIp = tkinter.Entry(win,textvariable=eip).grid(row=0,column=1)
entryPort = tkinter.Entry(win,textvariable=eport).grid(row=1,column=1)
button = tkinter.Button(win,text='启动',command=startServer).grid(row=2,column=1)

# 显示交互信息
content = tkinter.Text(win,width=30,height=10)
content.grid(row=3,column=1)
win.mainloop()