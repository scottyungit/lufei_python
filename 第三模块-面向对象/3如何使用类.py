class LuffStudent:
    school = "luffycity"   # 类的数据属性

    def learn(self):    # 类的函数属性
        print("is learning")

    def eat(self):
        print("is eating")

# 雷和函数的区别：
# 类定义好之后，就相当于已经执行了一遍，这一点于函数不同，函数实在定义之后，调用才会执行.


# class的使用：
# 查看类的命令空间.
print(LuffStudent.__dict__)  # 定义好之后把class的内容存入到一个dict之后，所以通过__dict__来查看
print(LuffStudent.__dict__['learn'])   # 查看函数
# 查看
print(LuffStudent.learn)   # 和上边的返回一样
# 增加
LuffStudent.country = "china"
print(LuffStudent.country)
# 删除
del LuffStudent.country
# 改
LuffStudent.school="Luffycity"
print(LuffStudent.school)


# Class的另外一种用法
# class名字加()会实例化对象 函数加()确实执行函数 这点是class和function的区别
leijie=LuffStudent()
print(leijie.school)