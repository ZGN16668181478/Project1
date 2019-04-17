import urllib.request
from collections import deque
import time
from getQQNumber import getQQNumber
# 首先输入一个url，从这个url中存取QQ号，返回分页的网址，然后进继续获取

def centerDeal(url,toPath):
    queue = deque()
    # 进队
    queue.append(url)
    # 进行批处理 只要队列不空就行
    while len(queue)!=0:
        # 出队数据
        qUrl = queue.popleft()
        print('开始获取一个页面的QQ号........')
        urlList = getQQNumber(qUrl,toPath)
        for item in urlList:
            item = item[0]
            queue.append(item)
        print('歇一会接着爬取.......')
        time.sleep(2)

url = 'https://www.douban.com/group/topic/110094603/'
toPath = r'C:\Users\Asus\PycharmProjects\Project1\test\spider\file\saveQQ.txt'
centerDeal(url,toPath)