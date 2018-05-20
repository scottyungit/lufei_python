#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:Leijie
@file:course_app_start.py
"""

import os, sys
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)
print(sys.path)
if __name__ == "__main__":
    from core import main
    main.run()  # 入口

