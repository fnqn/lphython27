#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math

####define varaible parameters###
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print calc(1,2,3)