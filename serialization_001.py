#!/usr/bin/env python
# -*- coding: utf-8 -*-

#d = dict(name='Bob', age=20, score=88)
#print d

'''
try:
    import cPickle as pickle
except ImportError:
    import pickle

d = dict(name='Bob', age=20, score=88)
pickle.dumps(d)


f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()

f = open('dump.txt', 'rb')
d = pickle.load(f)
f.close()
print d
'''

'''
import json
d = dict(name='Bob', age=20, score=88)
print json.dumps(d)


json_str = '{"age": 20, "score": 88, "name": "Bob"}'
json.loads(json_str)
'''



'''
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score =score

s = Student('Bob', 20, 88)
print(json.dumps(s))
'''
import json

def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score =score

s = Student('Bob', 20, 88)
print(json.dumps(s, default=student2dict))


def dict2student(d):
    return Student(d['name'],d['age'],d['score'])

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2student))




