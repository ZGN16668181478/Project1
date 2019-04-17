import ssl
import re
import urllib.request
from bs4 import BeautifulSoup
import os
import time

def getYHDImage(url,savePath):
    headers = {"User-Agent":'User-Agent:Mozilla/5.0'}
    req = urllib.request.Request(url,headers=headers)
    res= urllib.request.urlopen(req)
    content = res.read().decode('utf-8')
    # saveHTML(content)
    pattern = r'<img src="//(img.*?)"/>'
    imgList = re.findall(pattern,content)
    print(imgList)
    num = 1
    del imgList[-2:]
    for imgUrl in imgList:
        imgUrl = os.path.join('https://',imgUrl)
        toPath = os.path.join(savePath,str(num)+'.jpg')
        print('第', str(num),'正在下载.......')
        print('imgUrl:',imgUrl)
        print('toPath',toPath)
        urllib.request.urlretrieve(imgUrl,toPath)
        print('第',str(num),'下载完成！')
        num += 1
        time.sleep(1.5)
    print('全部下载完成！啦啦啦啦啦！')
    # print(len(imgList))
    # print(imgList[1])
    # print(savePath+r'\1.jpg')
    # savePath = savePath+r'\1.jpg'
    # urllib.request.urlretrieve(imgList[1],savePath)

    # saveImgList(imgList,savePath)



def saveImgList(imgList,savePath):
    for img in imgList:
        i = 1
        print('正在下载中......')

        # savePath = savePath+str(i)+'.jpg'
        print(savePath)
        urllib.request.urlretrieve('http:' + img,savePath+str(i)+'.jpg')
        print('http:' + img)
        print('第'+str(imgList.index(img))+'下载完成！')
        i += 1

def saveHTML(content):
    path = r'C:\Users\Asus\PycharmProjects\Project1\test\spider\html\yhd.html'
    with open(path,'wb') as f:
        f.write(content)
    print('写入成功！')
savePath = r'C:\Users\Asus\PycharmProjects\Project1\test\spider\img'
url = 'http://search.yhd.com/c0-0/mbname-b/a80746::2342-s1-v4-p1-price-d0-f0b-m1-rt0-pid-mid0-color-size-k%E5%A5%B3%E8%A3%85/'
getYHDImage(url,savePath)
