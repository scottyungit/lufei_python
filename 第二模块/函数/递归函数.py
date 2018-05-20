# encoding:utf-8
def calc(n,count):
    print(n,count)
    if count<5:
        return calc(n/2,count+1)
    else:
        return n

res=calc(188,1)
print(res)

#递归函数可以循环下去，在退出时再一层一层退出.
#会受到栈的限制，默认栈为1000，当循环次数过多，会栈溢出

#