#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math


def is_odd(n):
    return n % 2 == 1
print filter(is_odd, range(10))

def not_empty(s):
    return s and s.strip()
print filter(not_empty,['A','B','Home', 'C', ' '])