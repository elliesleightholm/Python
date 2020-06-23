# import files here
from math import sin
from math import cos
from math import pi
from math import sqrt
from math import atan

# 5A Write your functions below
# E.g., a function which takes an integer and squares it
# def squared 

def squared(x):
    xx = x**2
    return xx

## DO NOT CHANGE THE FUNCTION NAMES!! ##
# (1)  def cubed

def cubed(x):
    xx = x**3
    return xx


#(2) def sumanddiff

def sumanddiff(x,y):
    x_plus_y = x+y
    difference = abs(y-x)
    return x_plus_y, difference

#(3) def sin2cos2

def sin2cos2(x):
    trig = (sin(x))**2 + (cos(x))**2
    return trig 


#(4) def fibonacci
    
def fibonacci(n):
    if n < 0:
        return "Invalid Input"
    if n==0:
        return[]
    if n==1:
        return[1]
    elif n==2:
        return[1,1]
    else:
        fibonacci_list=fibonacci(n-1)
        fibonacci_list.append(fibonacci_list[-1]+fibonacci_list[-2])
    return fibonacci_list


#(5) def polartocartesian

def polartocartesian(r, theta):
    x = r*cos(theta)
    y = r*sin(theta)
    return(x, y)


#(6) def cartesiantopolar
    

def cartesiantopolar(x, y):
    r = sqrt(x**2 + y**2)
    if x > 0:
        theta = atan(y/x)
    elif x < 0:
        theta = atan(y/x) + pi
    elif x==0 and y>0: 
        theta = pi/2
    elif x==0 and y<0:
        theta = -pi/2
    elif x==0 and y==0:
        theta = 0
    return(r, theta)

## DO NOT CHANGE THE FUNCTION NAMES!!
# 5B
#(1) def horner

def horner(x,coeffs):
    coeffs.reverse()
    b=0
    for a in coeffs:
        b = a+x*b
    return b
        

#(2)(a)
# For P1(x) = x^3 + 3x + 2 at x=6, we simply input the following:

print(horner(6,[2,3,0,1]))

# This gives the value of 236 so at x=6 the polynomial equals 236.
# 
#(2)(b)
# For P2(x) = 2 - x^2 at x = sqrt(2), we simply input the following:

print(horner(sqrt(2),[2,0,-1]))

# This gives the value -4.440892098500626e-16 

# Are the answers exact?
# For (a) python gives the value of 236. Doing the calculation by hand
# or in Python, ((6)**3 + 3*6 + 2), we also get 236. Therefore, this is exact.
# 
# For (b) this gives the value -4.440892098500626e-16 which we can immediately 
# see is  not exact. If we do the calculation by hand we get 2 - 2 = 0 and 
# -4.440892098500626e-16 does not equal 0 .
# Even using the floor function on horner(sqrt(2),[2,0,-1]) we get -1 which
# does not equal 0. 
# We can also check this by running the commmand:
# horner(sqrt(2),[2,0,-1]) == 0 
# which returns False. So we can therefore say that the answer to (b) is not
# exact. 
# This is simply because python uses finite precision when calculating
# a number like sqrt(2) and gives an approximation rather than it's exact 
# value. 



#(3)
# def hornerderiv

def hornerderiv(x,coeffs):
    coeffs.reverse()
    b = 0
    deriv = 0
    for a in coeffs:
        deriv = x*deriv+b
        b = a+x*b
    return b,deriv

# This function returns (b, deriv) where b is the value of P(x0) and deriv
# is the value of P'(x0)


#(4)(a)
# e.g., P_3(1) and P_3'(1) where P_3(x) is defined as x^2 - 4x^3 + 7x^5 can 
# be calculated by the following command:
    
print(hornerderiv(1,[0,0,1,-4,0,7]))

# print(hornerderiv(1,[0,0,1,-4,0,7])) = (4,25) 
# From this we see that P_3(1) = 4 and the derivative of P_3(x) at x = 1 
# equals 25.

#(4)(b)
# e.g., P_3(pi) and P_3'(pi) where P_3(x) is defined as x^2 - 4x^3 + 7x^5 can 
# be calculated by the following command:
    
print(hornerderiv(pi,[0,0,1,-4,0,7]))

# print(hornerderiv(pi,[0,0,1,-4,0,7])) = (2027.9822911768597, 3297.166118684192)
# From this we see that P_3(pi) = 2027.9822911768597 and the derivative of P_3(x) 
# at x = pi equals 3297.166118684192.



#(5)
# e.g. The first non-zero terms of the Maclaurin series of sin^(-1)(x) is 
# given by:
# x + (x^3/6) + (x^5/6) + (5x^7/112)
# The coefficients can be written in the list [0,1,0,1/6,0,3/40,0,5/112] 
# Substituting this into the horner function at x = 1, we get:

print(horner(1, [0,1,0,1/6,0,3/40,0,5/112]))

# 
# print(horner(1, [0,1,0,1/6,0,3/40,0,5/112])) gives the value 
# 1.286309523809524
# Therefore, using the first four non-zero terms in the Maclaurin series
# of sin^(-1)(x) and substituing this into the horner function at x=1
# gives an approximation to pi/2 as 1.286309523809524 










