import win32com
import win32com.client

def writePPT(path):
    # 通过系统进行打开
    ppt = win32com.client.Dispatch('PowerPoint.Application')
    ppt.Visiable()

    # 增加一个文件
    pptFile = ppt.Presentations.Add()

    # 创建页
    page1 = pptFile.Slides.Add(1,1)
    t1 = page1.Shapes[0].TextFrame.TextRange
    t1.Text = 'oh shit mother fucker!'
    t2 = page1.Shapes[1].TextFrame.TextRange
    t2.Text = 'Damn it'

    # 保存并关闭
    pptFile.SaveAs(path)
    pptFile.Cloe()
    ppt.Quit()

path = r'F:\Notes\sublime\Python\file\writePPT.ppt'
writePPT(path)