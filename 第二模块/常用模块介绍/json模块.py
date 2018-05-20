#-*- coding: utf-8 -*-
import json
# data={
#     "roles":[
#         {"roles":'monster',"type":"pig","life":50},
#         {"roles":"hero","type":"关羽","life":"80"}
#     ]
#
# #使用json.dump()将dict存到文件中，json.dump()需要跟一个文件对象，所以需要下面这几句打开文件的操作。f就是一个文件对象
# f=open("test.json","w")
# json.dump(data,f)   ##json 可以dump好几次，但最好不要dump好多次。后边就append到文件中，但是不会自动换行
f=open("test.json","r")
data=json.load(f)
print("load data:",data)

str=json.dumps(data) #只是转成字符串,
#print(type(d)) #是字符串
d2=json.loads(str) ##json.loads()从字符串在转为dict
print("loads:",d2)

#json
#1.json定义了不同语言之间的交互规则

aa=json.dumps(data)
print("111",aa)