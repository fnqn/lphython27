#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math

####define x power####
def power(x):
    return x * x

####define x power n ####
def power3(x,n):
    s = 1
    while n > 0:
        n = n -1
        s = s * x
    return s

#### define x power 2 x2###
def power2(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
