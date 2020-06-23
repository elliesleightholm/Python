#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 21:57:00 2019

@author: elliesleightholm
"""

import matplotlib.pyplot as plt

# Part 1 (a)

def primelist(n):
    primes = list(range(2,n+1))
    for i in primes:
        j=2
        while i*j<= primes[-1]:
            if i*j in primes:
                primes.remove(i*j)
            j=j+1
    return primes

# Part 1 (b)
N = 100
primes = primelist(N)

# Part 1 (c)

def twinprimes(n):
    mylist=[]
    primes = list(range(2,n+1))
    for i in primes:
        j=2
        while i*j<= primes[-1]:
            if i*j in primes:
                primes.remove(i*j)
            j=j+1
    for k in primes:
        if k+2 in primes:
            mylist.append((k,k+2))
    return mylist


def twinprimes(n):
    mylist=[]
    primes = primelist(n)
    for k in primes:
        if k+2 in primes:
            mylist.append((k,k+2))
    return mylist


# Part 1 (d)
    
#A Sophie Germain prime is a prime p where 2p + 1 is also prime. For instance, 
#3 is a Sophie Germain prime. Write a function sgprimes(n) which returns a list 
#all Sophie Germain primes up to and including n.
    
def sgprimes(n):
    mylist=[]
    primes = list(range(2,n+1))
    for i in primes:
        j=2
        while i*j<= primes[-1]:
            if i*j in primes:
                primes.remove(i*j)
            j=j+1
    germain = primes
    for k in germain:
        if (2*k) + 1 in primelist(2*n +1):
            mylist.append(k)
    return mylist

def sgprimes(n):
    mylist=[]
    germain = primelist(n)
    for k in germain:
        if (2*k) + 1 in primelist(2*n +1):
            mylist.append(k)
    return mylist

# Part 1 (e)
# A plot whose x-coordinates are the primes (up to some limit), and whose 
#y-values are the corresponding prime count. For instance the point (7, 4)
# should be plotted, since 7 is the 4th prime.
    
### We would plot different graphs with different numbers, e.g 30,100,1000

plt.figure('Figure A')
x1 = primelist(100)
y1 = list(range(1,len(primelist(100))+1))
plt.loglog(x1,y1,'g', label = 'Primes Against Their Count')
plt.legend(loc='upper left')
plt.xlabel('Prime Numbers')
plt.ylabel('Prime Count')
plt.title('Prime Numbers Against Their Count')
plt.show()

#A plot whose x-coordinates are the larger values of all pairs of twin primes, 
#and whose y-values are the corresponding twin prime count. For instance (7, 2)
# is a point to plot, since 7 is the larger of the twin pair (5, 7) which is 
#the 2nd pair of twin primes.

### Define a new function to produce a list of largest values in the twinprime
# function

def largetwinprimes(n):
    mylist=[]
    primes = list(range(2,n+1))
    for i in primes:
        j=2
        while i*j<= primes[-1]:
            if i*j in primes:
                primes.remove(i*j)
            j=j+1
    for k in primes:
        if k+2 in primes:
            mylist.append(k+2)
    return mylist

### Plot the function

plt.figure('Figure B')
x2 = largetwinprimes(100)
y2 = list(range(1,len(largetwinprimes(100))+1))
plt.loglog(x2,y2,'b', label = 'Largest Twin Primes Against Their Count')
plt.legend(loc='upper left')
plt.xlabel('Largest Twin Prime Numbers')
plt.ylabel('Prime Count')
plt.title('Largest Twin Prime Numbers Against Their Count')
plt.show()


#A plot whose x-coordinates are the Sophie Germain primes, and whose y-values 
#are the corresponding Sophie Germain prime count. For instance (3, 2) is a 
#point to plot, since 3 is the 2nd Sophie Germain prime.

plt.figure('Figure C')
x3 = sgprimes(100)
y3 = list(range(1,len(sgprimes(100))+1))
plt.loglog(x3,y3,'r', label = 'Sophie Germain Primes Against Their Count')
plt.legend(loc='upper left')
plt.xlabel('Sophie Germain Prime Numbers')
plt.ylabel('Prime Count')
plt.title('Sophie Germain Prime Numbers Against Their Count')
plt.show()

### Experiment with different plots, i.e standard, semilog plots, see how the
### graphs change - PLOT MORE THAN ONE GRAPH FOR EACH - comment on findings
# Part 1 (f) comment on your plots



#Part 2 (a)
#A pair of sexy primes1 is a pair (p, p + 6) where both coordinates are prime, 
#such as (5, 11). Write a function sexyprimes(n) which returns a list all pairs
# of sexy primes up to and including n. (Follow the same input/output format as
# previously.)

def sexyprimes(n):
    mylist=[]
    primes = list(range(2,n+1))
    for i in primes:
        j=2
        while i*j<= primes[-1]:
            if i*j in primes:
                primes.remove(i*j)
            j=j+1
    for k in primes:
        if k+6 in primes:
            mylist.append((k,k+6))
    return mylist

#Part 2 (b)
# A prime triplet is a triple of the form (p, p+2, p+6) or (p, p+4, p+6) where 
#all three entries are prime, such as (5, 7, 11). Write a function tripletprimes(n)
# which returns a list all prime triplets up to and including n. (Follow the same 
#input/output format as previously.)

def tripletprimes(n):
    mylist=[]
    primes = list(range(2,n+1))
    for i in primes:
        j=2
        while i*j<= primes[-1]:
            if i*j in primes:
                primes.remove(i*j)
            j=j+1
    for k in primes:
        if k+2 in primes and k+6 in primes:
            mylist.append((k,k+2,k+6))
    for l in primes:
        if l+4 in primes and l+6 in primes:
            mylist.append((l,l+4,l+6))
            mylist.sort()
    return mylist

#Part 2 (c)
#Notice that a prime triplet contains both a pair of twin primes and a pair of 
#sexy primes.
#Denote
#S(n) = Number of prime triplets up to n / Number of sexy primes up to n
#(n) = Number of prime triplets up to n./ Number of twin primes up to n
#Plot a graph of n against S(n), and on the same axes n against T(n), 
#up to some limit of your choice. (As in Part 1, it is sufficient to plot 
#only values of n which feature in a relevant configuration of primes.)

###Define Sn
### Start from 11 since we don't want division by 0    
    
def s_n(n):
    mylist = []
    for i in range(11,n+1):
        s = len(tripletprimes(i))/len(sexyprimes(i))
        mylist.append(s)
    return mylist

def t_n(n):
    mylist = []
    for i in range(5,n+1):
        s = len(tripletprimes(i))/len(twinprimes(i))
        mylist.append(s)
    return mylist

plt.figure('Figure D')
x4 = list(range(11,101))
y4 = s_n(100)
x5 = list(range(5,101))
y5 = t_n(100)
plt.loglog(x4,y4,'r', label = 'Sn')
plt.loglog(x5,y5,'b', label = 'Tn')
plt.legend(loc='upper left')
plt.xlabel('n')
plt.ylabel('corresponding value')
plt.title('n against Sn and Tn')
plt.show()

### Comment on graphs - change value of n, etc etc 

#Part 2 (d) Comment on your graph

#Part 3
### Primes in the form n^2 + 1 

### This is one of Landau's 4 Problems - infinitely many primes in this form
### is still unproven - unable to comment on infinte primes, etc

def squareprimes(n):
    mylist=[]
    primes = list(range(2,n+1))
    for i in primes:
        j=2
        while i*j<= primes[-1]:
            if i*j in primes:
                primes.remove(i*j)
            j=j+1
    squares = primes
    for k in squares:
        if (k**2 + 1) in primelist(n**2 + 1):
            mylist.append(k**2 + 1)
    return mylist

### Talk about lack of numbers in this form, research a bit more into it
    
#Prime quadruplets of primes of the form (p,p+2,p+6,p+8)
    
def quadprimes(n):
    mylist=[]
    primes = list(range(2,n+1))
    for i in primes:
        j=2
        while i*j<= primes[-1]:
            if i*j in primes:
                primes.remove(i*j)
            j=j+1
    for k in primes:
        if k+2 in primes and k+6 in primes and k+8 in primes:
            mylist.append((k,k+2,k+6,k+8))
    return mylist

### Look at lengths of primes for triplets, doubles, quads, etc, plot graphs, etc
    

#Strong primes: a prime p is strong, if p is nearer to the next prime than to 
#the previous prime. For example, 11 is strong as |13 − 11| > |11 − 7|.
    



def strongprimes(n):
    mylist=[]
    primes = list(range(2,n+1))
    for i in primes:
        j=2
        while i*j<= primes[-1]:
            if i*j in primes:
                primes.remove(i*j)
            j=j+1
    for i in primelist(n):
        if i > ((i+1)+(i-1))/2:
            return i
        
def strongprimes(n):
    mylist=[]
    primes = list(range(2,n+1))
    for i in primes:
        j=2
        while i*j<= primes[-1]:
            if i*j in primes:
                primes.remove(i*j)
            j=j+1
    for k in primes:
        if k > ((k+1)+(k-1))/2:
            mylist.append(k)
        k=k+1
    return mylist        




def strongprimes(n):
    for i in primelist(n):
        if i > ((i+1)+(i-1))/2:
            return i



def meanpair_or_gcd(n,m):
    if 2*gcd(n,m) > meanpair(n,m):
        return 2*gcd(n,m)
    else:
        return meanpair(n,m)


## extensions of parts 1 and 2 









