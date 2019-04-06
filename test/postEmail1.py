# -*- coding: utf-8 -*-

import smtplib
# 发邮件的文本形式
from email.mime.text import MIMEText
# 通过服务器连接发邮件人的邮箱
# SMTP服务器
SMTPServer = 'smtp.163.com'
# 发邮件地址
sender = '1666818478@163.com'
# 发件人密码
password = 'Zhang990203'


#设置发送
# 发送内容
content = 'oh shit mother fucker!'
# 将内容转成邮件文本
msg = MIMEText(content,'ISO-8859-1  ')
msg["Accept-Language"]="zh-CN"
msg["Accept-Charset"]="ISO-8859-1,utf-8"
# 设置邮件的标题
msg['Subject'] = 'from the Brother Nan'
# 设置发送者
msg['from'] = sender

# 进行发送
# 创建SMTP服务器
mailServer = smtplib.SMTP(SMTPServer,25)
# 在服务器登录邮箱
mailServer.login(sender,password)
# 开始发送  记住内容要以SMTP字符串格式发送
mailServer.sendmail(sender,['1666818478@163.com'],msg.as_string())
# 退出邮箱
mailServer.quit()