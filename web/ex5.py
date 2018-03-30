#!/usr/bin/python
# -*- coding: utf-8 -*-
#title			:ex5.py
#description	:http://learnpythonthehardway.org/book/ex5.html
#author			:Gonzalo
#date			:20160618
#version		:1.0
#usage			:python ex5.py
#notes			:
#python_version	:2.7.6
#==============================================================================

my_name = 'Gonzalo Sanchez'
my_age = 32
my_height = 178
my_weight = 69
my_eyes = 'Brown'
my_teeth = 'White'
my_hair = 'Blond'

print "Let's talk about %s." % my_name
print "He's %d cm tall." % my_height
print "He's %d Kg heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)

