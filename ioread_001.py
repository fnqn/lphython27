#!/usr/bin/env python
# -*- coding: utf-8 -*-

f = open('D:/Scripts/Python/Liaoxuefeng/lphython27/1.txt','r')

print f.read()
f.close()

try:
    f = open('D:/Scripts/Python/Liaoxuefeng/lphython27/1.txt','r')
    print f.read()
finally:
    if f:
        f.close()

with open('D:/Scripts/Python/Liaoxuefeng/lphython27/1.txt','r') as f:
    print f.read()

with open('D:/Scripts/Python/Liaoxuefeng/lphython27/1.txt','r') as f:
    for line in f.readlines():
        print(line.strip()) # 把末尾的'\n'删掉

