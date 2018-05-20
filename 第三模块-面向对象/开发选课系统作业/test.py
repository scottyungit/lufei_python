#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:Leijie
@file:test.py
"""


import hashlib
import time

def create_md():
    m = hashlib.md5()
    m.update(bytes(str(time.time()), encoding='utf-8'))
    return m.hexdigest()

class Admin:
    pass

Admin()