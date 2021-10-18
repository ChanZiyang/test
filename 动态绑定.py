class Student(object):
    pass
s=Student()
s.name='fuck' #动态给实例绑定属性

def set_age(self,age): #在类以外定义一个函数作为方法
    self.age=age

from types import MethodType
s.set_age=MethodType(set_age,s) #给实例绑定一个方法
s.set_age(25)
print(s.age) #age这个属性已经被赋值为25了

Student.fuck_age=set_age #给class绑定方法,新增了方法名为fuck_age,实际上是set_age函数

s2=Student()
s2.fuck_age(0) #所有实例都能用
print(s2.age)

'''slots方法'''
class fuck(object):
    __slots__ = ('name','age') #用tuple定义允许绑定的属性

f1=fuck()
try:
    f1.score = 99
except AttributeError as e:
    print('AttributeError:', e)

class fuck2(fuck):  #然而继承的子类不会继承slots,除非子类定义slot
    __slots__ = ('score')  #此时子类允许的属性是父类+子类

f=fuck2()
f.name=10
print(f.name)

