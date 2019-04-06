from urllib import request
import requests
from bs4 import BeautifulSoup


class getContent(object):
    def __init__(self,path):
        self.path = path
        self.content = requests.get(self.path).text.encode('utf-8')
        self.soup = BeautifulSoup(self.content)

    def getImg(self,toPath):
        links = []
        imgHref = self.soup.find_all('img')
        for link in imgHref:
            if link!=None:
                i = imgHref.index(link)
                print('获取图片连接中........')
                link = path + link.get('src')
                name = link[-4:]
                request.urlretrieve(link,(toPath+'\\'+str(i)+name))
                print('图片下载完成')
                links.append(link)
        return 'OK'

    def getText(self):
        # ul = self.soup.select('div[class="pc_list"] li a')
        ul = self.soup.select('div[class="pc_list"] li a')
        # print(ul)
        pathList = []
        for a in ul:
            if a!=None:
                # print(a)
                link = self.path + a.get('href')
                self.getRealText(link)
                pathList.append(link)
        print(pathList)
        print("="*100)
        # ul.get('href')

    def getRealText(self,textPath):
        text = requests.get(textPath).text.encode('utf-8')
        text = BeautifulSoup(text)
        content = text.select('div[id="content1"]')
        print(content)


path = 'https://www.qisuu.la/'
path2 = 'https://www.qisuu.la/du/9/9118/'
textPath = 'https://www.qisuu.la/du/9/9118/17288415.html'
toPath = r'C:\Users\Asus\PycharmProjects\Project1\test\spider\img'
c = getContent(path2)
c.getRealText(textPath)