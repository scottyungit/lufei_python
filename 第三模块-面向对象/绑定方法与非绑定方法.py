# -*- coding: utf-8 -*-
# 在类中定义方法可以有这么几种选择：
# 1、绑定方法  绑定给谁，谁来调用就自动将它本身当作第一个参数传入
#   1.1 绑定到对象： 没有被任何装饰器装饰的方法。  对象.boud\_method\(\),自动将对象当作第一个参数传入
#   1.2 绑定到类：  用classmethod装饰器装饰的方法。  类.boud\_method\(\),自动将类当作第一个参数传入
#
# 2、非绑定方法： 用staticmethod装饰器装饰的方法
# 不与类或对象绑定，即类和对象都可以调用，但是没有自动传值那么一说。

# 例子： 如何使用绑定类方法
# import setting
#
#
# class MySQL:
#     def __init__(self, host, port):
#         self.host = host
#         self.port = port
#
#     @classmethod
#     def from_conf(cls):
#         print(cls)
#         return cls(setting.HOST, setting.PORT)
#
#
#
# print(MySQL.from_conf) #<bound method MySQL.from_conf of <class '__main__.MySQL'>>
# conn = MySQL.from_conf()
# conn.from_conf() #对象也可以调用，但是默认传的第一个参数仍然是类
# 这里为什么使用绑定类方法这种思路来写代码呢？
# 因为host和port写在一个setting文件中，又不想对象conn连接时自己去传入host 和 port.所以需要些一个方法，内容就是读取setting文件。
# 然后return一个对象.想return一个对象代码必须要写类名。当然我们可以直接写MYSQL这个类名，但是如果定义的类名变了，那函数也跟着变化，所以
# 使用绑定类的方法较好，cls就可以被自动传入类名。

# 例子： 如何使用非绑定方法
import hashlib
import time


class MySQL:
    def __init__(self,host,port):
        self.id=self.create_id()
        self.host=host
        self.port=port
    @staticmethod
    def create_id(): #就是一个普通工具
        m=hashlib.md5(str(time.time()).encode('utf-8'))
        return m.hexdigest()

print(MySQL.create_id) #<function MySQL.create_id at 0x0000000001E6B9D8> #查看结果为普通函数
conn=MySQL('127.0.0.1',3306)
print(conn.create_id) #<function MySQL.create_id at 0x00000000026FB9D8> #查看结果为普通函数

# 这个例子是说给每一个连接设置一个唯一的id，id使用hash算出来的（确保唯一）.因为后边写函数时，貌似完全不care类名和对象。既然不依赖他们，所以
# 采取非绑定方法去做比较好


