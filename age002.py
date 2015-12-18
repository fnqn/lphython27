#!/usr/bin/env python
# -*- coding: utf-8 -*-
age = input('how old are you: ')
if age >= 18:
    print 'your age is', age
    print 'adult'
elif age >=6:
    print 'your age is', age
    print 'teenager'
elif age <= 0:
    print 'your age is', age
    print 'wrong input format,please input your real age'
else:
    print 'your age is', age
    print 'kid'
