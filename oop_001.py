#!/usr/bin/env python
# -*- coding: utf-8 -*-

def print_score(std):
    print '%s: %s' % (std['name'], std['score'])

std1 = { 'name': 'Michael','score':98 }
std2 = { 'name': 'Bob', 'score':81 }



class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print '%s: %s' % (self.name, self.score)

bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Campel', 88)
bart.print_score()
lisa.print_score()
