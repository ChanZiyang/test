def log(fuck):
    def warpper(*args,**kwargs):
        print('call {}():'.format(fuck.__name__))
        return fuck(*args,**kwargs)
    return warpper

@log
def now():
    print('fuck you python')
now()

'''@方法等价于'''
now_super=log(now) #now是指向warpper的,所以fuck.name是warpper
now_super()
print('now_super的函数名是:',now_super.__name__)

'''使用functools可以修改好名字'''
from functools import wraps
def fog(fuck):
    @wraps(fuck)
    def warpper(*args,**kwargs):
        print('call {}():'.format(fuck.__name__))
        return fuck(*args,**kwargs)
    return warpper

@fog
def f():
    pass
now_x=fog(f)
print('now_x的函数名是:',now_x.__name__) #此时能正确显示函数名


'''带参数的decorator'''
def info(value):
    def decorator(func): #把上面的代码再套了一层
        def wrapper(*args, **kwargs):
            print(value)
            return func(*args, **kwargs)

        return wrapper

    return decorator

@info('456')
def say_hello():
    print('同学你好')

say_hello()
'''等价于'''
say_hello_super=info('nmsl')(say_hello)
