#Template for Week 8 Exercises

# import files here
import time
import random
import matplotlib.pyplot as plt

# Question 1 code

#First we define our Selection Sort algorithm as follows:

def selectionsort(mylist):
    sortedlist = []
    while len(mylist) > 0:
        lowest = mylist [0]
        for x in mylist:
            if x < lowest:
                lowest = x
        sortedlist.append(lowest)
        mylist.remove(lowest)
    return sortedlist

#We then create a list with the ith entry corresponding to the time taken for
#Python to sort the list of length 2^i using Selection Sort. We did this as
#follows:    

ivalues = []
sorttimelist = []
for i in range(1, 11):
    ivalues.append(2**i)
    mylist = list(range(2**i))
    random.shuffle(mylist)
    time_start = time.perf_counter()
    selectionsort(mylist)
    time_end = time.perf_counter()
    sorttime = time_end - time_start
    sorttimelist.append(sorttime)
    
#This gives the list of times taken for each list.
   

# Question 2 code
    
#Here we plot the Selection Sort time against 2^i

plt.figure()
x = list(2**i for i in range(1,11))
y1 = sorttimelist
plt.loglog(x,y1, label = 'Selection Sort')
plt.xlabel('Length of a List in the Form 2^i for i Between 0 and 10')
plt.ylabel('Time Taken to Sort List')
plt.title('Figure A - Time Taken to Sort Lists of Length 2^i using Selection Sort')
plt.show()

# Question 2 comment

# On a loglog graph the gradient of a line represents the corresponding power 
# of the elements. For example, a graph of O(n^2) on a loglog plot would be a 
# line of gradient 2. For O(n^3), it would be a line of gradient 3 and so on. 
# Therefore, when analysing our graph, it is important that the gradient 
# does not exceed that of 2. For an algorithm to be O(n^2) it means that, 
# in our case, the Selection Sort Time graph will not grow any faster than n^2.
# Looking at our graph we see that this is not the case, it does not exceed
# a gradient of 2 and therefore, we can conclude that the selection sort is
# O(n^2) algorithm.
# We can also observe this by plotting a line of gradient 2. When doing so
# we see that our Selection Sort graph lies either on or below the line.


#Question 3 code for bubblesort:

#Next, we define our Bubble Sort algorithm as follows:

def bubblesort(mylist):
    for i in range(0,len(mylist)-1):
        for j in range(0,len(mylist)-1-i):
            if mylist[j] > mylist[j+1]:
                mylist[j],mylist[j+1] = mylist[j+1], mylist[j]
    return mylist


# Question 4 code 
    
# We follow the same process as above and create a list with the ith entry 
# corresponding to the time taken for Python to sort a list of length 2^i 
# using Bubble Sort.    

jvalues = []
sorttimelist1 = []
for j in range(1, 11):
    jvalues.append(2**j)
    mylist1 = list(range(2**j))
    random.shuffle(mylist1)
    time_start1 = time.perf_counter()
    bubblesort(mylist1)
    time_end1 = time.perf_counter()
    sorttime1 = time_end1 - time_start1
    sorttimelist1.append(sorttime1)

#Here we plot t_b(i) on the same graph as t_s(i):

plt.figure()
y2 = sorttimelist1
x,y1,y2 = [2**i for i in range(1,11)],y1,y2
plt.loglog(x, y1, label = 'Selection Sort')
plt.loglog(x, y2, label = 'Bubble Sort')
plt.legend(loc='upper left')
plt.xlabel('Length of a List in the Form 2^i for i Between 0 and 10')
plt.ylabel('Time Taken to Sort List')
plt.title('Time Taken to Sort Lists of Length 2^i')
plt.show()

#Question 5 code 

#Next, we define our Merge Sort algorithm as follows:

def mergesort(mylist):
    if len(mylist) <= 1:
        return mylist
    
    m = len(mylist) // 2
    l = mergesort(mylist [:m])
    r = mergesort(mylist[m:])
    
    result = []
    i=j=0
    while (len(result)<len(r)+len(l)):
        if l[i] < r[j]:
            result.append(l[i])
            i = i+1
        else :
            result.append(r[j])
            j = j+1
        if i == len(l) or j == len(r):
            result.extend(l[i:] or r[j:])
            break
    return result


# Again, we create a list with the ith entry corresponding to the time taken
# for Python to sort a list of length 2^i using Merge Sort.  

kvalues = []
sorttimelist2 = []
for k in range(1, 11):
    kvalues.append(2**k)
    mylist2 = list(range(2**k))
    random.shuffle(mylist2)
    time_start2 = time.perf_counter()
    mergesort(mylist2)
    time_end2 = time.perf_counter()
    sorttime2 = time_end2 - time_start2
    sorttimelist2.append(sorttime2)
    
#Here we plot t_m(i) on the same graph as t_s(i) and t_b(i):   
    
plt.figure()
y3 = sorttimelist2
x,y1,y2,y3 = [2**i for i in range(1,11)],y1,y2,y3
plt.loglog(x, y1, label = 'Selection Sort')
plt.loglog(x, y2, label = 'Bubble Sort')
plt.loglog(x, y3,label = 'Merge Sort')
plt.legend(loc='upper left')
plt.xlabel('Length of a List in the Form 2^i for i Between 0 and 10')
plt.ylabel('Time Taken to Sort List')
plt.title('Time Taken to Sort Lists of Length 2^i')
plt.show()

#Question 5 comment 

# Despite some initial overlapping between the Merge Sort graph and the 
# Selection Sort graph which is an O(n^2) algorithm, we see that the Merge
# Sort graph's gradient begins to decrease in comparison to the Selection
# Sort graph. If an algorithm is faster than O(n^2) then the gradient of the
# algorithm's function will be less than 2. We can observe this by increasing 
# the range of i - as you increase i the gradient of the Merge Sort graph drops 
# below 2. Since the gradient is less than two and by observation, the Merge 
# Sort graph is below the Selection sort graph we can confirm that the Merge 
# Sort is faster than O(n^2).
  

#Question 6 code

## We create a list with the ith entry corresponding to the time taken
# for Python to sort a list of length 2^i using its own built in algorithm,
# Timsort defined under 'sorted' in Python. We do this as follows:  

lvalues = []
sorttimelist3 = []
for l in range(1, 11):
    lvalues.append(2**l)
    mylist3 = list(range(2**l))
    random.shuffle(mylist3)
    time_start3 = time.perf_counter()
    sorted(mylist3)
    time_end3 = time.perf_counter()
    sorttime3 = time_end3 - time_start3
    sorttimelist3.append(sorttime3)
    
# We now plot the Merge Sort and Timsort on the same graph and observe any
# differences:
    
plt.figure()
y4 = sorttimelist3
x,y3,y4 = [2**i for i in range(1,11)],y3,y4
plt.loglog(x, y3,label = 'Merge Sort')
plt.loglog(x, y4, label = 'Timsort')
plt.legend(loc='upper left')
plt.xlabel('Length of a List in the Form 2^i for i Between 0 and 10')
plt.ylabel('Time Taken to Sort List')
plt.title('Time Taken to Sort Lists of Length 2^i')
plt.show()


#Question 6 comment

# Yes - we plot the graph of Python's built-in algorithm's times to sort code
# against our Merge Sort algorithm graph and notice that the Timsort graph is 
# below the Merge Sort graph. In general, a lower gradient in this case means a
# quicker sort time. For every list of length 2^i for i between 1 and 10, it 
# takes the Timsort code less time to sort in comparison to the Merge sort. This
# can be observed by looking at the graph and noticing that the Timsort graph
# is below the Merge Sort graph. 
# Overall, since the Timsort graph has smaller gradients and is below
# the Merge Sort graph we can conclude that the Timsort graph is more efficient
# and quicker than the Merge Sort.


#Question 7 code

# Here we define our countingsort alogirthm:

def countingsort(mylist):
    N = max(mylist)
    bucketlist = [0 for i in range(0,N+1)]
    for j in mylist:
            bucketlist[j] = bucketlist[j] + 1
    returnlist = []
    for i in range(len(bucketlist)):
        returnlist.extend([i]*bucketlist[i])
    return returnlist

#Question 8 comment
    
# We can do the same as before and plot the graph for the Counting Sort 
# algorithm onto our previous graphs and observe where it lies in relation
# to the others. To do this, I input the following:
    
# This code creates a list with the ith entry corresponding to the time taken
# for Python to sort a list of length 2^i using Counting Sort. 

mvalues = []
sorttimelist4 = []
for m in range(1, 11):
    mvalues.append(2**m)
    mylist4 = list(range(2**m))
    random.shuffle(mylist4)
    time_start4 = time.perf_counter()
    countingsort(mylist4)
    time_end4 = time.perf_counter()
    sorttime4 = time_end4 - time_start4
    sorttimelist4.append(sorttime4)
    
# Next, we plot Counting Sort onto our graph with the following code:
    
plt.figure()
y6 = sorttimelist4
x,y1,y2,y3,y4,y6 = [2**i for i in range(1,11)],y1,y2,y3,y4,y6
plt.loglog(x,y1, label = 'Selection Sort')
plt.loglog(x,y2, label = 'Bubble Sort')
plt.loglog(x,y3,label = 'Merge Sort')
plt.loglog(x,y4, label = 'Timsort')
plt.loglog(x,y6, label = 'Counting Sort')
plt.legend(loc='upper left')
plt.xlabel('Length of a List in the Form 2^i for i Between 0 and 10')
plt.ylabel('Time Taken to Sort List')
plt.title('Comparison of all Algorithms')
plt.show()

# This produces a graph with the Counting Sort algorithm above the Timsort
# graph but lower than the others. From this, we can conclude that the 
# Counting Sort is more efficient than Selection Sort, Bubble Sort and 
# Merge Sort but isn't as efficient as the Timsort. We can also confirm our
# observation by observing the gradients of the graphs:
# Timsort has the lowest gradient followed closely by Counting Sort whereas
# the gradients of the other graphs are steeper. This, along with the position
# of the graphs allows us to confirm that Counting Sort is the second most 
# efficient algorithm.

# An example of where the Counting Sort Algorithm would be very ineffecient
# would be the list [1,100000000000]. This is because the algorithm would have
# to create a list of 100,000,000,000 zeros and then go through each of these
# individually when following the algorithm. This is an extremely long and 
# unnecessary way of sorting a list like this. The algorithm fails because of 
# the large range between the values. 

# To overcome the problem above we would simply have to reduce the range between
# values in the list. For example, the list [1,2,3] would be efficiently ordered
# by the Counting Sort Algorithm as the range between values is small and the 
# list is also small. So, an example of where the Counting Sort Algorithm 
# would be efficient would be the list [1,2,3]
    

    