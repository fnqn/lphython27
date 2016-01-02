#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math

print range(1,11)

L = []
for x in range(1,11):
    L.append(x * x)
print L

print [x * x for x in range(1,11)]

''' only odd and even'''
print [x * x for x in range(1,11) if x % 2 ==0]
print [x * x for x in range(1,11) if x % 2 != 0]

'''生成全排列'''
print [m + n for m in range(1,3) for n in range(5,9)]
print [m + n for m in 'ABC' for n in 'xyz']

'''list current files/directory'''
import os
print [d for d in os.listdir('.')]

'''for using dict iteritem'''
d = {'x':'A','y':'B','z':'C'}
for k, v in d.items():
    print k,'= ',v
    print v,'=',k

d = {'x':'A','y':'B','z':'C'}
print [k + '=' + v for k,v in d.iteritems()]

L = ['Hello','World','IBM','ORACLE','APPLE']
print [s.lower() for s in L]
print [t.upper() for t in L]
