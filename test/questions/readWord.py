import win32com
import win32com.client

def readWordFile(path):
    # import os
    # os.system('taskkill /im wps.exe')
    # 调用系统的word功能，可以处理doc和docx两种文件，设置格式
    mv = win32com.client.Dispatch('Word.Application')
    # 打开文件
    doc = mv.Document.Open(path)
    # 进行读取
    for paragraph in doc.Paragraphs:
        line = paragraph.Range.Text()
        print(line)
    # 关闭文件和关闭调用系统的doc入口
    doc.Close()
    mv.Quit()

def readDocx(path):
    import docx
    file = docx.Document(path)
    for con in file.paragraphs:
        print(con.text)

path = r'C:\Users\Asus\Desktop\新建文件夹\doc\Do college students need teachers.docx'
path2 = r'C:\Users\Asus\Desktop\1.docx'
readWordFile(path)
# readDocx(path)