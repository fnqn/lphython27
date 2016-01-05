#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math

''' f(x)=x^2'''
''' using map()
map()函数接收两个参数，一个是函数，一个是序列，map将传入的函数依次作用到序列的每个元素，并把结果作为新的list返回'''
def f(x):
    return x*x

print map(f, range(1,10))


'''using for loop'''
L = []
for n in [1,2,3,4,5,6,7,8,9]:
    L.append(f(n))
print L

print map(str, range(1,10))


'''reduce的用法。reduce把一个函数作用在一个序列[x1, x2, x3...]上，这个函数必须接收两个参数，
reduce把结果继续和序列的下一个元素做累积计算，其效果就是
reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)'''


'''eg: sum'''
def add(x, y):
    return x + y
print reduce(add, [1,3,5,7,9])

print sum([1,3,5,7,9])

'''eg: 如果要把序列[1, 3, 5, 7, 9]变换成整数13579'''
def fn(x, y):
    return x * 10 + y
print reduce(fn,[1, 3, 5, 7, 9])

def fn(x,y):
    return x * 10 + y
def char2num(s):
    return {'0':0, '1': 1, '2':2, '3':3,'4':4,'5':5,'6':6, '7':7, '8':8 ,'9':9}[s]
print reduce(fn,map(char2num, '13579'))


def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return {'0':0, '1': 1, '2':2, '3':3,'4':4,'5':5,'6':6, '7':7, '8':8 ,'9':9}[s]
    return reduce(fn, map(char2num, s))

print str2int('18')

def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
def str2int(s):
    return reduce(lambda x,y: x*10+y, map(char2num, s))
print char2num('2')