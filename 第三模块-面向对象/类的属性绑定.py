class LuffStudent:
    school = "luffycity"   # 类的数据属性

    def __init__(self,name,sex,age):
        self.Name = name
        self.Sex = sex
        self.Age = age


    def learn(self):    # 类的函数属性
        print("%s is learning" % self.Name)

    def eat(self):
        print("is eating")


stu1 = LuffStudent("scott1","boy",25)
stu2 = LuffStudent("scott2","girl",25)
# 总结：类的数据属性和对象的数据属性都用了同一块内存地址
# 验证:对象相同的属性都放在类里边
print(LuffStudent.school,id(LuffStudent.school))
print(stu1.school,id(stu1.school))
print(stu2.school,id(stu2.school))

# 类的函数属性：绑定给对象的
print(LuffStudent.learn)
print(stu1.learn)
print(stu2.learn)
# 总结 数据属性内存地址一样，对象的绑定函数属性内存地址不一样

# 类调用函数属性
#LuffStudent.learn()   #类自己调用自己的函数属性， self不会自己传进来，手工传入
LuffStudent.learn(stu1)
# 对象调用自己的绑定函数属性
stu1.learn()  # 会自动传入self
stu2.learn()

# 当对象自己有一个属性，Class也有一个相同的属性，那哪个会优先生效呢？是对象自己
stu1.aa = "from stu1"
LuffStudent.aa = "from LuffStudent class"
print(stu1.aa)    #实验证明是从对象找，