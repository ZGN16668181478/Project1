import csv

# 避免功能性文件进行打印
def readCSV(path):
    listInfo = []
    with open(path,'r') as f:
       allCsvInfo = csv.reader(f)
       # 每一行的进行读取
       for csvLine in allCsvInfo:
           print('xxxxxx')
           listInfo.append(csvLine)
    return listInfo

path = r'F:\Notes\sublime\Python\csv\forReadCSV.csv'
path2 = r'F:\Notes\sublime\Python\csv\forWriteCSV.csv'
content = readCSV(path2)
print(content)