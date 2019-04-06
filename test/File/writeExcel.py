from pyexcel_xls import get_data,save_data
from collections import OrderedDict
import os
def writeExcel(path,data):
    dic = OrderedDict()
    if not os.path.exists(path):
        with open(path,'a'):
            pass
    if os.path.exists(path):
        for sheetName, sheetValue in data.items():
            # 用一个字典来存储，再将这个字典全部插入到dic里面
            d = {}
            d[sheetName] = sheetValue
            dic.update(d)
            # dic[sheetName] = sheetValue
    save_data(path,dic)

path = r'F:\Notes\sublime\Python\file\ExcelWrite.xls'
data = {'sheet1':[[1,2,3],[4,5,6],[7,8,9]],
        'sheet2':[[11,22,33],[44,55,66],[77,88,99]]}
writeExcel(path,data)