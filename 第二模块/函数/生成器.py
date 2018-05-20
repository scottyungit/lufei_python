#coding=utf-8

#列表生成式和生成器的区别 ，列表生成器已经将每个元素生成，占用了内存。生成器是在调用的时候才会生成元素。
#在函数中写上yield 当执行函数时，遇到yield就会中止在此，下次next()时，再次继续执行。
#有yield的函数 就会变成一个生成器。
#两种方法写一个生成器：
#1.类似列表生成式的方法，把[]变成了()
a=(x*x for x in range(10))
print(a)
print(next(a))
print(next(a))
print(next(a))
#2.函数的方法
def fib(max):
    n,a,b=0,0,1   #同时赋予三个变量的值
    while  n<max:
        yield b   #有了yield此函数就会变成生成器，遇到yield就会中止在此 并返回yield 后边的值，下次next()时，再次继续执行
        a,b=b,a+b
        n+=1
    return "done"

f=fib(6)
print(next(f))
print(next(f))
print(next(f))

函数有了yield之后，
1.return在生成器里，就不会生效了，会报错

next(f) #唤醒生成器继续运行
f.send()
1.唤醒并继续运行
2.发送一个信息给生成器内部

iter() #把一个可迭代对象变成迭代器

