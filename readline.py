#!/usr/bin/python
# -*- coding: utf-8 -*-
#title			:readline.py
#description	:read lines from a textfile
#author			:Gon
#date			:20160619
#version		:1.0
#usage			:python readline.py
#notes			:
#python_version	:2.7.6
#==============================================================================

from sys import argv

script, input_file = argv

def print_a_line(filename):
    for i in range(0,5):
        print filename.readline()

current_file = open(input_file)

current_file.seek(0)



print_a_line(current_file)
