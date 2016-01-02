#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math

L = [x * x for x in range(10)]
print L

g = (x * x for x in range(10))
print g
for n in g:
    print n


'''function Fibonacci'''
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print b
        a, b = b, a + b
        n = n + 1

fib(10)


def fib(max01):
    n, a, b = 0, 0, 1
    while n < max01:
        yield b
        a, b = b, a + b
        n = n + 1

print fib(8)


def odd():
    print 'step 1'
    yield 1
    print 'step 2'
    yield 3
    print 'step 3'
    yield 5

o = odd()
print o.next()
print o.next()
print o.next()
#print o.next()

for n in fib(6):
    print n