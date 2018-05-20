# # encoding: utf-8
# str='123'
# li = ["alex","eric","rain"]
# new_str = '_'.join(li)
# print(new_str)
# #list1
# li = ("alec", " aric", "Alex", "Tony", "rain")
# new_li=[]
# for element  in li:
#     new_element=element.strip()
#     if new_element.startswith(('a','A')) and new_element.endswith('c'):
#         print(new_element)
#
# #dict1
# dic = {'k1': "alex", 'k2': ' aric', "k3": "Alex", "k4": "Tony"}
# #print(dic.values())
# for element in dic.values():
#     new_element = element.strip()
#     if new_element.startswith(('a','A')) and new_element.endswith('c'):
#         print(new_element)
#
# #列表功能练习
# li=['alex','eric','rain']
# print(len(li))
# li.append('seven');print(li)
# li.insert(0,'Tony');print(li)
# li[1] = 'Kelly';print(li)
# li.remove('eric');print(li)
# print(li.pop(1))
# print(li)
# li.pop(2)
# print(li)
li = ['Tony', 'Kelly', 'eric', 'rain', 'seven']
del li[1:4]
print(li)
#？ print(li.pop([1,2,3]))

# li = ['Tony', 'Kelly', 'eric', 'rain', 'seven']
# li.reverse()
# print(li)
# for i in range(len(li)):
#     print(i)
#
# for i in enumerate(li,100):
#     print(i)
# for i in li:
#     print(i)

##4.
# li = ["hello", 'seven', ["mon", ["h", "kelly"], 'all'], 123, 446]
# print(li[2][1][1])
# li[2][2]='ALL'
# print(li)
#
# ##5.元祖：
# tu = ('alex', 'eric', 'rain')
# print(len(tu))
# print(tu[1])
# print(tu[:2])
#
# #6.
# tu = ("alex", [11, 22, {"k1": 'v1', "k2": ["age", "name"], "k3": (11,22,33)}, 44])
# '''
# 元祖的特性:元素无法修改，具有唯一性
# '''
# tu[1][2]["k2"].append('seven')
# print(tu)
#
# #7.dict
# dic = {'k1': "v1", "k2": "v2", "k3": [11,22,33]}
# for k in dic.keys():
#     print(k)
# for v in dic.values():
#     print(v)
# for k,v in dic.items():
#     print(k,v)
#
# dic['k4']='v4'
# print(dic)
# dic['k1']='alex'
# print(dic)
# dic['k3'].insert(0,19)
# print(dic)
# list.insert
#
# #8.转换
# s='alex'
# s=tuple(s)
# print(type(s))
# print(s)
# li = ["alex", "seven"]
# li=tuple(li)
# print(li)
#
    # tuple = ["Alex", "seven"]
    # tuple=list(tuple)
# print(tuple)

##?????????将列表li = ["alex", "seven"]转换成字典且字典的key按照10开始向后递增
li = ["alex", "seven"]
d=dict(enumerate(li,10))
print(d)

#将所有大于66的值保存至字典的第一个key中，将小于66的值保存至第二个key的值中。
l={11,22,33,44,55,66,77,88,99,90}
l1=[]
l2=[]
d={}
for i in l:
    if i>66:
     l1.append(i)
    if i<66:
     l2.append(i)
d['k1']=l1
d['k2']=l2
print(d)

# li = ["手机", "电脑", '鼠标垫', '游艇']
# shopping_car=[]
#
# while True:
#     n=int(input('please enter the sequence you want:'))
#     print(li[n-1])
#     shopping_car.append(li[n-1])
#     print(shopping_car)


l1=[11,22,33]
l2=[22,33,44]
l1_l2=[]
for i in l1:
    if i in l2:
        l1_l2.append(i)
print(l1_l2)

#13.
l1={11,22,33}
l2={22,33,44}
l1_l2=l1&l2
l1_not_l2=l1.difference(l2)
l2_not_l1=l2.difference(l1)
l1_different_l2=l1^l2
print(l1-l2)
print(l2_not_l1)
print(l1_different_l2)

#14.
# l=list(range(101))
# l.reverse()
# print(l)
# for i in l:
#     print(i,end=' ')

#打印9X9乘法表
for i in range(1,10):
    for j in range(1,10):
        if j<=i:
            if j*i<10:
                print(str(j)+"X"+str(i)+"="+str(j*i),end='  ')
            else:
                print(str(j)+"X"+str(i)+"="+str(j*i),end=' ')
    print()
#
