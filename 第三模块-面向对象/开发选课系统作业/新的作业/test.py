#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:Leijie
@file:test.py
"""

class School(object):
    '''学校类'''

    def __init__(self, school_name, city_name, teachers=None, courses=None, students=None, banjis=None):
        '''
        定义学校属性
        :param school_name: 学校名，字符类型
        :param city_name: 城市名，字符类型
        :param teachers: 讲师，字典类型，如{"teachers": []}
        :param students: 学员, 字典类型，如{"students": []}
        :param courses: 课程，字典类型，如{"courses": []}
        :param banjis: 班级，字典类型，如{"banjis": []}
        '''
        self.school_name = school_name
        self.city_name = city_name
        self.teachers = teachers
        self.courses = courses
        self.students = students
        self.banjis = banjis
        #self.db = Db(settings.BASE_DATABASE)  # 数据库连接
        #self.db_path = self.db.db_handler()


# go = Course("go", 8000)
# linux = Course("linux", 10800)
# python = Course("python", 8800)

# 创建学校2所，北京老男孩、上海老男孩
beijing_oldboy_school = School("beijing_oldboy_school", "beijing",
                               {"teachers": []},
                               {"students": []}, {"banjis": []})

base_data = {
            "schools": [beijing_oldboy_school,],
        }
school = base_data["schools"]
attr_students = "students"
students = getattr(school, attr_students)[attr_students]
print(students)