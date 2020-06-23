
# Template file for Week 3
# Lines that start with '#'
# are comments and are ignored
# by Python.

# 3A Write your functions below
# E.g., a function which takes an integer and squares it
# def squared 

def squared(x):
    xx = x**2
    return xx

## DO NOT CHANGE THE FUNCTION NAMES!! ##
# (1)  def cubed
#Here we have the function that takes x and returns x cubed:
    
def cubed(x):
    xx = x**3
    return xx

# (2) def meanpair
#The following function takes a pair of integers and returns their mean:
    
def meanpair(x,y):
    xy = (x+y)/2
    return xy

# (3) def pyth
# The following function tests whether three numbers a,b and c form 
# a Pythagorean triple:

def pyth(a,b,c):
    a < b
    b < c
    if a**2 + b**2 == c**2:
        return True
    else:
        return False

# (4) def meanlist
# The following function takes a list of inegers and returns their mean:
        
def meanlist(a):
    sum=0
    for i in a:
        sum = sum+i
    return sum/len(a)

# (5) def gcd
# The following function takes a pair of positive integers
# and returns their greatest common divisor
def gcd(a,b):
    while b > 0:
       a, b = b, a % b
    return a

# (6) def dectobin
# The following function takes a decimal integer and returns a list that
# represents the binary representation:
    
def dectobin(decimal):
    binary = []
    while decimal>0:
        binary.append(decimal%2)
        decimal=decimal//2
    binary.reverse() 
    return binary
    

# (7) def bintodec
# The following function takes a list representing a binary expression and returns
#the decimal representation:
    
def bintodec(binary):
    decimal = 0
    binary.reverse()
    for i in range (len(binary)):
        decimal = decimal + (2**i)*binary[i]
    return(decimal)

# (8) def meanpair_or_gcd
# Here we use 
# This function takes a pair of integers and returns their mean or twice their 
# greatest common divisor, whichever is the greater:
    
def meanpair(x,y):
    xy = (x+y)/2
    return xy    
    
def gcd(a,b):
    while b > 0:
       a, b = b, a % b
    return a 
    
def meanpair_or_gcd(n,m):
    if 2*gcd(n,m) > meanpair(n,m):
        return 2*gcd(n,m)
    else:
        return meanpair(n,m)
    
# 3B Write your Eratosthenes function below
# def eratosthenes(N):
# The following is my Eratosthenes function: 

def eratosthenes(N):
    primes = list(range(2,N+1))
    for i in primes:
        j=2
        while i*j <= primes[-1]:
            if i*j in primes:
                primes.remove(i*j)
            j=j+1
        return primes

# To find the 100th prime number, (assuming the first is 2), we do the
# following code:

list1=eratosthenes(600)
list1[99]

# To find the 2000th prime number we do the
# following code: 

list2=eratosthenes(20000)
list2[1999]

# The following code finds how many primes there
# are between 3000 and 30000

len(eratosthenes(30000)) - len(eratosthenes(3000))

# Answer the questions as comments below:
# 100th prime is: 514
# 2000th prime is: 17389
# Primes between 3000 and 30000: 2815
#


# 3C Write your Sundaram function below:
# def sundaram(n):
# The following is a Sundaram function:

def sundaram(n):
    list1 = list(range(1,n))
    for j in range(1, n+1):
        for i in range(1, j+1):
            if i+j+2*i*j in list1:
                list1.remove(i+j+2*i*j)
    for k in range(len(list1)):
        list1[k] = 2 * list1[k] + 1
    return list1

# We can test our function works by inputting n = 20
    
sundaram(20)
print(sundaram(20))

# This gives you the list of primes from 3 up to 2n (which in this case is 40)











