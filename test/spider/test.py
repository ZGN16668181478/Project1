import urllib.request
import requests
import ssl
path = 'http://www.baidu.com'
# print(requests.get(path).text)
# 单独设置一个请求体
header = {
    "User-Agent":'User-Agent:Mozilla/5.0'
}
for i in range(1,20):
    try:
        req = urllib.request.Request(path, headers=header)
        con1 = urllib.request.urlopen(req, timeout=0.5).read().decode('utf-8')
        print(len(con1))
        print('获取成功，继续爬取............')
    except :
        print('请求超时，继续下一个爬取！')
# 把所有的代理放到一个可迭代对象里，然后进行随机放入

agentList = [
    "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "User-Agent:Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "User-Agent:Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"
]

# import random
# agent = random.choice(agentList)
# req2 = urllib.request.Request(path)
# req2.add_header("User-Agent",agent)
# con = urllib.request.urlopen(req2)
# print(con)