path = r'C:\Users\Asus\PycharmProjects\Project1\test\test6.txt'

List = [1,2,3,4,5,'oh shit mother fucker']
import pickle
with open(path,'wb') as f:
    pickle.dump(List,f)

with open(path,'rb') as f:
    list = pickle.load(f)
    print(list)

import os
# print(os.system('notepad'))
print(type(os.system('taskkill /f /im notepad.exe')))