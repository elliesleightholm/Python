#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 21 16:52:40 2020

@author: elliesleightholm
"""

# Draws a heart

import turtle
turtle.speed(5)
turtle.bgcolor("black")

def curve():
    for i in range(200):
        turtle.right(1)
        turtle.forward(1)

turtle.color("red", "pink")        

turtle.begin_fill()
turtle.left(140)
turtle.forward(111.65)
curve()

turtle.left(120)
curve()
turtle.forward(111.65)
turtle.end_fill()
turtle.hideturtle()

# Draws a circle every 10 degrees for a 360 degree turn 

import turtle
turtle.bgcolor("black")
turtle.pensize(2)
# turtle.speed(0)

for i in range(6):
    for colours in ["red", "magenta", "blue","cyan","green","yellow"]:
        turtle.color(colours)
        turtle.circle(100)
        turtle.left(10)

        
