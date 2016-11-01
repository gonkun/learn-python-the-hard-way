#!/usr/bin/python
# -*- coding: utf-8 -*-
#title			:ex6.py
#description	:http://learnpythonthehardway.org/book/ex6.html
#author			:Gonzalo
#date			:20160618
#version		:1.0
#usage			:python ex6.py
#notes			:
#python_version	:2.7.6
#==============================================================================
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e

