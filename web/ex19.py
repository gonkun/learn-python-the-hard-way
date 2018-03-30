#!/usr/bin/python
# -*- coding: utf-8 -*-
#title			:ex19.py
#description	:http://learnpythonthehardway.org/book/ex19.html
#author			:Gon
#date			:20160619
#version		:1.0
#usage			:python ex19.py
#notes			:
#python_version	:2.7.6
#==============================================================================

def cheese_and_crackers(cheese_count,boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

print "OR, we can use vatiables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
