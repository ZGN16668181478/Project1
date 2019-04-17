from multiprocessing import Process
import time,os

class myProcess(Process):
    def __init__(self,name):
        Process.__init__(self)
        self.name = name

    def run(self):
        print('子进程%s启动....'%self.name,os.getpid())
        time.sleep(1)
        print('子进程%s结束！'%self.name)