import json

jsonStr = '{"name":"shit","age":14,"hobby":["money","power","girl"],"params":{"a":1,"b":2}}'

# 本地获取，需要获取json类型
JStr = json.loads(jsonStr)
print(JStr)
print(JStr['params']['a']) 
print(type(JStr))
# 传给服务器时，需要传字符串类型的
JStr2 = json.dumps(JStr)
print(JStr2)
print(type(JStr2))