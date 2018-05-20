# 子类重用：默认子类Gawen有attack方法，不从父类继承。但是现在的需求是：想让子类继承父类的函数，但是又想使用子类的函数。相当于重用
# 方式1：指名道姓法 (不继承父类)

# 实现1： 函数属性的重用
# 需求：让子类Gawen的attack函数既能继承父类的attack，同时有他自己的attack定义的一些东西
# class Hero:
#     def __init__(self, nickname, life_value, aggressivity):
#         self.nickname = nickname
#         self.life_value = life_value
#         self.aggressivity = aggressivity
#
#     def attrack(self, enemy):
#         enemy.life_value -= self.aggressivity
#
# class Gawen(Hero):
#     """ 对每个英雄定义自己的类"""
#     # 每个英雄都有自己的阵营，
#     camp = "Beijing"
#
#     def attrack(self, enemy):
#         Hero.attrack(self, enemy)   #加上这句，指名道姓说要使用父类，但是这个其实不是继承下来的，而是自己去找的，相当于一个普通的函数调用
#         print("From Gawen Class")
#
# class Riwen(Hero):
#     camp = "Shanghai"
#
#     def attrack(self, enemy):
#         print("From Riwen Class")
#
#
# g1 = Gawen("草丛伦", 100, 30)
# r1 = Riwen("雯雯", 80, 50)
# print(r1.life_value)
# g1.attrack(r1)   #此时会做两件事：attack 和 print
# print(r1.life_value)

# 实现2： 属性的重用（init方法）：
# 需求：需要给Gawen添加一个weapon属性，尽量减少代码

# class Hero:
#     def __init__(self, nickname, life_value, aggressivity):
#         self.nickname = nickname
#         self.life_value = life_value
#         self.aggressivity = aggressivity
#
#     def attrack(self, enemy):
#         enemy.life_value -= self.aggressivity
#
# class Gawen(Hero):
#     """ 对每个英雄定义自己的类"""
#     # 每个英雄都有自己的阵营，
#     camp = "Beijing"
#
#     # 加了weapon的属性
#     def __init__(self, nickname, life_value, aggressivity, weapon):
#         # self.nickname = nickname
#         # self.life_value = life_value
#         # self.aggressivity = aggressivity
#         Hero.__init__(self,nickname,life_value,aggressivity)
#         self.weapon = weapon
#
#     def attrack(self, enemy):
#         Hero.attrack(self, enemy)   #加上这句，指名道姓说要使用父类，但是这个其实不是继承下来的，而是自己去找的，相当于一个普通的函数调用
#         print("From Gawen Class")
#
# class Riwen(Hero):
#     camp = "Shanghai"
#
#     def attrack(self, enemy):
#         print("From Riwen Class")
#
# #调用时加入了weapon的属性值
# g1 = Gawen("草丛伦", 100, 30, "knife")
# r1 = Riwen("雯雯", 80, 50)
# print(r1.life_value)
# g1.attrack(r1)   #此时会做两件事：attack 和 print
# print(r1.life_value)

# 方式二：super() 这种方式会继承父类
# 需求：1. 让子类Gawen的attack函数既能继承父类的attack，同时有他自己的attack定义的一些东西
#      2. 添加weapon属性给Gawen对象
class Hero:

    def __init__(self, nickname, life_value, aggressivity):
        self.nickname = nickname
        self.life_value = life_value
        self.aggressivity = aggressivity

    def attrack(self, enemy):
        enemy.life_value -= self.aggressivity

class Gawen(Hero):
    """ 对每个英雄定义自己的类"""
    # 每个英雄都有自己的阵营，
    camp = "Beijing"

    def __init__(self, nickname, life_value, aggressivity, weapon):
        # self.nickname = nickname
        # self.life_value = life_value
        # self.aggressivity = aggressivity
        #这里用了super函数 ，super()会实例化出一个特殊的对象(对象不用传self),所以后边调用init函数时时self没有传进来
        super(Gawen, self).__init__(nickname,life_value,aggressivity)   # super() == super(Gawen,self)
        self.weapon = weapon

    def attrack(self, enemy):
        super().attrack(enemy)
        print("From Gawen Class")

class Riwen(Hero):
    camp = "Shanghai"

    def attrack(self, enemy):
        print("From Riwen Class")


g1 = Gawen("草丛伦", 100, 30, 'knife')
r1 = Riwen("雯雯", 80, 50)
print(r1.life_value)
g1.attrack(r1)   #此时会做两件事：attack 和 print
print(r1.life_value)

# 补充： super()在使用时，
# Python2中  super(当前类名，self)，本例子时 super(Gawen,self)
# python3中，super() 不用传参