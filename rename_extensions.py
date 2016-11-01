#!/usr/bin/python
# -*- coding: utf-8 -*-
#title			:rename_extensions.py
#description	:https://github.com/geekcomputers/Python/blob/master/batch_file_rename.py
#author			:Gon
#date			:20160619
#version		:1.0
#usage			:python rename_extensions.py
#notes			:
#python_version	:2.7.6
#==============================================================================


'''
This will batch rename a group of files in a given directory,
once you pass the current and new extensions
'''

__author__ = 'Gonzalo Sanchez'
__version__ = '1.0'

import os
import sys

def rename_extensions(work_dir, old_ext, new_ext):
    for filename in os.listdir(work_dir):
        file_ext = os.path.splitext(filename)[1]
        if old_ext == file_ext:
            newfile = filename.replace(old_ext,new_ext)
            os.renames(os.path.join(work_dir, filename), os.path.join(work_dir,newfile))

def main():
    work_dir = sys.argv[1]
    old_ext = sys.argv[2]
    new_ext = sys.argv[3]
    rename_extensions(work_dir, old_ext, new_ext)

if __name__ == '__main__':
    main()

