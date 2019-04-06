import sys
import importlib
importlib.reload(sys)

from pdfminer.pdfparser import PDFParser,PDFDocument
from pdfminer.pdfinterp import PDFResourceManager,PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal,LAParams
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed

def readPDF(path,topath):
    # 以二进制打开文件
    f = open(path,'rb')
    # 创建一个pdf文档分析器
    parser = PDFParser(f)
    # 创建pdf文档
    pdfFile = PDFDocument()
    # 链接分析器和文档对象，相互链接
    parser.set_document(pdfFile)
    pdfFile.set_parser(parser)
    # 提供初始化密码
    pdfFile.initialize()
    # 检测文档是否提供txt转换
    if not pdfFile.is_extractable:
        raise PDFTextExtractionNotAllowed
    else:
        # 解析数据

        # 数据管理器
        manager = PDFResourceManager()
        # 创建pdf设备对象
        laparams = LAParams()
        device = PDFPageAggregator(manager,laparams=laparams)
        # 解释器对象
        interpreter = PDFPageInterpreter(manager,device)

        # 开始循环处理，每次处理一页
        for page in pdfFile.get_pages():
            interpreter.process_page(page)
            layout = device.get_result()
            for x in layout:
                if (isinstance(x,LTTextBoxHorizontal)):
                    with open(topath,'a') as f:
                        str = x.get_text()
                        print(str)
                        f.write(str+"\n")
path = r'C:\Users\Asus\Desktop\sss.pdf'
topath = r'C:\Users\Asus\PycharmProjects\Project1\test\File'
readPDF(path,topath)