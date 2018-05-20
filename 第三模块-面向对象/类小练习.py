# -*-coding: utf-8 -*-
# 题目：写一个学生类,要求有一个计数器，能记录总共实例化了多少对象


class LuffStudent:
    school = "luffycity"   # 类的数据属性
    # 计数器变量
    count = 0

    def __init__(self,name,sex,age):
        self.Name = name
        self.Sex = sex
        self.Age = age
        # 使用self也可以,但是count永远都是1
        self.count=self.count + 1
        # 所以必须调用类的count属性，才能增加
        LuffStudent.count += 1

    def learn(self):    # 类的函数属性
        print("%s is learning" % self.Name)

    def eat(self):
        print("is eating")

# 思路：怎么知道实例化对象呢，以为每次实例化都会触发__init__方法，所以在此方法中加点东西
# 能统计所有对象，所以应该有一个类的变量，而不是实例的变量
stu1 = LuffStudent("scott1", "boy", 25)
stu2 = LuffStudent("scott2", "girl", 25)
# 查看结果
print(LuffStudent.count)


# 题目2: 写两个英雄联盟的英雄类，让其互相攻击，打印出对方的生命值
class Gawen:
    def __init__(self, nickname, life_value, aggressivity):
        self.nickname = nickname
        self.life_value = life_value
        self.aggressivity = aggressivity

    def attrack(self, enemy):   # enemy传入r1
        enemy.life_value -= self.aggressivity  # 等于 r1.life_value-=g1.aggressivity

class Riwen:
    def __init__(self, nickname, life_value, aggressivity):
        self.nickname = nickname
        self.life_value = life_value
        self.aggressivity = aggressivity

    def attrack(self, enemy):
        enemy.life_value -= self.aggressivity


g1 = Gawen("草丛伦", 100, 30)
r1 = Riwen("雯雯", 80, 50)
g1.attrack(r1)
print("first", r1.life_value)

# 题目2的类代码可以优化，由于很多代码重复，可以使用父类继承


class Hero:
    def __init__(self, nickname, life_value, aggressivity):
        self.nickname = nickname
        self.life_value = life_value
        self.aggressivity = aggressivity

    def attrack(self, enemy):
        enemy.life_value -= self.aggressivity

class Gawen(Hero):
    """ 对Gawen英雄定义自己的类"""
    # 每个英雄都有自己的阵营，
    camp = "Beijing"

class Riwen(Hero):
    """ 对Riwen英雄定义自己的类"""
    camp = "Shanghai"

# 验证：使用父类继承的方法也能成功
g1 = Gawen("草丛伦", 100, 30)
r1 = Riwen("雯雯", 80, 50)
g1.attrack(r1)
print("Sencond", r1.life_value)