import ssl
import urllib.request
import os
import re

def getQQNumber(url,toPath):
    headers = {"User-Agent":'User-Agent:Mozilla/5.0'}
    req = urllib.request.Request(url,headers=headers)
    res = urllib.request.urlopen(req)
    cont = res.read().decode('utf-8')
    print(len(cont))
    # 获取url
    pattern = r'((http|ftp|https):\/\/[\w\-_]+(\.[\w\-_]+)+([\w\-\.,@?^=%&amp;:/~\+#]*[\w\-\@?^=%&amp;/~\+#])?)'
    urlList = re.findall(pattern,cont)
    # print(urlList)
    # 获取qq号
    pattern_qq = r'([1-9]\d{4,9})'
    qqList = re.findall(pattern_qq,cont)
    # 去重
    qqList = list(set(qqList))
    # print(qqList)
    # 将QQ号存储到本地
    f = open(toPath,'a')
    for qq in qqList:
        f.write(qq+"\n")
    print('QQ号写入成功！')
    f.close()
    return urlList



url = 'https://www.douban.com/group/topic/110094603/'
toPath = r'C:\Users\Asus\PycharmProjects\Project1\test\spider\file\saveQQ.txt'
getQQNumber(url,toPath)