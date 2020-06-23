# import files here

#Exercise 4A

from math import floor 
def continued_fraction_approx(a,i):
    cf = []
    r = a
    for j in range(0,i):
        cf.append(floor(r))
        r = 1/(r-floor(r))
    return cf 

# Answers to question:
# a_i cannot equal 0 at any point as 1 divided by 0 is always undefined.   
    


#Exercise 4B

def continued_fraction_exact(num,den):
    cf = []
    while den>0:
        cf.append(num//den)
        num=num%den 
        den,num=num,den
    return cf   

# Answers to question:
# continued_fraction_exact(123456789,987654321) gives [0,8,13717421]
# We can simply compute our continued fraction expansion list as a fraction:
# '123456789/987654321 == 0 + 1/(8+(1/13717421))' 
# This gives the output 'True' so it is therefore exact.



#Exercise 4C

def rational_from_cf(somelist):
    num = somelist[-1]
    den = 1
    for j in range(len(somelist) - 1):
        den,num=num,den
        somelist.pop(-1)
        num = num + den*somelist[-1]
    return num,den
    
    
# Answers to question:
#Continued fractions of the positive rational numbers a/b and b/a are related
# such that their continued fraction expansion list are identical but for 
# the case where b>a, a/b does begin with a 0 but b/a doesn't. So the 
# continued fraction expansion for b/a = [a[0],a[1],a[2],a[3],...a[n]] and
# a/b = [0,a[0],a[1],a[2],a[3],...,a[n]] where b>a


#Exercise 4D
     
def partcon(a,k):
    cf = continued_fraction_approx(a,k+1)
    return rational_from_cf(cf)
    

#Answers to questions
#(i)
# partcon(((1+sqrt(5))/2),1) = (2,1)
# partcon(((1+sqrt(5))/2),2) = (3,2)
# partcon(((1+sqrt(5))/2),3) = (5,3)
# partcon(((1+sqrt(5))/2),4) = (8,5)
# partcon(((1+sqrt(5))/2),5) = (13,8)
# The first five partial convergents are:
# k = 1 gives (2,1) = 2/1
# k = 2 gives (3,2) 
# k = 3 gives (5,3)
# k = 4 gives (8,5) 
# k = 5 gives (13,8)
# The pattern here is that the previous two terms in the (num, den) form are added together to create the next term.
# For example k = 3 gives the result of (2,1)+(3,2) = (5,3) (where k=1 gives (2,1) and k = 2 gives (3,2))
# Also, k = 5 gives the result of (5,3)+(8,5) = (13,8) (where k = 2 gives (5,3) and k = 3 gives (8,5))
#From this we can conclude that k = 6 gives (8,5)+(13,8)=(21,13)
#
#
#(ii) The closest approximation to pi of all fractions with denominator at most 113 is 
# 355/113 
#(355,133)
#
#
#
#(iii) We can create a function to test which the first partial convergent of sqrt(5) is within 0.001% of the true value:
'''
from math import sqrt
def conv(t, true_value, accuracy):
    num,den=t[0],t[1]
    num_d_den = t[0]/t[1]
    if abs(num/den - true_value) < accuracy:
        return True
    else:
        return False '''
        
# We then input t = partcon(sqrt(5),k) for k any positive intger greater than zero
# Doing this we get that for k = 4, the function returns True
# Therefore, the first partial convergent of sqrt(5) to be within 0.00001% of sqrt(5) is when 
#k = 4 and the fraction is 682/305








