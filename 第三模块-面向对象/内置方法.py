#
# class People:
#     pass
# class Student(People):
#     def __init__(self,name):
#         self.name=name
#     pass
#
# print(Student.__dict__)
# stu1=Student('scott1')
# print(isinstance(stu1,Student))
# print(issubclass(Student,People))
# print(stu1)
#

# 类中的items系列的内置方法：__getitem__()   __setitem__()  __delitem__()
# 之前说过__开头结尾的方法不要自己去调用，python会自己调用。所以要知道什么时候它会自己调用，下面例子测试

# class Foo:
#     def __init__(self,name):
#         self.name = name
#
#     def __getitem__(self, item):
#         return self.__dict__.get(item)
#
#     def __setitem__(self, key, value):
#         self.__dict__[key] = value
#
#     def __delitem__(self, key):
#         self.__dict__.pop(key)
#
#
# f=Foo("scott")
# print(f.__dict__)
# # 查看某属性的值：现在多了一种方法，像字典一样通过key访问，下例子：
# print(f['name'])  #验证了：当这样时f['name'] 触发getitem
# # 设置属性
# f['name'] = "scott2"  #验证了：当这样时f['name'] = "scott2"   触发setitem
# print(f['name'])
# # 删除属性
# del f['name']   # 验证了：当这样时f['name'] = "scott2"   触发setitem
# print(f['name'])


# 其他内置方法
# __str__()
class Student:
    def __init__(self,name):
        self.name=name

    def __str__(self):
        return '"name":%s' % self.name

stu1=Student("leijie")
print(stu1)


# __del__() :在程序运行结束后，自己执行这里定义的代码
# class Open:
#     def __init__(self,filename):
#         print("open file..")
#         self.filename=filename
#     def __del__(self):
#         print("close file...")
#
# f=Open("setting.py")
# print("test")
