import doctest

# doctest可以提取注释中的代码然后进行执行
def Sum(x,y):
    '''
    get The Sum form x and y
    :param x: firstName
    :param y: secondName
    :return: Sum

    example:
    >>> print(Sum(1,2))
    3
    '''
    return 1+2+1
print(Sum(1,2))

# 进行文档测试
doctest.testmod()