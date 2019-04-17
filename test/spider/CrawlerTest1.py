from urllib import request
import urllib
import ssl
import re
from bs4 import BeautifulSoup

def CrawlerTest1(getDataUrl):
    header = {"User-Agent":'User-Agent:Mozilla/5.0'}
    req = urllib.request.Request(url,headers=header)
    res = urllib.request.urlopen(req)
    cont = res.read().decode('utf-8')
    # print(cont)
    pattern = r'<div class="content">(.*?)</div>'
    # 它这里的任意不包括换行符，所以不进行修改会匹配不到数据
    divList = re.findall(pattern,cont,flags=re.S)
    print('本次数据有'+str(len(divList))+'行')
    contList = []
    for content in divList:
        soup = BeautifulSoup(content)
        content = soup.text
        contList.append(content)
    print("获取数据成功！")
    # print(contList)
    return contList

def saveData(writeStr,saveDataPath):
    with open(saveDataPath, 'a',encoding='utf-8') as f:
        for content in writeStr:
            f.write(content.replace('\n\n\n','\n'))
        print("保存成功！")

def getMorePageContent(url,savePath):
    for i in range(1,21):
        url = url+str(i)
        saveData(CrawlerTest1(url),savePath)
        print('获取第%.1f'%i+'数据成功！')

url = 'https://www.qiushibaike.com/text/'
savePath = r'C:\Users\Asus\PycharmProjects\Project1\test\spider\file\getCrawler.txt'
# saveData(CrawlerTest1(url),savePath)
getMorePageContent(url,savePath)