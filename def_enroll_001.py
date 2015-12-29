#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math

####define 一年级小学生注册####

####only name gender####
def enroll(name, gender):
    print 'name:', name
    print 'gender:', gender

enroll('Sarah','F')

####only name gender age city####
def enroll(name, gender, age=6, city='Beijing'):
    print 'name: ', name
    print 'gender: ', gender
    print 'age: ', age
    print 'city: ', city

enroll('Sarah','M')

enroll('Bob','F','8')
enroll('Nick','F',city='Sanya')
enroll('Jason','M','8','Shanghai')



####None parameter####
def add_end(L=[]):
    L.append('END')
    return L

add_end([1,2,3])
add_end(['x','y','z'])

add_end()

def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L