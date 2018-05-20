# 封装数据属性： 明确区分内外
# 装函数属性：隔离复杂度，藏一些不重要的函数方法，加上__
# class People():
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     # 通过定义此方法，让对象间接访问了隐藏属性
#     def tell_info(self):
#         print("Name:%s Age:%s" %(self.__name,self.__age))
#
#     # 通过定义此方法，防止对象在外部随便修改属性，通过函数可以加一些判断。
#     def set_info(self, name, age):
#         if not isinstance(name,str):
#             print("name must be str type")
#             return
#         if not isinstance(age,int):
#             print("age must a int type")
#             return
#         self.__name = name
#         self.__age = age
#
# p=People("scott",25)
# p.tell_info()
# p.set_info("new name",27)
# p.tell_info()


# 验证封装方法为什么能隔离复杂度
class ATM:
    def __card(self):
        print("插卡")
    def __auth(self):
        print("认证")
    def __input_amount(self):
        print("输入取款金额")
    def __get_money(self):
        print("拿钱")
    def withdraw(self):
        self.__card()
        self.__auth()
        self.__input_amount()
        self.__get_money()

a=ATM()
a.withdraw()  #用户只需要执行withdraw取钱就行，不用关心细节操作

"""
封装意义总结:
1：封装数据
将数据隐藏起来这不是目的。隐藏起来然后对外提供操作该数据的接口，然后我们可以在接口附加上对该数据操作的限制，
以此完成对数据属性操作的严格控制。
2：封装方法：目的是隔离复杂度
#取款是功能,而这个功能有很多功能组成:插卡、密码认证、输入金额、打印账单、取钱
#对使用者来说,只需要知道取款这个功能即可,其余功能我们都可以隐藏起来,很明显这么做
#隔离了复杂度,同时也提升了安全性
3.使用property
将一个类的函数定义成特性以后，对象再去使用的时候obj.name,根本无法察觉自己的name是执行了一个函数然后计算出来的，
这种特性的使用方式遵循了统一访问的原则
封装与扩展性
封装在于明确区分内外，使得类实现者可以修改封装内的东西而不影响外部调用者的代码；而外部使用用者只知道一个接口(函数)，
只要接口（函数）名、参数不变，使用者的代码永远无需改变。这就提供一个良好的合作基础——或者说，
只要接口这个基础约定不变，则代码改变不足为虑。
"""

