from multiprocessing import Pool
import time,os,random

def run(name):
    print('%s is starting!'%name,os.getpid())
    time.sleep(random.choice([1,2,3]))
    print('%s is finished!'%name)

if __name__=='__main__':
    print('Father Process is starting!',os.getpid())
    start = time.time()
    pp = Pool(3)
    for i in range(4):
        pp.apply_async(run,args=(i,))
    pp.close()
    pp.join()
    end = time.time()
    print('The end is consume %.3f'%(end-start))