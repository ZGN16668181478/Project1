import tkinter
import socket
import threading

win = tkinter.Tk()
win.title('QQ客户端')
win.geometry('500x400+400+100')

clientSocket = None
# 将消息发送到服务器
def sendMessage():
    content = eSendContent.get()
    user = eSender.get()
    clientSocket.send((content+':'+user))

# 从服务器获取消息进行显示到Text控件上
def getInfo():
    while True:
        data = clientSocket.recv(1024)
        text.insert(tkinter.INSERT,data.decode('utf-8'))
# 连接服务器
def connectServer():
    # 通过使用全局变量，以便于全局使用这个socket
    global clientSocket
    userName = eUser.get()
    ip = eIp.get()
    port = ePort.get()
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect((ip,int(port)))
    print('连接成功......')
    client.send(userName.encode('utf-8'))
    clientSocket = client
    t = threading.Thread(target=getInfo)
    t.start()

userName = tkinter.Label(win,text='userName').grid(row=0,column=0)
labelIp = tkinter.Label(win,text='Ip').grid(row=1,column=0)
labelPort = tkinter.Label(win,text='Port').grid(row=2,column=0)
eUser = tkinter.Variable()
eIp = tkinter.Variable()
ePort = tkinter.Variable()
entryUser = tkinter.Entry(win,textvariable=eUser).grid(row=0,column=1)
entryIp = tkinter.Entry(win,textvariable=eIp).grid(row=1,column=1)
entryPort = tkinter.Entry(win,textvariable=ePort).grid(row=2,column=1)
button1 = tkinter.Button(win,text='连接',command=connectServer).grid(row=2,column=2)
text = tkinter.Text(win,width=30,height=10)
text.grid(row=3,column=1)
sendContent = tkinter.Label(win,text='发送内容：').grid(row=4,column=0)
sender = tkinter.Label(win,text='发送者：').grid(row=5,column=0)
eSendContent = tkinter.Variable()
eSender = tkinter.Variable()
entrySendContent = tkinter.Entry(win,textvariable=eSendContent).grid(row=4,column=1)
entrySender = tkinter.Entry(win,textvariable=eSender).grid(row=5,column=1)
button = tkinter.Button(win,text='发送',command=sendMessage).grid(row=5,column=2)

win.mainloop()