#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Animal(object):
    def run(self):
        print 'Animal is running ...'

class Dog(Animal):
    def run(self):
        print 'Dog is running ... '
    def eat(self):
        print 'Eating meat... '


class Cat(Animal):
    def run(self):
        print 'Cat is runing'

dog = Dog()
cat = Cat()
print dog.run()
print dog.eat()
print cat.run()


a = list()
b = Animal()
c = Dog()

print isinstance(a, list)
print isinstance(b, Animal)
print isinstance(c, Dog)

print isinstance(c, Animal)

print isinstance(b, Dog)

def run_twice(animal):
    animal.run()
    animal.run()

print run_twice(Animal())
print run_twice(Dog())
print run_twice(Cat())
