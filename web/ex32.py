#!/usr/bin/python
# -*- coding: utf-8 -*-
#title			:32.py
#description	:http://learnpythonthehardway.org/book/ex32.html
#author			:Gon
#date			:20160619
#version		:1.0
#usage			:python 32.py
#notes			:
#python_version	:2.7.6
#==============================================================================

the_count = [1,2,3,4,5]
fruits = ['apples','oranges','pears','apricots']
change = [1, 'pennies', 2,'dimes',3,'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
    print "This is counf %d" % number

# same as above
for fruit in fruits:
    print "A fruit of type: %s" % fruit

# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
    print "I got %r" % i

# we can also build lists, forst start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0,6):
    print "Adding %d to the list." % i
    # append is a function that lists understand
    elements.append(i)

# now we can print them out too
for i in elements:
  print "Element was: %d" % i  

