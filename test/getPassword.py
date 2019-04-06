import itertools

mylist = list(itertools.permutations([1,2,3,4],3))
mylist2 = list(itertools.combinations([1,2,3,4],3))
mylist3 = list(itertools.product([1,2,3,4],repeat=4))  # 这个repeat代表几位的密码
print(mylist3)
print(len(mylist3))