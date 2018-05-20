# -*-coding: utf-8 -*-
# 封装的访问限制：属性和函数前加__ 就会隐藏，例子中是即__x ,__foo，此时外部无法访问了
# 验证一：
#
# class A:
#     __x = 1     # 在类定义时变成了 _A__x=1
#
#     def __init__(self, name):
#         self.__name = name    # 在类定义时变成了 _A__name=name
#
#     def __foo(self):    # 在类定义时变成了 _A__foo
#         print("fron foo")
#
#     def bar(self):
#         self.__foo()   # 可以调用隐藏的函数，为什么？因为在类定义时，已经变成self._A__foo
#         print("from bar")
#
# a = A("scott")
# #print(a.__x)    # 抱错
# #print(a.__foo)  # 抱错
# a.bar()  #成功访问
# #为什么？先看一下类的属性到底有啥
# print(A.__dict__) # 可以看出 __x 变成了_A__x
#
# print(a._A__name) # 这个方法可以访问

"""
这种变形的特点：
1.外部无法直接访问到隐藏的
2.类内部可以访问到隐藏的
3.子类无法覆盖父类__开头的属性 （下面举例说明）
"""

# 下面一个继承的例子，当函数加__以后，验证得到结论：func就会变成不一样的名字， 所以Bar就不覆盖Foo的func.
# class Foo():
#     def __func(self):   # -> _Foo__func
#         print("from foo")
#
# class Bar(Foo):
#     def __func(self):   # # -> _Bar__func
#         print("from Bar")


"""
注意的问题1、这种机制也并没有真正意义上限制我们从外部直接访问属性，知道了类名和属性名就可以
            拼出名字：_类名__属性，然后就可以访问了，如a._A__N
2、变形的过程只在类的定义是发生一次,在定义后的赋值操作，不会变形
3、在继承中，父类如果不想让子类覆盖自己的方法，可以将方法定义为私有的
"""

# 验证问题二：

#
# class Foo():
#     def __func(self):   # -> _Foo__func
#         print("from foo")
#
# f = Foo()
# f.__test = "test"
# print(f.__dict__)   #结果发现__test没有变形， 说明外部定义带__不会变形

# 验证问题3：
# 正常情况

class A:
    def fa(self):
        print("from A")
    def test(self):
        self.fa()

class B(A):
    def fa(self):
        print('from B')

b=B()
b.test()   #返回from B


#把fa定义成私有的，即__fa
class A:
    def __fa(self): #在定义时就变形为_A__fa
        print('from A')
    def test(self):
        self.__fa() # 只会与自己所在的类为准,即调用_A__fa

class B(A):
    def __fa(self):
        print('from B')

b=B()
b.test()   #返回 from A