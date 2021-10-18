'''把方法包装成属性'''
'''被 @property 装饰的方法是获取属性值的方法，被装饰方法的名字会被用做属性名。
被 @属性名.setter 装饰的方法是设置属性值的方法。
被 @属性名.deleter 装饰的方法是删除属性值的方法'''
class Screen(object):
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self,value):
        self._width=value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        return self._height*self._width

# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')

class Student:
    def __init__(self):
        self._age = None

    @property
    def age(self):
        print('获取属性时执行的代码')
        return self._age

    @age.setter
    def age(self, age):
        print('设置属性时执行的代码')
        self._age = age

    @age.deleter
    def age(self):
        print('删除属性时执行的代码')
        del self._age


student = Student()

# 设置属性
student.age = 18
"""
设置属性时执行的代码
"""

# 获取属性
print('学生年龄为：' + str(student.age))
"""
获取属性时执行的代码
学生年龄为：18
"""

# 删除属性
del student.age
"""
删除属性时执行的代码
"""



