#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math

d = {'a':1,'b':2,'c':3}
for key in d:
    print(key)

for value in d.itervalues():
    print(value)

for k,v in d.items():
    print (k,v)

for ch in 'ABC':
    print ch

from collections import Iterable
print isinstance('abc',Iterable)
print isinstance('123',Iterable)

for i,value in enumerate(['A','B','C']):
    print(i,value)

for x,y in [(1,1),(2,4),(3,9)]:
    print x,y