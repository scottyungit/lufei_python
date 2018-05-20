#coding=utf8
# all(Iterable) #如果迭代对象中的每一个值，返回true，all（）就返回true.  Iterable为空也会返回true
# any(Iterable) #跟all相反，迭代对象中只有一个元素值是true，就返回true
#dir()  #打印当前程序的所有变量
# hex()  #返回一个数的16进制
# sorted() #排序   关键参数 key ,reverse
# bin()  #转2进制
# eval() #按照解释器把str转为代码语法 ，但是只能处理单行代码， 有return 返回值
f="1+2+3"
print(eval(f))   #eval把f这个字符串转为python能看懂的语法

# exec() #可以执行多行str，  不可以return返回值
# ord() 和chr() #都是字符和ascii编码表的映射返回值
print(ord('a'))  #把返回ascii表中的值
print(chr(97))   #97对应“a”  和ord相反



def foo():
    print("run foo")
    return 134
res=foo()
print(res)
