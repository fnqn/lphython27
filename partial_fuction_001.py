#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math

print int('256')

print int('256',8)
print int('256',16)

def int2(x, base = 2):
    return int(x,base)

print int2('10000')
print int2('111111')

import functools
int2 = functools.partial(int, base = 2)
print int2('10000')

