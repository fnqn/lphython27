#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math


def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax

print calc_sum(5,6,7)

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

print(lazy_sum(3))

f = lazy_sum(1,3,5,7,9)
print f

f1 = lazy_sum(1,3,5,7,9)
f2 = lazy_sum(1,3,5,7,9)
print f1 == f2

'''每次循环，都创建了一个新的函数，然后，把创建的3个函数都返回了'''
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()

print f1()
print f2()
print f3()


'''如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变：'''
def count():
    fs = []
    for i in range(1, 4):
        def f(j):
            def g():
                return j*j
            return g
        fs.append(f(i))
    return fs

f1, f2, f3 = count()

print f1()
print f2()
print f3()



'''lambda'''
print map(lambda x: x * x, range(1,10))

f = lambda x: x * x
print f
print f(5)

def build(x, y):
    return lambda: x * x + y * y

print build(2, 5)
