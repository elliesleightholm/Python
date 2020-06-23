
###Exercise 6A solutions 

###import modules here

import matplotlib.pyplot as plt
import numpy as np

###Exercise 6A(i)
def collatzseq(n):
    list1 = [n]
    while n !=1:
        if n < 0: 
            return 'Invalid Input'
        if n == 0:
            return 'Invalid Input'
        if n % 2 == 0:
            n = n // 2
            list1.append(n)
        else:
            n = n * 3 + 1
            list1.append(n)
    return list1

###Exercise 6A(ii)
def collatzcount(n):
    count = 0
    while n != 1:
        if n < 0:
            return 'Invalid Input'
        if n == 0:
            return 'Invalid Input'
        if n % 2 == 0:
           n = n // 2
           count  += 1
        else:
            n = n * 3 + 1
            count += 1
    return count

###Exercise 6A(iii)
###Write your code that plots your graph here (not commented out)

list2=[]
for n in range (0,1000):
    n = n+1
    list2.append(collatzcount(n))
    
list3=list(range(1,1001))

plt.figure('Figure A')
plt.scatter(list3,list2,s=10)
plt.xlabel('n (from 1 to 1000)')
plt.ylabel('Number of Steps Until the Sequence Reaches 1')
plt.title('Figure A - Number of Steps in Collatz Sequence against n')

#From this graoh we see that the number of steps in the Collatz Sequence for 
#n between 1 and 1000 is less than 200. We can also observe how spread the 
#circles are on the graph. However, the circles appear to come in clusters.

    
###Exercise 6A(iv)
###Write your answer as a comment here (including including any code you used to obtain it but commented out.)
    
#In order to calculate what percentage of initial values, n, have the property
#that s(n) (as demonstrated by the code in 6A(ii)) is less than n/10 for 
# n between 1 and 1000, we must create the following python command:
#First we define an empty set, in this case, list4:

#list4 = []

# We define n in the region we require. Then we tell Python to append 
#collatzcount(n) to our empty list if collatzcount(n) < n/10 as follows:

#for n in range (1,1001):
#    if collatzcount(n) < n/10 :
#        list4.append(collatzcount(n))
#print(len(list4))
#print(len(list4)/1000) 

#Finally, we command Python to return the length of this list. This will give
# us the number of values of n for which s(n) < n/10. In this case we get 
# 443.
# We know we are using n in the range 1 to 1000 so we simply divide 443 by 1000
# to get our percentage (as seen in the Python command above).
# Therefore, we get that the percentage is 0.443 or 44.3%.   

###Exercise 6A(v)

###Write your code that plots your graph(s) here (not commented out)

#In order to plot this particular function, I decided to create a function,
# maximum, whereby when you input a particular value of n, it gives the 
# highest term in the Collatz's Sequence for that particular n. For example,
# maximum(11) gives the output 52. 
# I then take all outputs of this function from 1 to 1000 and append each of 
# then individually to an empty list. The code for this can be seen below. 
# This gives a list of the maximum element in the Collatz's sequence for n 
# between 1 and 1000.
# Finally, I create a scatter plot (we aren't interested in a continous 
# function so a scatter plot is the most suitable plot) for the list I just
# created and the list of n between 1 and 1000.

def collatz(number):
    if number % 2 == 0:
        return number // 2
    elif number % 2 == 1:
        return 3 * number + 1
    
def maximum(n):
    m = 0
    while n != 1:
        if n > m: m = n
        n = collatz(int(n))
    return m

list5=[]
for n in range (0,1000):
    n = n+1
    list5.append(maximum(n))
    
list3=list(range(1,1001))

plt.figure('Figure B')
plt.scatter(list3,list5,s=10)
plt.xlabel('n (from 1 to 1000)')
plt.ylabel('Maximum value in Collatz Sequence')
plt.title('Figure B - Maximum value in Collatz Sequence against n')


#Write your observations (as a comment) here

# Immediately, we can see that we have 3 extremely large values in our graph.
# These values of n lie in the 15,000 to 25,000 range for the maximum value. 
# We can overcome these anomalies by changing our y range.

plt.figure('Figure C')
plt.scatter(list3,list5,s=10)
plt.xlabel('n (from 1 to 1000)')
plt.ylabel('Maximum value in Collatz Sequence, for max(n) < 1000')
plt.title('Figure C - Maximum value in Collatz Sequence against n')
plt.ylim([0,1000])

plt.figure('Figure D')
plt.scatter(list3,list5,s=10)
plt.xlabel('n (from 1 to 1000)')
plt.ylabel('Maximum value in Collatz Sequence, for max(n) < 2000')
plt.title('Figure D - Maximum value in Collatz Sequence against n')
plt.ylim([0,2000])

plt.figure('Figure E')
plt.scatter(list3,list5,s=10)
plt.xlabel('n (from 1 to 5000)')
plt.ylabel('Maximum value in Collatz Sequence, for max(n) < 5000')
plt.title('Figure E - Maximum value in Collatz Sequence against n')
plt.ylim([0,5000])


# From these plots we can see that the scatter graph has positive correlation.
# Suggesting that, on average, increasing the value of n will result in a 
# higher maximum element within the Collatz's Sequence.

# Finally, we can experiment with drawing different lines to see where the
# points in the scatter graph lie. 
    
plt.figure('Figure F')
plt.scatter(list3,list5,s=10)
plt.xlabel('n (from 1 to 1000)')
plt.ylabel('Maximum value in Collatz Sequence for max(n) < 100,000')
plt.title('Figure F - Maximum value in Collatz Sequence against n')    
x = np.arange(0, 1000, 0.1)
y = x ** 1
plt.figure('Figure F')
plt.loglog(x, y,'r')
x = np.arange(0, 1000, 0.1)
y = x ** 0.9
plt.figure('Figure F')
plt.loglog(x, y,'g')
x = np.arange(0, 1000, 0.1)
y = x ** 0.5
plt.figure('Figure F')
plt.loglog(x, y,'y')
x = np.arange(0, 1000, 0.1)
y = x ** 3
plt.figure('Figure F')
plt.loglog(x, y,'c')
plt.ylim([0,100000])


# The code above produces Figure F. 
# In Figure F, we have the following lines:
# Red Line = gradient 1 (y = x)
# Green Line = gradient 0.9 (y = 0.9x)
# Yellow Line = gradient 0.5 (y = 0.5x)
# Cyan Line = gradient 3 (y = 3x)
# Observing these lines along with the data, we can see that all data points
# lie above or on the line y = 0.9x, this confirms our belief that, for n
# between 1 and 1000, the more you increase the value of n, the larger the 
# highest term in the sequence is. 
# Furthermore, no points lie above y = 3x either. This suggests that the data
# is growing at a constant rate and therefore, has positive correlation.

#R##eminder: check your programme runs before submission! Your code should generate any 
#figures when run
    
    
    
    
    
    
    