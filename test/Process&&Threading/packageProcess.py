from myProcess import myProcess

if __name__=='__main__':
    print('父进程启动....')
    # 创建子进程
    p = myProcess('shit')
    # 自动调用myProcess中的run方法
    p.start()
    p.join()
    print('父进程完成！')
