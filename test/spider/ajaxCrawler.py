import ssl
import urllib.request
import json
import requests

url = 'https://movie.douban.com/typerank?type_name=%E5%89%A7%E6%83%85&type=11&interval_id=100:90&action='
headers = {"User-Agent":'User-Agent:Mozilla/5.0'}

req = urllib.request.Request(url,headers=headers)
res = urllib.request.urlopen(req)
jsonStr = res.read().decode('utf-8')
# print(jsonStr)
jsonStr = jsonStr.replace('<html lang="zh-cmn-Hans" class=""><head>(.*?)</head><body><pre style="word-wrap: break-word; white-space: pre-wrap;">', '')
jsonStr = jsonStr.replace('</pre></body></html>', '')

print(jsonStr)
jsonData = json.loads(jsonStr)
print(jsonData)