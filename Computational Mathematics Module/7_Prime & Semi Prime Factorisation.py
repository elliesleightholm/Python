# import files here

from math import sqrt
from math import floor

# 5A Write your functions below
# E.g., a function which takes an integer and squares it
# def squared 

def squared(x):
    xx = x**2
    return xx


## DO NOT CHANGE THE FUNCTION NAMES!! ##
# (1)  def semiprime_factorisation2

def semiprime_factorisation2(n):
    for i in range(2,floor(sqrt(n)+1)):
        if n % i == 0:
            return i, n//i
    

#(2) def prime_factorisation

 
def prime_factorisation(n):
    i = 2
    primefactors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            primefactors.append(i)
    if n > 1:
        primefactors.append(n)
    return primefactors            
        
        
        
        
        

