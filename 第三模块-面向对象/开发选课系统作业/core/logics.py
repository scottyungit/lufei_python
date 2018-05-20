#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:Leijie
@file:logics.py
"""

from conf import settings
import json


def interactive(self,features):
    for index, feature in enumerate(features):
        print("%s:%s" % (index, feature[0]))
    exit_flag=False
    while not exit_flag:
        choice = input("选择功能(“q” to exit): ").strip()
        if not choice: continue
        if choice.isdigit():
            if int(choice) < len(features):
                choice = int(choice)
                features[choice][1](self)
            else:
                print("值必须小于%s请重新输入" % len(features))
        if choice == "q": exit_flag = True


class School:
    def __init__(self,school_name,school_location):
        self.school_name = school_name
        self.school_location = school_location


class Banji:
    def __init__(self, name):
        self.name = name


class Teacher:
    def __init__(self,name,course):
        self.name = name
        self.course = course


class Course:
    def __init__(self, name, period, price):
        self.name = name
        self.period = period
        self.price = price


class Admin:
    def __init__(self):
        pass
    def create_school(self):
        school_name = input(">>Enter school name: ").strip()
        school_location = input(">>Enter school location").strip()
        s1 = School(school_name, school_location)

    def create_banji(self):
        banji_name=input(">>Enter class name: ").strip()
        banji1 = Banji(banji_name,)
x`

class AdminView:
    def __init__(self):
        pass

    def auth(self,username,password):
        with open(settings.DB_ADMIN_ACCOUNT_FILE, "r", encoding="utf-8") as f:
            account_data = json.load(f)
        if account_data['username'] == username and account_data['password'] == password:
            return True
        else:
            print("usrname or pasword is wrong")

    def login(self):
        back_flag = False
        username = input("Enter username: ").strip()
        password = input("Enter passowrd").strip()
        isauthenticated = AdminView.auth(self, username, password)
        if isauthenticated:
            features = [("校区管理", None),
                        ("讲师管理", None),
                        ("学员管理", None),
                        ("课程管理", None)
                        ]
            interactive(self, features)




class Admin:
    pass


class StudentView:
        pass


