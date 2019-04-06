import win32com
import win32com.client
import docx

def ReadWordToOtherFile(path,toPath):
    cont = docx.Document(path)
    cont = [x.text for x in cont.paragraphs]
    with open(toPath,'w') as f:
        for v in cont:
            f.write(v)
        print('OK')

path = r'C:\Users\Asus\Desktop\新建文件夹\doc\Do college students need teachers.docx'
toPath = r'C:\Users\Asus\Desktop\新建文件夹\doc\copy.txt'

ReadWordToOtherFile(path,toPath)