#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 23 19:40:04 2020

@author: elliesleightholm
"""
# YouTube Course - sentdex
# String Concatenation and Formatting - Intermediate Python Programming Part 2

names = ['Jeff','Gary','Jill','Samantha']

for name in names:
    print('Hello there, ' + name)
 
# OR 
    
names = ['Jeff','Gary','Jill','Samantha'] 
for name in names:
# the following line of code, 'join' command joins the list of things you want
# together and ' ' leaves a space between those items. 
    print(' '.join(['Hello there,', name ]))
    

# This prints the list of names
print(', '.join(names))

# If you're concatenating more than 2 strings, you should use the command
# join because it'll scale better and use less processing

# Example using join
import os

location_of_files = '/Users/elliesleightholm/Desktop/YouTube Tutorial'
file_name = 'Example.txt'

print('location_of_files' + '\\' + file_name)

with open(os.path.join(location_of_files, file_name)) as f:
    print(f.read)
    
#String Formatting
    
who = 'Gary'
how_many = 12

# We're looking for a sentence that says 'Gary bought 12 apples today!'
# It may be tempting to do it is as follows:

print(who,'bought',how_many,'apples today!')

#However, we use this approach instead:

print('{} bought {} apples today!'.format(who, how_many))

#OR

print('{0} bought {1} apples today!'.format(who, how_many))


















