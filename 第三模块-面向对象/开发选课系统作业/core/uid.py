#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:Leijie
@file:uid.py.py
"""

import hashlib
import time


def create_md():
    m = hashlib.md5()
    m.update(bytes(str(time.time()),encoding='utf-8'))
    return m.hexdigest()
