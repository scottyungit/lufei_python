#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:Leijie
@file:course.py
"""

##!/usr/bin/env python
# -*- coding:utf-8 -*-
#version:3.5.2
#author:wangeq

import sys,os

#程序主目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#添加环境变量
sys.path.append(BASE_DIR)

from core import main2

if __name__ == '__main__':
    a =main2.Run()
    a.interactive()
