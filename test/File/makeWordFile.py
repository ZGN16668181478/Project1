import docx
import pydoc
import pythoncom
import win32com
import win32com.client
import sys
sys.coinit_flags = 0
def makeWordFile():
    win32com.client.Dispatch('Word.Application','')
    
makeWordFile()