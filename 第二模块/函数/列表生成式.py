a=list(range(10))
print(a)
aa=[ i*i if i<5 else i for i in a ]   #注意列表生成式的写法  ，if语句应该在哪里写
print(aa)