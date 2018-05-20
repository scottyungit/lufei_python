
#加入__init__方法，是为了定制类的每个实例化对象自己的属性 。

class LuffStudent:
    school = "luffycity"   # 类的数据属性

    def __init__(self,name,sex,age):
        self.Name = name
        self.Sex = sex
        self.Age = age


    def learn(self):    # 类的函数属性
        print("is learning")

    def eat(self):
        print("is eating")


# 加入了__init__以后，
stu1 = LuffStudent("scott1","boy",25)
# 此时stu1不光有了类的属性，还有了自己独特的属性，其实上面的语句做了两个事情
# 1.创建了stu1空对象
# 2.执行了init方法 此时self就已经是stu1了

print(stu1.__dict__)   # 返回了stu1自己的属性 {'Name': 'scott1', 'Sex': 'boy', 'Age': 25}

# 对stu1这个实例化对象进行增删改查
print(stu1.Name)

stu1.Age = 26
print(stu1.Age)

stu1.hobby = "sport"
print(stu1.hobby)

del stu1.hobby
# ---

