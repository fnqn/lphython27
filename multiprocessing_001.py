#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
import time, threading

#新线程执行的代码
def loop():
    print 'thread %s is runing...' % threading.current_thread().name
    n = 0
    while n < 5:
        n = n + 1
        print 'thread %s >>> %s' % (threading.current_thread().name,n)
        time.sleep(1)
    print 'thread %s ended.' % threading.current_thread().name
print 'thread %s is runing ...' % threading.current_thread().name

t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print 'thread %s ended.' % threading.current_thread().name
'''

'''没有加锁
import time, threading

#假定这是你的银行存款
balance = 0

def change_it(n):
    #先存后取,结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(10000):
        change_it(n)

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print balance

没有加锁'''


'''加锁
import time, threading

#假定这是你的银行存款,加锁,同一时间只能一个线程更改
balance = 0
lock = threading.Lock()

def change_it(n):
    #先存后取,结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(10000):
        change_it(n)

def run_thread(n):
    for i in range(10000):
        #先要获取锁:
        lock.acquire()
        try:
            #放心改吧:
            change_it(n)
        finally:
            #改完一定要释放锁,给别的线程更改
            lock.release()


t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print balance

加锁'''



'''S 循环
import threading, multiprocessing

def loop():
    x = 0
    while True:
        x = x ^ 1

for i in range(multiprocessing.cpu_count()-1):
    t = threading.Thread(target=loop)
    t.start()
S循环'''