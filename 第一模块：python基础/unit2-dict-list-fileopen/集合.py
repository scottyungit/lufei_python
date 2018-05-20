#集合
特点：去重   元素是可hash的，无序的
集合存在的意义就是去重复和关系运算
l1={11,22,33}
l2={22,33,44}
交集:
l1.intersection(l2) = l1&l2
并集
l1.union(l2) =  l1|l2
差集
l1.difference(l2)  =  l1-l2
l2.difference(l1)  =  l2-l1
对称差集
l1.symmetric_difference(l2) = l1^l2

包含关系

in,not in：判断某元素是否在集合内
＝＝,！＝:判断两个集合是否相等

两个集合之间一般有三种关系，相交、包含、不相交。在Python中分别用下面的方法判断：

set.isdisjoint(s)：判断两个集合是不是不相交
set.issuperset(s)：判断集合是不是包含其他集合，等同于a>=b
set.issubset(s)：判断集合是不是被其他集合包含，等同于a<=b


集合有可变集合和不可变集合之分
