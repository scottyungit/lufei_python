import shelve


##总结： shelve也可以作为一个序列化的模块，也是一个python独有的模块， 比pickle较好一点。因为他可以多次添加数据到文件中
#pickle和json都是一次性dump到文件中，再dump时选择别的文件了。
#下面的例子将names这个list写到shelve_test这个文件，会生成一个类似db结尾的文件，可以继续加数据。类似key-value的结构。
#相当于每次存数据key是一个记号，记住了这次存的内容，下次再用key来调用。
# f=shelve.open("shelve_test")
# print(f)
#
# names=["scott1","scott2"]
# info={"name":"scott1","age":22}
# f["names"]=names
# f["info"]=info
#
# f.close()

f=shelve.open("shelve_test")
print(f)
print(dict(f))
print(list(f.items()))
print(f.get("names"))
f["scores"]=[1,2,3]
print(f["scores"])
del f['names']
print(list(f))
f.close()
