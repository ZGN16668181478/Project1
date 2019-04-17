import re
import requests
import urllib.request
from bs4 import BeautifulSoup

def getWork(url,savePath):
    req = requests.get(url)
    res = req.text.encode('utf-8')
    print(type(res))
    with open(savePath,'wb') as f:
        f.write(res)
    print('写入成功！')
    # print(res)

def getWorkByUrllib(url,savePath):
    headers = {"User-Agent":'User-Agent:Mozilla/5.0'}
    url = urllib.request.Request(url,headers=headers)
    req = urllib.request.urlopen(url)
    res = req.read()
    with open(savePath,'wb') as f:
        f.write(res)
    print('写入成功！')
    content = res.decode('utf-8')
    print(len(content))
url = r'http://202.197.212.73/Web%20Client/ListDir.htm#'
savePath = r'C:\Users\Asus\PycharmProjects\Project1\test\spider\file\work.html'
# getWork(url,savePath)
getWorkByUrllib(url,savePath)