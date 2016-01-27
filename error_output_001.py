#!/usr/bin/env python
# -*- coding: utf-8 -*-

def foo():
    r = some_function()
    if r == (-1):
        return (-1)
    # do something
    return r

def bar():
    r = foo()
    if r == (-1):
        print 'Error'
    else:
        pass

print '########next part#######'
print '########next part#######'

try:
    print 'try...'
    r = 10 / 0
    print 'result:', r
except ZeroDivisionError, e:
    print 'except:',e
finally:
    print 'finally...'
print 'END'

print '########next part#######'
print '########next part#######'

try:
    print 'try...'
    r = 10 / int('a')
    print 'result:', r
except ValueError, e:
    print 'ValueError:', e
except ZeroDivisionError, e:
    print 'ZeroDivisionError:', e
else:
    print 'no error!'
finally:
    print 'finally...'
print 'END'

print '########next part#######'
print '########next part#######'

try:
    foo()
except StandardError, e:
    print 'StandardError'
except ValueError, e:
    print 'ValueError'


print '########next part#######'
print '########next part#######'

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except StandardError, e:
        print 'Error!'
    finally:
        print 'finally...'


print '########next part#######'
print '########next part#######'

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) *2

def main():
    bar('1')   ###bar('0')

main()

print '########next part#######'
print '########next part#######'


import logging

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('1')  #### bar('0')
    except StandardError, e:
        logging.exception(e)

main()
print 'END'


print '########next part#######'
print '########next part#######'


class FooError(StandardError):
    pass

def foo(s):
    n = int(s)
    if n==0:
        raise FooError('invalid value: %s ' % s)
    return 10/n

foo(1)

print '########next part#######'
print '########next part#######'

def foo(s):
    n = int(s)
    return 10 / n

def bar(s):
    try:
        return foo(s) * 2
    except StandardError, e:
        print 'Error!'
        raise

def main():
    bar('2')

main()


try:
    10 / 2
except ZeroDivisionError:
    raise ValueError('input error!')
