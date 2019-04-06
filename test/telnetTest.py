import telnetlib

def telnetDone(ip,user,passwd,command):
    try:
        # 连接服务器
        telnet = telnetlib.Telnet(ip)
        # 设置调试级别
        telnet.set_debuglevel(2)

        # 读取终端用户名
        nameContent = telnet.read_until('Login username:'.encode('utf-8'))
        # 写入用户名
        telnet.write((user + '\r\n').encode('utf-8'))
        # 读取终端密码进行写入
        pwd = telnet.read_until('Login password:'.encode('utf-8'))
        telnet.write((passwd + '\r\n').encode('utf-8'))
        # 读取验证IP并写入用户信息
        comfirm = telnet.read_until('Domain name'.encode('utf-8'))
        telnet.write((command + '\r\n').encode('utf-8'))
        return True
    except:
        return False

if __name__=='__main__':
    ip = '169.254.179.36'
    password = '123456'
    user = 'Damn it'
    command = 'shutdown /s'
    print(telnetDone(ip,password,user,command))