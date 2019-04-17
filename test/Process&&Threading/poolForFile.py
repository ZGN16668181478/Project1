import os,time,random
from multiprocessing import Pool

def copyFile(path,toPath):
    fr = open(path,'r')
    fw = open(toPath,'w')
    content = fr.read()
    fw.write(content)
    fr.close()
    fw.close()

if __name__=='__main__':
    path = r'F:\Notes\sublime\jsp'
    toPath = r'F:\Notes\sublime\test'
    print('开始文件复制.....')
    start = time.time()
    pp = Pool(3)
    fileList = os.listdir(path)
    for file in fileList:
        pp.apply_async(copyFile,args=(os.path.join(path,file),os.path.join(toPath,file)))
    pp.close()
    pp.join()
    end = time.time()
    print('文件拷贝完成！耗时：'+str(end-start))