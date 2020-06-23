## Ex 1.A (a)
# Calculating the date that Easter Sunday will fall on in 2034 by using Gauss's Easter
# Algorithm

a = 2034 % 19
b = 2034 % 4
c = 2034 % 7
d = (19*a + 24) % 30
e = (2*b + 4*c + 6*d + 5) % 7
date = 22 + d + e

# We get date = 40.
# There are a maximum of 31 days in a month and 31 days in March. Easter Sunday
# must therefore fall in April

40 % 31

# = 9
# So Easter Sunday must fall on the 9th April in 2034

## Ex 1.A (b)
# We now calculate what day of the week Christmas day is on this year. We use Zeller's Congruence.

da=25
m=12
Y=2019%100
from math import floor
C=floor(2019/100)

# Following Zeller's congruence we obtain:

(da + floor(0.2*13*(m+1)) + Y + floor(0.25*Y) + floor(0.25*C) - 2*C)%7

# We get the value 4 so we conclude that Christmas day this year (2019) will fall on a Wednesday since 4=Wednesday.

## Ex 1.A (c)
# Now we calculate what day it will be on 1st August 2020 again using Zeller's congruence. 

dat=1
mo=8
Ye=2020%100
Ce=floor(2020/100)
((dat + floor(0.2*13*(mo+1)) + Ye + floor(0.25*Ye) + floor(0.25*Ce) - 2*Ce)%7)

# We get the value 0. We conclude that Yorkshire Day next year (1st August 2020) will fall on a Saturday since 0=Saturday.

## Ex 1.A (d)
# Again, we use Zeller's congruence to calculate what day it will have been on 26th December 1791.

date=26
mon=12
Yea=1791%100
Cen=floor(1791/100)
((date + floor(0.2*13*(mon+1)) + Yea + floor(0.25*Yea) + floor(0.25*Cen) - 2*Cen)%7)

# We get the value 2 so the date above falls on a Monday. 


## Ex 1.B (i)
# A command that will produce a list of all odd integers from 1 to 100 inclusive?

start, end = 1, 100
for num in range(start, end + 1): 
    if num % 2 != 0: 
        print(num, end = " ")


## Ex 1.B (ii)
# A command that will produce a list of all even integers from 1 to 100 inclusive?

start, end = 1, 100
for num in range(start, end + 1): 
    if num % 2 != 1: 
        print(num, end = " ")


## Ex 1.B (iii)
# What is the 3rd element of the list a produced by a = list(range(70,1030,3))

a = list(range(70,1030,3))
a[2]

# This gives you 76. The third element of the list is 76.


## Ex 1.B (iv)
# What is the penultimate element of the list b produced by b = list(range(-41,10))?

b = list(range(-41,10))
b[-1]

# This gives 9 so penultimate element is 9.


## Ex 1.B (v)
# What is the middle element of the list c produced by c = 10*a+5*b?

c = 10*a+5*b
((len(c) + 1)/2) - 1

# This gives 1727. Now,

c[1727]

# This gives 451. So the middle element of the list c is 451.

