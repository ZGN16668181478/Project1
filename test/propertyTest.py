class Person(object):
    def __init__(self,name):
        # self.name = name
        # 限制访问
        self.__name = name

    # 使用限制访问，进行封装
    @property
    def Name(self):
        return self.__name
    @Name.setter
    def Name(self,name):
        self.__name = name
per = Person('shit')
# print(per._Person__name)
# 限制访问，外部无法进行访问
# print(per.name)
# 这里无法对里面的name进行访问，通过手动添加，两个装饰器进行setter和getter封装
per.name = 'oh shit mother fucker!'
# 这里是通过setter和getter方法来对属性进行修改的
print(per.name)
