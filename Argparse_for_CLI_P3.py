#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 24 19:28:44 2020

@author: elliesleightholm
"""
# YouTube Course - sentdex
# Argparse for CLI (Command Line Interface) - Intermediate Python Programming Part 3

# We are going to convert the following function into a Command Line Interface
# using Argparse

def calc(x, y, operation):
    if operation == 'add':
        return x + y
    if operation == 'sub':
        return x - y
    if operation == 'mul':
        return x * y
    if operation == 'div':
        return x / y
    
# Computing using Argparse

import argparse
import sys

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--x', type=float, default=1.0,
                        help='What is the first number?')
    parser.add_argument('--y', type=float, default=1.0,
                        help='What is the second number?')    
    parser.add_argument('--operation', type=str, default='add',
                        help='What operation? (add,sub,mul,div)')
    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))

def calc(args):
    if args.operation == 'add':
        return args.x + args.y
    if args.operation == 'sub':
        return args.x - args.y
    if args.operation == 'mul':
        return args.x * args.y
    if args.operation == 'div':
        return args.x / args.y
    
if __name__== '__main__':
    main()
    
# We now open up the terminal and input commands.
# We first begin by inputting:
    
    # python /Users/elliesleightholm/Desktop/Argparse_for_CLI.py  --x=5 --y=2 --operation=mul
    
# this returns 10.0
    
# We can now type '-h' to get a help output, i.e what we're trying to run, 
# what our various options are, etc.








