#!/usr/bin/python
# -*- coding: utf-8 -*-
#title			:ex15.py
#description	:http://learnpythonthehardway.org/book/ex15.html
#author			:Gon
#date			:20160618
#version		:1.0
#usage			:python ex15.py
#notes			:
#python_version	:2.7.6
#==============================================================================

from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

