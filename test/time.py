import time

t = time.time()
b = time.localtime(t)
print(b)
print(time.strftime('%Y-%m-%d %X',b))

import datetime

n = datetime.datetime.now()
print(n)
print(time.asctime(b))

import calendar
# print(calendar.calendar(2019))
print(calendar.monthrange(2019,3))
print(calendar.monthcalendar(2019,3))

msg = "\\u4f60\\u63d0\\u4ea4\\u8fc7\\u6765\\u7684\\u77ed\\u4fe1\\u5185\\u5bb9\\u5fc5\\u987b\\u4e0e\\u62a5\\u5907\\u8fc7\\u7684\\u6a21\\u677f\\u683c\\u5f0f\\u76f8\\u5339\\u914d"
print(msg.encode('utf-8').decode('utf-8'))