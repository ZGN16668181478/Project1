import win32com.client
import time
speaker = win32com.client.Dispatch('SAPI.SPVOICE')
while 1:
    speaker.Speak('Oh shit mother fucker!')
    time.sleep(2)