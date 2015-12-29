#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math

####define varaible parameters###
def person(name, age, **kw):
    print 'name: ', name, 'age: ', age, 'other: ', kw

print person('Michael',30)

print person('Bob',35, city='Bj')

print person('Adam',45, gender='M', Job='Engineer')

kw = {'city': 'Beijing', 'job': 'Engineer'}
print person('Jack',24,city=kw['city'],job=kw['job'])

kw = {'city': 'Beijing', 'job': 'Engineer'}
print person('Jack',24,**kw)