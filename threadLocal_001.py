#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
global_dict = {}

def process_student(name):
    std = Student(name)
    #std是局部变量,但是每个函数都要用它,因此必须传进去:-把std放到全局变量golbal_dict中
    global_dict[threading.current_thread()] = std
    do_task_1(std)
    do_task_2(std)

def do_task_1(std):
    #不传入std,而是根据当前线程查找:
    std = global_dict[threading.current_thread()]
    # do_subtask_1(std)
    #do_subtask_2(std)

def do_task_2(std):
    std = global_dict[threading.current_thread()]
    #do_subtask_2(std)
    #do_subtask_2(std)
'''


import threading

#创建全局ThreadLocal对象:
local_school = threading.local()

def process_student():
    print 'Hello, %s (in %s)' % (local_school.student, threading.current_thread().name)

def process_thread(name):
    #绑定ThreadLocal的student:
    local_school.student = name
    process_student()

t1 = threading.Thread(target=process_thread, args=('Alice',),name='Thread-A')
t2 = threading.Thread(target=process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()