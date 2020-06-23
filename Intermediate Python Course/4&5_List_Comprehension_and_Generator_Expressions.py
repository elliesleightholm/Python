#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 24 20:45:27 2020

@author: elliesleightholm
"""
# YouTube Course - sentdex
# List Comprehension and Generator Expressions - Intermediate Python Programming Part 4 & 5

# The following two codes produce the same output

xyz = [i for i in range(5)]
print(xyz)

xyz = []
for i in range(5):
    xyz.append(i)
print(xyz)

# The following is a generator expression.

xyz = (i for i in range(5))
print(xyz)

# Part 5

input_list = [5,6,2,10,15,20,5,2,1,3]

def div_by_five(num):
    if num % 5 == 0:
        return True
    else:
        return False
    
# Generator     
xyz = (i for i in input_list if div_by_five(i))
for i in xyz:
    print(i)
    
# OR
    
xyz = (i for i in input_list if div_by_five(i))    
[print(i) for i in xyz]

# How the generator essentially works
xyz = []
for i in input_list:
    if div_by_five(i):
        xyz.append(i)
        
# List comprehension:
        
xyz = [i for i in input_list if div_by_five(i)]
print(xyz)
[print(i) for i in xyz]

# If we type the following, we don't get any output
(print(i) for i in xyz)

# This gives every combination of 2 numbers in the range 0 to 5

[[print(i,ii) for ii in range(5)] for i in range(5)]        # (1)

# This is identical to

for i in range(5):                          
    for ii in range(5):                                     # (2)
        print(i,ii)
        
# To obtain (1) we work backwards from (2). So we begin with the last line:

print(i,ii)

# Follow with the second to last line but replace the : with [].

[print(i,ii) for ii in range(5)] 

# Follow with the first line and replace the : with [] again:

[[print(i,ii) for ii in range(5)] for i in range(5)] 

# OR, you can write the following which gives a list of tuples:

xyz = [[(i,ii) for ii in range(5)] for i in range(5)] 
print(xyz)

# OR

xyz = ([(i,ii) for ii in range(5)] for i in range(5))
print([i for i in xyz])

#OR

xyz = ([(i,ii) for ii in range(5)] for i in range(5))
for i in xyz:
    print(i)
    
# OR
    
xyz = (((i,ii) for ii in range(5)) for i in range(5))
for i in xyz:
    for ii in i:
        print(ii)

# with big list comprehensions you'll run out of memory. With big generators 
# you'll run out of time.

