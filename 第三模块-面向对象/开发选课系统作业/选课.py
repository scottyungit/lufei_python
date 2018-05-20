# -*- coding: utf-8 -*-

class School:
    def __init__(self, localtion):
        self.localtion = localtion


class Student:
    def __init__(self, name):
        self.name = name

class Course:
    def __init__(self, name,period, price):
        self.name = name
        self.period = period
        self.price = price

class Teacher:
    def __init__(self, name):
        self.name = name

class Banji:
    def __init__(self,name):
        self.name = name


bj = School("Beijing")
sh = School("Shanghai")

linux = Course("linux", 10, 8000)
python = Course("python", 8, 9000)
go = Course("go", 6, 10000)

banji1=Banji("banji1")

alex=Teacher("alex")

banji1.teacher = alex
banji1.course = linux

bj.course = [linux, python]
sh.cource = [go]

bj.banji = [banji1,]
