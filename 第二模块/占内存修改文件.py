# -*- coding: utf-8 -*-
f_name = '文件2.txt'
f = open(f_name,'r+')
ss = f.read()
ss = ss.replace("你好", "hello")
print(ss)
f.seek(0)
f.truncate()
f.write(ss)
f.close()
