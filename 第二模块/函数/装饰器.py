#coding=utf-8

import time,functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        print("call %s():" % func.__name__)
        func(*args,**kw)
    return wrapper

@log   ##
def now():
    print("2017-4-5")

now()
print(now)
##注意这里是没有讲到的地方
print(now.__name__)    #当没有使用@functools.wrap时，经过装饰器之后的now函数，再执行now.__name__时值就会改变为wrapper.
#为了解决这个问题，加入了一句话：@functools.wraps(func)


#装饰器：
#now=log(now)
#带参数的装饰器需要再进行函数嵌套，

#start_time=time.time()
#print("test")
#end_time=time.time()
#print(end_time-start_time)


def metric(func):
    @functools.wraps(func)
    def wrapper1(*args,**kw):
        starttime=time.time()
        f=func(*args,**kw)
        endtime=time.time()
        print('%s executed in %f ms' % (func.__name__, endtime-starttime))
        return f
    return wrapper1

@metric
def fast(x, y):
    time.sleep(0.12)
    return x + y

@metric  #slow=metric(slow)
def slow(x, y, z):
    time.sleep(0.34)
    return x * y * z


print("-------分割线------------")
f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('fast测试失败!')
elif s != 7986:
    print('slow测试失败!')


def login():
    def wrapper():
        f=open("database.txt",'r')
        data=f.read().rstrip()
        person=data.split(",")
        print(person)
        # for line in data:
        #     line=line.rstrip()
        #     person=line.split(",")
        #     print(type(person))
        #     print(person[0],person[1])
        #     username=input("enter your username: ")
        #     password=input("enter your password: ")
        #     if username==person[0] and password==person[1]:
        #         print("done")
        username = input("enter your username: ")
        password=input("enter your password: ")
        if username==person[0] and password==person[1]:
            print("done")
    return wrapper()
login()

#生成器
