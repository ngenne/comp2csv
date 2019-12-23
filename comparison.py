# coding: utf-8
"""
Created on Tue Nov  5 10:44:54 2019

@author: NGENNE
"""

### COMPARISON ##

import argparse

parser = argparse.ArgumentParser(description='REMEMBER : You do not have to put ">" after the command line because this program creates already a file named "output.txt" in the current file directory !')
parser.add_argument('file1', type=str, help='Needs to write first file path you want to compare as initial')
parser.add_argument('file2', type=str, help='Needs to write second file path you want to compare as final')

args = parser.parse_args()

import sys
import difflib

old = open(sys.argv[1], 'r').readlines()
new = open(sys.argv[2], 'r').readlines()

output = open("output.txt","w") # write mode 

for line in difflib.unified_diff(old, new):
    output.write(line) 

output.close()



# if the number of lines --- is equal to the number of lines +++, so there is no differences between files ;)
