#!/usr/bin/env python
# -*- coding:gbk -*-
# s="路飞"
# print(type(s))
# print(s)
# s2 = s.decode("utf-8")
# print(type(s2))
# print(s2)
#
# print(s,s2)

# # -*- coding: utf-8 -*-
# import sys
# print(sys.getdefaultencoding())
# print(sys.getfilesystemencoding())
#
# f=open()


import codecs
import locale
print(locale.getpreferredencoding())

# f = open('test.txt','a')
# f.write('中文')
# f.close()

# s = '中文'
# print(type(s))
# s2 = s.decode('utf-8')
# s3=s2.encode('utf-8')
# f.write(s3)
# f.close()
#
f = open('test.txt','r')
s = f.readlines()
f.close()
for line in s:
    print(line)
