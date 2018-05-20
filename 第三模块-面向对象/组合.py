# -*- coding: utf-8 -*-


class  Teacher:
    def __init__(self,name):
        self.name=name

class Student:
    def __init__(self,name):
        self.name=name


teacher1 = Teacher("alex")
stu1 = Student("scott1")

# 需求： 现在想有一个课程的角色，让学生可以上python课，老师也可以教python课程
# 分析： 那我们可以给teacher一个课程的属性。但是这个每个对象都要传课程的值，比较麻烦。为何不用写一个课程的class，然后让老师和学生继承。
# 这样是不行的。因为继承的定义原则是“什么是什么” 例如学生是人。那么学生类可以继承人的类。老师和课程不属于老师属于课程的关系。而是老师有课程，
# 这个有点像属性的定义。所以方案就是我定义一个课程的Class。然后给老师定义一个课程属性，课程属性指向课程class。即可

#需求实现代码：
class  Teacher:
    def __init__(self,name):
        self.name=name

class Student:
    def __init__(self,name):
        self.name=name

class course:
    def __init__(self, name, price):
        self.name = name
        self.price = price


teacher1 = Teacher("alex")
stu1 = Student("scott1")

python = course("python", 10000)
# 老师的课程属性
teacher1.course = python
# 学生的课程属性
stu1.cource = python
# 访问学生的课程
print(stu1.cource.name)