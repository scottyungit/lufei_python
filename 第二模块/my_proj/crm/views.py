#coding=utf-8
import os,sys
#sys.path.append("C:\lufei_python\第二模块\my_proj")
print(dir())
print(__file__)  ##返回相对路径
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)) ) #返回相对路径所在的文件夹
#BASE_DIR=os.path.abspath(BASE_DIR)
print(BASE_DIR)
sys.path.append(BASE_DIR)
print(sys.path)
from  proj  import settings
#print(sys.path)

def sayhi():
    print("hello,world")
