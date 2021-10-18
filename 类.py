#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):

    def __init__(self, name, score):#__表示将其定为private
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'
    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score
    def set_score(self, score):
        self.__score = score #允许从外面修改score
    abc=property(get_score,get_name,get_grade,doc='文档信息')

print(Student.abc.__doc__)
bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)

try:
    print(bart.__score)
except AttributeError as e:
    print('print(bart.__score)错误为{},因为是private属性'.format(e))
bart.print_score()

'''赋值方法无法改变内部变量_Student__score,而是外部新增了一个__score变量'''
bart.__score=90
print(bart.get_score())

bart.set_score(99) #外部修改score
print(bart.get_score())

'''__score是一开始外部新增的,_Student__score才是内部的'''
print(bart.__score)
print(bart._Student__score)

'''类的继承'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('Dog is running...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')

def run_twice(animal):
    animal.run()
    animal.run()

a = Animal()
d = Dog()
c = Cat()

print('a is Animal?', isinstance(a, Animal))
print('a is Dog?', isinstance(a, Dog))
print('a is Cat?', isinstance(a, Cat))

print('d is Animal?', isinstance(d, Animal))
print('d is Dog?', isinstance(d, Dog))
print('d is Cat?', isinstance(d, Cat))

run_twice(c)


