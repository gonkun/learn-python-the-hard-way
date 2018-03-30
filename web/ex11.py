#!/usr/bin/python
# -*- coding: utf-8 -*-
#title			:ex11.py
#description	:http://learnpythonthehardway.org/book/ex11.html
#author			:Gonzalo
#date			:20160618
#version		:1.0
#usage			:python ex11.py
#notes			:
#python_version	:2.7.6
#==============================================================================

print "How old are you?",
age = raw_input()

print "How tall are you?",
height = raw_input()

print "How much do you weight?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % ( age, height, weight)

