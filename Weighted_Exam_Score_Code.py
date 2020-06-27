#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 20:57:55 2020

@author: elliesleightholm
"""

# Weighted Exam Score Average 

num =int(input("Enter number of exams : "))
average = 0
year = int(input("Enter how many credits these exams cover : "))
for i in range(num):
    score = int(input("Enter Exam Score : "))
    credit = int(input("Enter how many credits is this exam worth : "))
    average = average + score*credit/year
print("Your average is", average)
