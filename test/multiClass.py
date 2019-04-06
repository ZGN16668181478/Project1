# 定义一个动物类，让他可以吃和有名字
class Animal():
    def __init__(self,name):
        self.name = name
    def eat(self):
        print(self.name,'吃')
# 让猫可以吃
# class Cat():
#     def __init__(self,name):
#         self.name = name
#     def eat(self):
#         print(self.name,'吃')
# # 让狗可以吃
# class Dog():
#     def __init__(self,name):
#         self.name = name
#     def eat(self):
#         print(self.name,'吃')

# 按照这样先让所有动物都能吃，岂不是要写很多方法？

# 省掉eat方法,只需要一个初始化来完成
class Cat(Animal):
    def __init__(self,name):
        # 这里的init方法中name，将name传入到Animal中，通过Animal调用eat方法，在Cat类中实现方法的功能
        super(Cat, self).__init__(name)

class Dog(Animal):
    def __init__(self,name):
        super(Dog, self).__init__(name)
# 定义一个人类，可以喂猫和老鼠吃

class Person(object):
    # 这里feedCat方法，通过传入Cat好调用Animal中eat方法，在这个方法中实现
    def feedCat(self, Cat):
        Cat.eat()
    def feedDog(self, Dog):
        Dog.eat()

from types import MethodType
def say(self):
    print('my name is '+self.name)
if __name__=='__main__':
    tom = Cat('tom')
    person = Person()
    # 这里必须指明，feedCat 中传入的参数必须是Cat类型
    person.feedCat(Cat('tom'))
    person.feedDog(Cat('jerry'))
    # 给person加属性
    person.name = 'oh shit mother fucker!'
    # 给person加方法
    person.speak = say
    # 给person
    speak = MethodType(say,person)
    speak()