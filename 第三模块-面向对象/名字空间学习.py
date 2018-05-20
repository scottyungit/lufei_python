#!/usr/bin/env python
# -*-coding: utf-8 -*-

# 例子1


# def func1():
#     x = 1
#     #print globals()
#     print 'before func1:', locals()
#
#     def func2():
#         a = 1
#         print 'before fun2:', locals()
#         a += x
#         print 'after fun2:', locals()
#
#     func2()
#     print 'after func1:', locals()
#     #print globals()
#
# if __name__ == '__main__':
#     func1()

# 例子2


# def func1():
#     x = 1
#     print 'before func1:', locals()
#
#     def func2():
#         print 'before fun2:', locals()
#         x = x + x  #就是这里使用x其余地方不变
#         print 'after fun2:', locals()
#
#     func2()
#     print 'after func1:', locals()
#
# if __name__ == '__main__':
#     func1()

def func():
    if False:
        x = 10 #该语句永远不执行
    print x

func()















