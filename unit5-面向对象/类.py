#-*- coding: utf-8 -*-
class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age

p=Person("Alex",22)
print(Person)

p.male="男"
print(p.name,p.age,p.male)
