# # str
# ###字符串类型：
# 字符串的特点：有序的，不可变的
# s.count('h') ## h出现了几次
# #格式化
s = "my name's {0},I'm {1} year old"
print(s.format('scott', 22))
print(s)
# 或者
# s="my name's {name},I'm {age} year old"
# s3.format(name='scott',age=22)
# s3.isidentifier() ##是不是一个合法的变量名
#
# 从列表变成一个字符串（拼接）
# L=[1,2,3,]
# s='_'.join(L)
# 从字符串分割为列表（分割）
# s='hello_world'
# L=s.split('_')
#
# 字符串s的方法:
s="hello"
s.upper()
print(s.center(20,"*"))
# count
# replace
# isdigit
# find
# format()
# split
# center
# strip