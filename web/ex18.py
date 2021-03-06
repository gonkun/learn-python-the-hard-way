#!/usr/bin/python
# -*- coding: utf-8 -*-
#title			:ex18.py
#description	:http://learnpythonthehardway.org/book/ex18.html
#author			:Gon
#date			:20160619
#version		:1.0
#usage			:python ex18.py
#notes			:
#python_version	:2.7.6
#==============================================================================

# this one is like your scripts with argv

def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes one argument
def print_one(arg1):
    print "arg1: %r" % arg1

# this one takes no arguments
def print_none():
    print "I got nothin'."

print_two("Gonzalo","Sanchez")
print_two_again("Gonzalo","Sanchez")
print_one("First!")
print_none()

