#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

r = []
n = 3
for i in range(n):
    r.append(L[i])
print r

'''
对这种经常取指定索引范围的操作，用循环十分繁琐，因此，Python提供了切片（Slice）操作符，能大大简化这种操作。
#对应上面的问题，取前3个元素，用一行代码就可以完成切片：
'''

print L[0:3]
print L[:2]
print L[1:3]
print L[-2]

#####create list 0~99####
X = range(100)
print X

###pick first 10##
print X[:10]
###pick last 10###
print X[-10:]
##pick 11~20##
print X[10:20]
##pick first10, step 2###
print X[:10:2]
##pick every 5 ##
print X[::5]
##copy list##
print X[:]

###tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple：
C = (0, 1, 2, 3, 4, 5)[:3]
print C

###字符串'xxx'或Unicode字符串u'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串：
print 'ABCDEFG'[:3]
print 'ABCDEFG'[::2]