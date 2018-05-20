#!/usr/bin/env python
#-*- coding:utf-8 -*-

#第一次，位置参数 positional arguments
# import argparse
#
# parser = argparse.ArgumentParser()
# parser.add_argument("echo")
# args = parser.parse_args()
# print(args.echo)


#第二次   可选参数，optional arguments  。
#命令行调用语句  python 此脚本名  -v 1
# import argparse
# parser=argparse.ArgumentParser()
# parser.add_argument("-v","--verbosity",help="increase output verbosity")
# args=parser.parse_args()
# print(args.verbosity)    # -v后边的参数会传入这个变量
# if args.verbosity:
#     print("verbosity turned on")

#第三次调用  可选参数可以不输入值，指定默认值
# import argparse
# parser=argparse.ArgumentParser()
# parser.add_argument("-v","--verbosity",help="increase output verbosity",action="store_true")
# args=parser.parse_args()
# print(args.verbosity)    # 这个值为True 或 False
# if args.verbosity:
#     print("verbosity turned on")

#第四次测试，参数值的类型默认都是str。如果想传入一个int数字，就需要转换
# import argparse
#
# parser = argparse.ArgumentParser()
# parser.add_argument('x',type=int,help="the base")
# args = parser.parse_args()
# answer = args.x ** 2
# print(answer)

#choice=[] ，上边测试x可以有任意数，但是我想给x限定只有某几个数可以选择：0，1，2
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-v',"--versibity",type=int,help="the base",choices=[0,1,2])
args = parser.parse_args()
answer = args.versibity ** 2
print(answer)