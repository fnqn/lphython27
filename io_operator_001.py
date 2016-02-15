#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
#print os.name
#print os.uname()

#print os.environ
#print os.getenv('PATH')

print os.path.abspath('.')
print os.path.join('D:\Scripts\Python\Liaoxuefeng\lphython27','dirtest001')
#os.mkdir('D:\Scripts\Python\Liaoxuefeng\lphython27\dirtest001')
#os.rmdir('D:\Scripts\Python\Liaoxuefeng\lphython27\dirtest001')

#os.rename('1.txt', '2.txt')
#os.remove('2.txt')

print [x for x in os.listdir('.') if os.path.isdir(x)]
print [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']