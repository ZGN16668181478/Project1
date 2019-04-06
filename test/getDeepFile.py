import os

def getAllDir(path):
    stack = []
    stack.append(path)

    # 处理栈，当栈为空时结束循环
    while len(stack)!=0:
        # 从栈里边取出数据
        dirPath = stack.pop()
        if os.path.isdir(dirPath):
            fileList = os.listdir(dirPath)
            for file in fileList:
                # filePath = os.path.abspath(file)
                filePath = os.path.join(path,file)
                if os.path.isdir(filePath):
                    print('目录：',file)
                    stack.append(file)
                else:
                    print('文件：',file)
                    stack.pop()
            print(stack)
            print(fileList)


if __name__=='__main__':
    path = 'F:\\Notes\\sublime'
    getAllDir(path)