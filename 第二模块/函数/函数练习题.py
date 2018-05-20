#encoding: utf-8
def calculate(*numbers):
    print(sum(numbers))

calculate(3,4,5)


def modify_file(filename,old_str,new_str):
    f = open(filename, 'r+')
    s = f.read()
    s = s.replace(old_str, new_str)
    f.seek(0)
    f.truncate()
    f.write(s)
    f.close()


def modify_file2(filename,old_str,new_str):
    import os
    f=open(filename,'r')
    f2=open(filename+".new",'w')
    s=f.read()
    s=s.replace(old_str,new_str)
    s2=f2.write(s)
    f.close()
    f2.close()
    os.remove(filename)
    os.replace(filename+".new",filename)

modify_file2('准备修改的文件2',"hello",'你好吗')


modify_file('准备修改的文件','你好',"hello")

def check_null(*objectname):
    if len(objectname)==0:
        print("传入的对象中没有任何元素")
    else:
        value=all(objectname)
        if value==False:
            print("传入的对象中有空元素")

check_null(1,'',3)  #利用了可变参数


#4.保留value长度为2
dic = {"k1": "v1v1", "k2": [11,22,33,44]}
# print(dic["k2"][:2])
# print(dic.values())
def value2(dic):
    for k,v in dic.items():
        if len(v)>2:
            dic[k]=v[:2]

dic = {"k1": "v1v1", "k2": [11,22,33,44]}
value2(dic)
print(dic)

#计算图形面积
from math import pi
def area(xingzhuang,*value):
    def 计算长方形的面积(value):
        mianji=value[0]*value[1]
        print("长方形面积是: "+str(mianji))
    def 计算正方形面积(value):
        mianji=value[0]**2
        print("正方形面积是："+str(mianji))
    def 计算圆形面积(value):
        mianji=pi*value[0]**2
        print("圆形面积是："+str(mianji))
    if xingzhuang=="长方形":
        计算长方形的面积(value)
    if xingzhuang=="正方形":
        计算正方形面积(value)
    if xingzhuang=="圆形":
        计算圆形面积(value)

area("长方形",15,20)
area("正方形",5)
area("圆形",5)


###函数进阶
#扑克牌列表
def cards():
    card_number=list(range(1,11))+["J","Q","K","A"]
    print(card_number)
    card_type=["红心","黑桃","方片","梅花"]
    card_list=[]
    for i in card_number:
        for t in card_type:
            card_list+=((t,i),)
    print(card_list)

cards()

#2.内置方法max和min
def min_max(*numbers):
    d={}
    min_number=min(numbers)
    max_number=max(numbers)
    d['max']=max_number
    d['min']=min_number
    print(d)

min_max(2,3,4,5)

#内置函数：
#3. 计算面积
name=['alex','wupeiqi','yuanhao','nezha']
name=list(map(lambda x:x+"_sb",name))
print(name)
##内置方法函数 filter 取出列表中的偶数
num=[1,3,5,6,7,8]
num=list(filter(lambda x:x%2==0,num))
print(num)

#4.普通函数求n的阶乘
def cal(num):
    ji=1
    while num>0:
        ji*=num
        num=num-1
    print(ji)
cal(5)
#递归函数做阶乘
def recursion(num):
    if num==1:
        return num
    return num*recursion(num-1)
print(recursion(5))

