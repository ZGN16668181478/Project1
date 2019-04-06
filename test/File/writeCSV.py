import csv,os

def writeCSV(path,data):
    with open(path,'w')as f:
        if os._exists(path):
            print('file is exist, Warning!')
            write = csv.writer(f)
            for dataLine in data:
                write.writerow(dataLine)
        else:
            write = csv.writer(f)
            for dataLine in data:
                write.writerow(dataLine)
    return 'ok'

path = r'F:\Notes\sublime\Python\csv\forWriteCSV.csv'
data = [['name','age','gender'],['tom',11,'male'],['shit',21,'Female']]
status = writeCSV(path,data)
print(status)