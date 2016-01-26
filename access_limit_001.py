#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
class Student(object):
    pass

bart = Student()
bart.name = 'Bart Simpson'

print bart.name
print bart
print Student
'''

'''
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

bart = Student('Bart Simpson', 59)
print bart.name
print bart.score

def print_score(std):
    print '%s: %s' % (std.name, std.score)
print_score(bart)

'''
class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 >= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

    def print_score(self):
        print '%s: %s' % (self.name, self.score)


    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

bart = Student('Bart Simpson', 98)
#print bart.__name
print bart.print_score()
print bart.get_grade()
