# -*- coding:utf-8 -*-

class ParentClass:
    pass


class SubClass(ParentClass):
    camp = "personal"
    pass

# 打印出子类继承哪个类
print(SubClass.__bases__)

# 总结： 在继承属性时，先找对象自己 -->Class -->ParentClass，


# 多继承
#print(SubClass.mro())   # 默认有个mro方法,可以帮你统计出继承的顺序
#到底是怎么一个原理呢？
#python2中的多继承
#经典类：没有继承object类  深度优先
#新式类：继承object类， 广度优先原则

#python3中的多继承
#新式类：不管写不写，都继承object类， 广度优先原则

#测试一下
class A:
    def test(self):
        print("from A")

class B(A):
     # def test(self):
     #     print("from B")
     pass
class C(A):
    def test(self):
        print("from C")

class D(B):
     # def test(self):
     #     print("from D")
     pass
class E(C):
    def test(self):
        print("from E")

class F(D,E):
    # def test(self):
    #     print("from F")
    pass
f=F()
#print(F.__mro__)   # f所在类有个mro方法或者__mro__属性都能看出顺序
# 按照广度优先原则继承顺序应该是：F->D->B->E->C->A，通过注释test进行测试
f.test()
