import re
str1='imooc video=1000'
print(str1.find('1'))

#re的一些方法 re.S 可以匹配多行，其实是能匹配换行符，这样就匹配多行了
str = "a23b\na34b"  #\n是换行符，难点就是怎么能匹配多行，在多行里找到想要的结果
#预期结果是，匹配23，34并返回
re.findall(r"a(\d+)b.+a(\d+)b", str)
#输出[]
#因为不能处理str中间有\n换行的情况

re.findall(r"a(\d+)b.+a(\d+)b", str, re.S)
#s输出[('23', '34')]

#re.M可以可以将会匹配每一行，其实是将^$匹配了，达到匹配多行的效果。默认^$只匹配每一行
str = "a23b\na34b"

re.findall(r"^a(\d+)b", str)
#输出['23']

re.findall(r"^a(\d+)b", str, re.M)
#输出['23', '34']