# -*- coding: utf-8 -*-
# 例子：计算圆的周长和面积
import math


class Circle:
    def __init__(self,radius): #圆的半径radius
        self.radius=radius

    @property
    def area(self):
        return math.pi * self.radius**2 #计算面积

    @property
    def perimeter(self):
        return 2*math.pi*self.radius #计算周长

c = Circle(10)
print(c.radius)
# print(c.area())  # # 一般使用函数名（）的方式去访问，但是加入@property会还这样访问报错
print(c.area) # 可以向访问数据属性一样去访问area,会触发一个函数的执行
print(c.perimeter) # 同上

# 解释：一般我们使用函数名（）的方式去访问，加入@property会报错 .此时应该就该像访问属性一样去访问这个函数
# 为什么要这样做呢，因为area可以是圆的一个属性。但是这个属性时算出来的，要算我们需要定义一个函数。但是为了用户调用方便（像属性一样访问），
# 就有了@property这样的解决方案。 所以像让一个函数像属性一样去访问就加上@property

