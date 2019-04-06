# map  类似分布式
def ChrInt(list):
    return 'shit'
l = map(ChrInt,[1,2,3])  # 惰性序列
print(list(l))

from functools import reduce
def Add(x,y):
    return str(x)+str(y)
res = reduce(Add,['oh ','shit ','mother ','fucker'])