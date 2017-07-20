#!/usr/bin/python
# encoding:utf-8

'''
Created on 2017/7/6
@author: Yuping
'''

import sys

from PythonProjects.e1.excise1 import *
from PythonProjects.e1.excise1_love import *

print '''
 Input 1. print love
 Input 2. print feb
 Input 3. exit
'''

while True:
    input=raw_input("Please input nuber:")
    if input=='1':        # input is 1, print feb
        line = 17
        feb_list = [[]]     # init list
        for i in range(1, line + 1, 1):  # generate List
            if (i < 3):
                feb_list = [[1], [1, 1]]
            else:
                feb_tri(feb_list, i)  # Generate list
        print_triangle(feb_list, line)  # Print
    elif input=='2':
        love_print()
    elif input=='3':
        sys.exit()

    else:
        print "Please input 1, 2, or 3"