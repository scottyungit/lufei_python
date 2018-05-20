name=input("enter your name: ")
age=int(input("enter your age: "))
job=input("enter your job: ")
hometown=input("enter your hometown: ")

#占位符： %s %d %f
##三个引号就算是写多行了
print(
"""--- info of %s---
name:%s
age:%d
job:%s
hometown:%s
---end--- """ %(name,name,age,job,hometown))

info="""
--- info of %s---
name:%s
age:%d
job:%s
hometown:%s
---end--- 
"""  %(name,name,age,job,hometown)
print(info)

#