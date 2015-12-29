#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math

####define mix parameters###

def func(a, b, c=0, *args, **kw):
    print 'a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw

print func(1,2)
print func(1,2,c=3)
print func(1,2,3,'a')
print func(1, 2, 3, 'a', 'b')
print func(1, 2, 3, 'a', 'b', x=99)

args = (1,2,3,4)
kw = {'x': 99}
func(*args, **kw)
