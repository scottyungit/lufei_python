#41讲：product的练习题
#48讲：最后dict的练习题

#列表
#特点： 1.值是可以重复的，，有序的，可变的，有index,
# 方法:index(),count(),[0:3:2]，
# L=[1,2,3,4,4]
# print(L[0])
# print(L[-1])
#
# #index： value对应的key值
# print(L.index(1))   #--> 0
#
# #统计某个值出现了几次
# print(L.count(4))  #--> 2
#
# #切片
# #取前四个，每两个取一个
# L[0:4:2]

#list一些方法：
# L =[1,2,3,4,4]
# L.append(6) #追加
# L.insert(6,'six')  #插入
# L[0]='first' #修改
# L[1:3]="second"   #注意这里，其实修改了5个值
# print(L)
# #删除
# L.pop() #倒着删除
# L.remove(6) #从左往右删
# del L  #可以删除任何东西
#
# #for 循环
# # for i in  L:
# #     print(i)

#列表是有顺序的  根据索引排序
#如何给列表排序,默认按照Ascii编码表里边的顺序排序
# L.sort()
# #倒排序
# L.reverse()
# #扩展
# L2=[1,3]
# L + L2
# L.extend(L2)
#
#
# #列表的长度l
# len(L)
#
# #把两个列表拼接到一起
# L + L2
# name=["scott1","scott2","scott3"]
#
# id() #显示内存地址

#n2=names ,names中元素发生变化时，n2会怎么样？
# 解释：names列表本身有一个内存地址，列表里边的每个值又都有一个内存地址，表示独立个体
# 当n2=names，表示： n2指向names的内存地址。所以当names的某个元素变化时，names这个列表的内存地址不会变，所以n2和names还是会相等。
# 当n3=names.copy()，这是浅copy,这是n3会有一个新的内存地址，但是里边的元素还是names那一份元素，相当与共享元素。 这时如果改一个names的元素值，
# n3和names就不一样了，因为相当于names重新换了一个独立个体，而n3还用原来的那个个体。 去检查个体的内存地址也会不一样。
# name2里边嵌套子列表时，情况又是怎么样呢？其他元素会变，子列表不会变。
#
# 注意copy只是copy了一个新的list的内存地址。但是里边的元素和原来的元素共享空间，并没有产生新的元素。
# 深copy：与浅copy的区别啥情况下有区别呢？ 在list里嵌套子list时
# 浅copy对子list不起作用，修改之后不变
# 深copy是完全clone一份，包括子list，
# 深copy一般不用，必须import deepcopy模块才能用
# n3=names.deepcopy()


#
#
#
# 数据类型:元祖
# 功能:
# index
# 切片
# count
#
#
#
# dict字典:
# 特点：
# key:value结构
# 无序的
# key必须是hash的，是不可变的
# 查找速度快

d={'scott':1,'scott2':2,'leijie':[24, 'Software engineer']}
print(d.get("scott", "no_value"))
# #删除 dict.pop(key)    dict.popitem()自动删  del dict['scott']
# 扩展，两个dict相加    dict1.update(dict2)
# #返回为列表  dict.items()
# 只有值 dict.values()
# 只有key dict.keys()
# dict.setdefault()   dict.setdefault('test','test_value') 指：如果有test这个key，就返回value，如果没有，就设置。
#
d.popitem()
print(d.items)