#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:Leijie
@file:main.py
"""

import os
import conf.settings
from .logger import logger
from libs import school, student, course
from .logics import AdminView



access_log = logger("access")
sysadmin_log = logger("sysadmin")

features = [("学员视图", None),
          ("讲师视图", None),
          ("系统视图", AdminView),
         ]

def run():
    print("-----欢迎进入选课系统-----")
    exit_flag=False
    while not exit_flag:
        for index, feature in enumerate(features):
            print("%s:%s" % (index, feature[0]))
        choice = input("选择视图(“q” to exit): ").strip()
        if not choice: continue
        if choice.isdigit():
            if int(choice) < len(features):
                choice = int(choice)
                obj = features[choice][1]()
                obj.login()
            else:
                print("值必须小于%s请重新输入" % len(features))
        if choice == "q": exit_flag = True




# def run():
#     menu = """
#     ----- 欢迎进入选课系统-----
#           1.学员视图
#           2.讲师视图
#           3.系统视图
#           4.退出
#           """
#
#     menu_dic = {
#         "1": None,
#         "2": None,
#         "3": None,
#     }
#     print(menu)
#     exit_flag = False
#     while not exit_flag:
#         option = input("选择视图:").strip()
#         if not option: continue
#         if int(option) == 4:
#             exit_flag = True
#         elif option in menu_dic:
#             menu_dic[option].login()
#         else:
#             print("输入错误，请重新输入")

