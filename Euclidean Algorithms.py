# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 12:30:12 2019

@author: mm18e2s
"""
''' Ex 2A'''
# Euclidean Algorithm for the following values: (105,24), (6024,1284), (98777,12945)

a = 105
b = 24
while b > 0:
    if a > b:
        a = a - b
    else:
        b = b - a
gcd = a
print(a) 


c = 6024
d = 1284
while d > 0:
    if c > d:
        c = c - d
    else:
        d = d - c
gcd = c
print(c)

e = 98777
f = 12945
while f > 0:
    if e > f:
        e = e - f
    else:
        f = f - e
gcd = e
print(e)

''' Ex 2B '''

# Extended Euclidean Algorithm

a = 105
b = 24
x = 0
xprev = 1
y = 1
yprev = 0
while b>0:
    q = a//b
    a, b=b, a%b
    x, xprev = xprev - q * x, x
    y, yprev = yprev - q * y, y
print(a)
print(xprev)
print(yprev)

#Finding counting steps for Euclidean algorithm

a = 105
b = 24
count = 0
while b > 0:
    if a > b:
        a = a - b
    else:
        b = b - a
        count += 1
gcd = a
print(count)

'''Ex 2C (2)'''

x = count
print(x)
a = 105
from math import log
print(5*log(a,10))

'''Ex 2C (3)'''

from math import pi
from math import e
a = 105
((12*log(2,10))/(pi)**2)*log(a,10)
y = ((12*(log(2))/(pi)**2)*log(a)

#Values greater than

a = 200
b = 90
count = 0
while b > 0:
    if a > b:
        a = a - b
    else:
        b = b - a
        count += 1
gcd = a
print(count)
5

a = 200 
(12*log(2)*log(a))/(pi)**2 


'''Values of a and b where the steps in the Euclidean algorithm is less than the average of 12ln2/pi^2*lna'''
a = 200
b = 24
count = 0
while b > 0:
    if a > b:
        a = a - b
    else:
        b = b - a
        count += 1
gcd = a
print(count)

a =200
(12*log(2)*log(a))/(pi)**2 


'''Confirm that the number of steps attains the maximum of 5loga when a and b are fibonnacci numbers'''
a = 210
b = 36
count = 0
while b > 0:
    if a > b:
        a = a - b
    else:
        b = b - a
        count += 1
gcd = a
print(count)

a = 200
k = (12*log(2)*log(a))/(pi)**2
k
m = floor(k)
m
count > m

# Give examples of a,b which produce larger
# and smaller number of steps than the average
# here: (200,24), (200,90)










