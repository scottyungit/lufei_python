#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:Leijie
@file:settings.py
"""
import os
import logging

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)
DB_PATH = os.path.join(BASE_DIR, "db")
DB_ADMIN_PATH = os.path.join(DB_PATH, "admin")
DB_COURSE_PATH = os.path.join(DB_PATH, "course")
DB_SCHOOL_PATH = os.path.join(DB_PATH, "school")
DB_STUDENT_PATH = os.path.join(DB_PATH, "student")
DB_TEACHER_PATH = os.path.join(DB_PATH, "teacher")
DB_ADMIN_ACCOUNT_FILE=os.path.join(DB_ADMIN_PATH, "admin.json")
LOG_PATH = os.path.join(BASE_DIR, "log")
# print(LOG_PATH)
LOG_LEVEL = logging.INFO
LOG_TYPES = {"access": "access.log",
             "sysadmin": "sys.log",
             }

LOG_FORMAT = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
