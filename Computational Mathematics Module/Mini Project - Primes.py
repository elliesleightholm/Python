
#Patterns in the Primes MATH2920 Miniproject Template File

#import files here
import matplotlib.pyplot as plt

#Part 1
#Q1(a)
# Here, we define the function primelist which produces a list of prime 
# numbers up to and including n. We do this as follows:

def primelist(n):
    primes = list(range(2,n+1))
    for i in primes:
        j=2
        while i*j<= primes[-1]:
            if i*j in primes:
                primes.remove(i*j)
            j=j+1
    return primes

#Q1(b)
# Now, we call our function with the command primes = primelist(N). We
# choose a suitable value for N. We observed the programme's total 
# running time when inputting different values of N and observed that 
# N = 100 is suitable. Since we are using the command later when plotting
# graphs, 100 is also a suitable value. So we write the following:

N = 100
primes = primelist(N)


#Q1(c)
# We now write a function, twinprimes, that returns a list of all pairs of 
# twin primes up to and including n. To do this, we can use our primelist
# function as defined above. Using this, we can code the function twinprimes
# as follows:

def twinprimes(n):
    mylist=[]
    primes = primelist(n)
    for k in primes:
        if k+2 in primes:
            mylist.append((k,k+2))
    return mylist


#Q1(d)
# Now, we consider the Sophie Germain prime. This a prime, p, where 2p + 1
# is also a prime number. To write a function, sgprimes, that returns Sophie Germain 
# primes up to and including n, we can use our primelist function again. So,
# the Sophie Germain function is as follows:
    
def sgprimes(n):
    mylist=[]
    germain = primelist(n)
    for k in germain:
        if (2*k) + 1 in primelist(2*n +1):
            mylist.append(k)
    return mylist

#Q1(e)
# We are now required to observe the functions defined above. 
# Firstly, we form a plot whose x-coordinates are the primes up to a certain 
# limit and whose y-values are the corresponding prime count. Before plotting 
# our graph we must consider a suitable limit for our primes. We do not want 
# to use an excessive amount of primes because we may miss any patterns that
# arise in the graph. Similarly, we don't want to use a limited amount of 
# primes as, again, we may miss any patterns. In order to find a suitable limit,
# we consider the length of the primelist function for varied n. 

# First, we take n = 100 and input:
    # len(primelist(100))
# This gives 25
    
# 25 seems a suitable lower limit but to observe the graphs fully we decide to plot 
# multiple graphs for different values of n. We will take n=100,n=200 and n = 500. 

# Furthermore, we must consider which plots are suitable to observe any 
# pattern changes. Therefore, for n = 100, we will plot three graphs, one that
# is loglog, one semilog and one standard and decide which is best to observe
# patterns from. 
    
# Figure A will be primes up to and including 100 against their count on a 
# loglog graph:
    
plt.figure('Figure A')
# Since we defined primes above we can substitute primes for our x value
x1 = primes
y1 = list(range(1,len(primes)+1))
plt.loglog(x1,y1,'g^-', label = 'Primes Against Their Count on a LogLog Graph')
plt.legend(loc='upper left')
plt.xlabel('Prime Numbers')
plt.ylabel('Prime Count')
plt.title('Prime Numbers Against Their Count')
plt.show()

#Figure B will be primes up to and including 100 against their count on a 
# semilog graph:

plt.figure('Figure B')
x1 = primes
y1 = list(range(1,len(primes)+1))
plt.semilogy(x1,y1,'g^-', label = 'Primes Against Their Count on a SemiLog Graph')
plt.legend(loc='upper left')
plt.xlabel('Prime Numbers')
plt.ylabel('Prime Count')
plt.title('Prime Numbers Against Their Count')
plt.show()

#Figure C will be primes up to and including 100 against their count on a 
# standard graph:

plt.figure('Figure C')
x1 = primes
y1 = list(range(1,len(primes)+1))
plt.plot(x1,y1,'g^-', label = 'Primes Against Their Count on a Standard Graph')
plt.legend(loc='upper left')
plt.xlabel('Prime Numbers')
plt.ylabel('Prime Count')
plt.title('Prime Numbers Against Their Count')
plt.show()

# After observing the three graphs, we notice that the standard plot gives 
# the easiest readings with the x and y axis suitably labelled. 

#Now, we form three additional standard plots for varying sizes of n.

# For primes up to and including 100:
plt.figure('Figure D')
x1 = primes
y1 = list(range(1,len(primes)+1))
plt.plot(x1,y1,'g^-', label = 'Primes Against Their Count')
plt.legend(loc='upper left')
plt.xlabel('Prime Numbers')
plt.ylabel('Prime Count')
plt.title('Types of Prime Numbers up to 100 Against Their Count')
plt.show()

# For primes up to and including 200:
plt.figure('Figure E')
x1 = primelist(200)
y1 = list(range(1,len(primelist(200))+1))
plt.plot(x1,y1,'g^-', label = 'Primes Against Their Count')
plt.legend(loc='upper left')
plt.xlabel('Prime Numbers')
plt.ylabel('Prime Count')
plt.title('Types of Prime Numbers up to 200 Against Their Count')
plt.show()

#For primes up to and including 500:
plt.figure('Figure F')
x1 = primelist(500)
y1 = list(range(1,len(primelist(500))+1))
plt.plot(x1,y1,'g^-', label = 'Primes Against Their Count')
plt.legend(loc='upper left')
plt.xlabel('Prime Numbers')
plt.ylabel('Prime Count')
plt.title('Types of Prime Numbers up to 500 Against Their Count')
plt.show()

# Now we plot a graph whose x-coordinates are the larger values of all pairs 
# of twin primes, and whose y-values are the corresponding twin prime count. In
# order to do this, we decided to define a new function that produces a list 
# of the larger values of all pairs of twin primes. We did this as follows:

def largetwinprimes(n):
    mylist=[]
    primes = primelist(n)
    for k in primes:
        if k+2 in primes:
            mylist.append(k+2)
    return mylist

# Now, we plot the function for n = 100, n = 200, n = 500 on the same Figures 
# (D, E and F) so that we are able to observe any differences between the 
# different types of primes. 
    
# Plotting the larger values of pairs of twin primes for n = 100 on the same
# graph as the normal primes:
plt.figure('Figure D')
x2 = largetwinprimes(100)
y2 = list(range(1,len(largetwinprimes(100))+1))
plt.plot(x2,y2,'b^-', label = 'Largest Twin Primes Against Their Count')
plt.legend(loc='upper left')
plt.xlabel('Prime Numbers')
plt.ylabel('Prime Count')
plt.title('Types of Prime Numbers up to 100 Against Their Count')
plt.show()

# Plotting the larger values of pairs of twin primes for n = 200 on the same
# graph as the normal primes:
plt.figure('Figure E')
x2 = largetwinprimes(200)
y2 = list(range(1,len(largetwinprimes(200))+1))
plt.plot(x2,y2,'b^-', label = 'Largest Twin Primes Against Their Count')
plt.legend(loc='upper left')
plt.xlabel('Prime Numbers')
plt.ylabel('Prime Count')
plt.title('Types of Prime Numbers up to 200 Against Their Count')
plt.show()

# Plotting the larger values of pairs of twin primes for n = 500 on the same
# graph as the normal primes:
plt.figure('Figure F')
x2 = largetwinprimes(500)
y2 = list(range(1,len(largetwinprimes(500))+1))
plt.plot(x2,y2,'b^-', label = 'Largest Twin Primes Against Their Count')
plt.legend(loc='upper left')
plt.xlabel('Prime Numbers')
plt.ylabel('Prime Count')
plt.title('Types of Prime Numbers up to 500 Against Their Count')
plt.show()

# Now we plot a graph whose x-coordinates are the Sophie Germain primes, 
# and whose y-values are the corresponding Sophie Germain prime count. We
# follow the same process as before, observing the Sophie Germain primes for
# different values of n and plot these graphs on the same graphs as the normal
# primes and largest pair of the twin primes. 

# Plotting the Sophie Germain primes for n = 100 on the same graph as the 
# normal primes and largest value of twin primes:
plt.figure('Figure D')
x3 = sgprimes(100)
y3 = list(range(1,len(sgprimes(100))+1))
plt.plot(x3,y3,'r^-', label = 'Sophie Germain Primes Against Their Count')
plt.legend(loc='upper left')
plt.xlabel('Prime Numbers')
plt.ylabel('Prime Count')
plt.show()

# Plotting the Sophie Germain primes for n = 200 on the same graph as the 
# normal primes and largest value of twin primes:
plt.figure('Figure E')
x3 = sgprimes(200)
y3 = list(range(1,len(sgprimes(200))+1))
plt.plot(x3,y3,'r^-', label = 'Sophie Germain Primes Against Their Count')
plt.legend(loc='upper left')
plt.xlabel('Prime Numbers')
plt.ylabel('Prime Count')
plt.show()

# Plotting the Sophie Germain primes for n = 500 on the same graph as the 
# normal primes and largest value of twin primes:
plt.figure('Figure F')
x3 = sgprimes(500)
y3 = list(range(1,len(sgprimes(500))+1))
plt.plot(x3,y3,'r^-', label = 'Sophie Germain Primes Against Their Count')
plt.legend(loc='upper left')
plt.xlabel('Prime Numbers')
plt.ylabel('Prime Count')
plt.show()


#Q1(f)
#Comment:
# Since we have multiple graphs we are able to observe any patterns in our
# graphs thoroughly. First, we will talk about each of the graphs individually 
# then go on to compare against the others. 

# First, we look at the prime against prime count graph, denoted in green
# on Figures D, E and F. We will start with n = 100 and observe any changes as
# n is increased. In Figure D, we observe the frequency of the primes between 
# 1 and 100. The count reaches 25 which means we have 25 primes in the first 
# 100 integers, this implies that 25 percent of integers between 1 and 100 are 
# prime. Is this a phenomenon that always arises? In order to answer this 
# question we must observe our other graphs. In Figure E, the count reaches 46
# which implies 23 percent of integers between 1 and 200 are prime. In Figure
# F, the count reaches 95 which implies 19 percent of integers between 1 and 
# 500 are prime. This answers our question. Although it would be remarkable 
# if it were true, a quarter of all numbers are indeed, not prime. We notice the 
# decrease in percentage of primes as we increase the number of n. So, we have
# observed that as you increase n, the count of n increases but at a slower rate
# than for smaller n. In other words, the primes become less frequent as you 
# increase n. 

# Now, we look at the largest value of all pairs of twin primes, denoted in
# blue on Figures D,E and F. We can follow a similar approach above and observe
# how frequent these primes are. In figure D, we notice that the count is 8.
# So, roughly 8 percent of integers between 1 and 100 are the upper value of a 
# pair of twin primes. Similarly, in Figure E and F we have the counts 15 and
# 24 respectively. Implying 7.5% of integers between 1 and 200 and 4.8% of 
# integers between 1 and 500 are of this type of prime. Again, we notice a 
# decrease in the frequency of these primes as we increase the value of n. This
# can also be observed by the sudden stop in the graph in Figure D, there is no
# value between 74 and 100 which further confirms the lowered frequency as n is
# increased. 

# We now observe the Sophie Germain primes, as denoted in red in our graphs. 
# Again, we follow a similar method above and observe the count for Sophie 
# Germain primes as n increases. In Figure D,E and F we notice that the count 
# reaches 10, 15 and 25. Again, we observe the decrease in the percentage 
# of Sophie Germain primes as n is increased. 

# We can now look at the graphs together. In Fig D,E and F we notice the
# prominence of our green graph, the prime against prime count. In comparison 
# to the other graphs it is considerably higher, implying that for each range
# of n (100,200 and 500) prime numbers occur more frequently than Sophie 
# Germain primes and largest paired value twin primes. In fact, in all graphs
# there are more primes than the product of the other two types of primes. 

# We can now compare the Sophie Germain primes with the largest paired value
# twin primes. In Fig D we observe that the count of Sophie Germain primes is 
# higher and extends further than the blue graph. However, as we begin to 
# increase the value of n, our two graphs begin to become closer until they
# considerably overlap in Fig F. This suggests that as you increase the value 
# of n, the count for these two types of primes become equal. 

# We could also try observe any patterns we see in terms of difference
# between values. For example, whether the values for each type of primes 
# increases by the same amount. We could observe this by looking at the length
# of the straight lines in our plots. However, we notice that there is no
# pattern. All types of primes increase to the next value by varying values
# each time so there is no similarity in the rate of increase between primes. 
# Equally, we can argue that the difference between primes for all types of primes 
# does not follow a particular pattern. 

# To conclude, we have observed that for all the types of primes investigated,
# their frequency becomes less as we increase the value of n. Furthermore, 
# primes occur much more frequently than Sophie Germain primes and largest
# paired value twin primes. Finally, we observed that as n is increased, 
# Sophie Germain primes and largest paired value twin primes eventually 
# have the same count. 
    
#Part 2
#Q2(a)
# We now define a function that returns sexy primes, i.e primes in the form
# (p, p+6). We use the primelist function defined above:

def sexyprimes(n):
    mylist=[]
    primes = primelist(n)
    for k in primes:
        if k+6 in primes:
            mylist.append((k,k+6))
    return mylist

#Q2(b)
# Now we define a function that returns prime triples, i.e primes in the form
# (p, p+2, p+6) or (p, p+4, p+6) where all three entries are prime. We do this 
# as follows:
    
def primetriplets(n):
    mylist=[]
    primes = primelist(n)
    for k in primes:
        if k+2 in primes and k+6 in primes:
            mylist.append((k,k+2,k+6))
    for l in primes:
        if l+4 in primes and l+6 in primes:
            mylist.append((l,l+4,l+6))
            mylist.sort()
    return mylist

#Q2(c)
# We must now plot a graph of n against Sn and n against Tn where Sn is defined
# as:
# Sn = (number of prime triplets up to n)/(number of sexy primes up to n)
# and Tn is defined as:
# Tn = (number of prime triplets up to n)/(number of twin primes up to n)
    
# In order to plot these graphs, we decide to create functions for Sn and Tn.
# First, we must consider the values of n that are appropriate for this function.
# Obviously, between n = 1 and n = 10 there are no sexy primes. So Sn would be
# divided by 0 which we don't want. So we decide to start our function at 11. 
# We define the function Sn as follows:
    
def s_n(n):
    mylist = []
    for i in range(11,n+1):
        s = len(primetriplets(i))/len(sexyprimes(i))
        mylist.append(s)
    return mylist

# Similarly, for Tn, betwen n = 1 and n = 4, there are no twin primes. So in
# our function, we will start it at 5. 
# We define the function Tn as follows:
    
def t_n(n):
    mylist = []
    for i in range(5,n+1):
        s = len(primetriplets(i))/len(twinprimes(i))
        mylist.append(s)
    return mylist

# Now we have defined the functions, we can plot. We take n = 200. After plotting
# different values of n, this seemed the most suitable - it allows us to observe
# the data on a larger scale but also notice any intricate patterns that may 
# arise. 
# We plot the graph as follows:

plt.figure('Figure G')
xs = list(range(11,201))
ys = s_n(200)
xt = list(range(5,201))
yt = t_n(200)
plt.plot(xs,ys,'r', label = 'Sn')
plt.plot(xt,yt,'b', label = 'Tn')
plt.legend(loc='upper left')
plt.xlabel('n')
plt.ylabel('Corresponding Value')
plt.title('n against Sn and Tn')
plt.show()

# Since we have used all values of n, it is easy to depict which values are prime
# by observing the straight lines in the graph. 

#Q2(d)
#Comment:    
# As a reuslt, python produces some very interesting graphs that we are able
# to analyse. The first thing we can comment on is the sharp inclines and
# declines as well as straight lines that are present in both graphs. This 
# suggests that the functions Sn and Tn do not follow a particular pattern - 
# they are irregular. Furthermore, we can observe that there are no pointed
# peaks and troughs, this suggests that when the value of Tn or Sn increases/
# decreases, it stays at that particular value before increasing/decreasing 
# again. This may be because of the large range between the different primes. 
# Take n = 13 to n = 16 for example, the number of prime triplets is 2 for all
# of these values of n and similarly, the number of sexy primes is also 2. This
# is why we get a straight line at y = 1 between n = 13 and n = 16. This 
# happens frequently in both Sn and Tn since the prime triplets, sexy primes
# and twin primes are so spread apart, particularly between non-primes, like 
# 14, 15 and 16 in our example. 

# Furthermore, we can comment on the corresponding value for Sn and Tn. 
# Immediately, we can observe that Tn begins at 0 and rapidly increases to 1
# between n = 5 and n = 17. After that it moves above and below 1 and begins 
# to decrease below 1 after n = 180. This suggests that, on average, the 
# number of prime triplets and twin primes are equal for each value of n. 
# However, when we plot the graph for n = 1000, we notice that as n increases,
# the value of Tn drops below 1 which suggests that as n increases, the number
# of prime triplets is lower than the number of twin primes. 

# Similarly, for Sn, we notice that the graph begins at 1 and quickly decreases.
# It moves slightly above and below the 0.5 mark. We observe the graph for 
# n = 1000 and notice that it continues to drop lower as n increases. This 
# suggests that, on average, the number of prime triplets is less than half that 
# compared to sexy primes. Therefore, we can conclude that there are more sexy
# primes in comparison to twin primes for our particular value of n.

    

##Part 3
# For Part 3, we are asked to continue our investigation of patterns in
# the prime numbers. As a result, we will be observing primes in the form 
# n^2 + 1 where n is an integer and Mersenne primes and looking at any 
# similarities or differences. We will then explore methods we have used in 
# previous workshops/lectures to observe the patterns of prime numbers in 
# Fibonacci sequences. 

# First, we explore primes in the form n^2 + 1. In order to do this, we 
# create the following function:

def squareprimes(n):
    mylist=[]
    squares = primelist(n)
    for i in range(1,n+1):
        if (i**2 + 1) in squares:
            mylist.append(i**2 + 1)
    return mylist

# This produces a list of primes, in the form n^2 + 1 up to and including n.

# We can look into the length of this function for particular values of n to 
# see how frequently these types of primes occur. 
# Let's take n = 10, n = 50, n = 100 and n = 1000. So,
    
#    len(squareprimes(10)) 
#    len(squareprimes(50))
#    len(squareprimes(100))
#    len(squareprimes(1000))
    
# We get 2,4,4 and 10 respectively so immediately, we can see that primes of 
# this form aren't particularly frequent, especially against sexy and twin primes. 
# This seems intuitive since half of squared numbers are odd so adding 1 would
# give an even number which certainly isn't prime. Furthermore, since square
# numbers become further spread apart, we can say that primes in the form 
# n^2 + 1 will also become further spread apart. 

# Now, we consider Mersenne primes and plot these primes against
# primes in the form n^2 + 1. Mersenne primes are primes in the form 2^n - 1 
# and are widely studied because of their connection to perfect numbers. 

# We must write a function for primes in the form 2^n - 1. 
# We do this as follows:
    
def mersenneprimes(n):
    mylist=[]
    mersenne = primelist(n)
    for i in range(1,n+1):
        if (2**i - 1) in mersenne:
            mylist.append(2**i - 1)
    return mylist

# This produces a list of all Mersenne primes up to and including n.

# As above, we can now look into the length of this function for different 
# values of n to see how frequently Mersenne primes occur. 

# Let's take n = 10, n = 50, n = 100 and n = 1000. So,
    
#    len(mersenneprimes(10)) 
#    len(mersenneprimes(50))
#    len(mersenneprimes(100))
#    len(mersenneprimes(1000))
    
# We get 2,3,3 and 4 respectively. Similar to primes in the form n^2 + 1, 
# Mersenne primes aren't very frequent. In fact, they are less frequent than
# primes in the form n^2 + 1. This is why we chose to observe these two 
# particular types of primes because they appear so rarely. 
    
# Since all primes greater than 2 are odd, one would think that Mersenne primes
# would occur more frequently than primes of the form n^2 + 1 purely because 
# 2^n - 1 will always be odd whereas half of the numbers in the form n^2 + 1 
# are even. However, we have shown that this is clearly not the case. 
    
# Now, we plot these primes on a graph and observe any differences. We do this
# as follows:
    
# First we will plot Mersenne primes vs primes in the form n^2 + 1 for n = 100 
plt.figure('Figure H')
xsquare = squareprimes(100)
ysquare = list(range(1,len(squareprimes(100))+1))
xmersenne = mersenneprimes(100)
ymersenne = list(range(1,len(mersenneprimes(100))+1))
plt.plot(xsquare,ysquare,'c^-', label = 'Primes in the Form n^2 + 1')
plt.plot(xmersenne,ymersenne,'r^-', label = 'Mersenne Primes')
plt.legend(loc='upper left')
plt.xlabel('Type of primes')
plt.ylabel('Prime Count')
plt.title('Mersenne Primes vs Primes in the Form n^2 + 1')
plt.show()

# Now we will plot for n = 500 
plt.figure('Figure I')
xsquare1 = squareprimes(500)
ysquare1 = list(range(1,len(squareprimes(500))+1))
xmersenne1 = mersenneprimes(500)
ymersenne1 = list(range(1,len(mersenneprimes(500))+1))
plt.plot(xsquare1,ysquare1,'c^-', label = 'Primes in the Form n^2 + 1')
plt.plot(xmersenne1,ymersenne1,'r^-', label = 'Mersenne Primes')
plt.legend(loc='upper left')
plt.xlabel('Type of primes')
plt.ylabel('Prime Count')
plt.title('Mersenne Primes vs Primes in the Form n^2 + 1')
plt.show()

# Looking at the graphs we notice that, as observed earlier, primes in the 
# form n^2 + 1 have a higher count compared to Mersenne primes. This suggests
# that Mersenne primes occur much less frequently than primes in the form 
# n^2 + 1. 

# Furthermore, by observing the graph for n = 500, the Mersenne prime graph
# stops at 127 and there are no further Mersenne primes between 127 and 500. 
# This further highlights the lack of Mersenne primes. In fact, the next 
# Mersenne prime after 127 is 8191! We also observe that the n^2+1 prime graph
# stops at 401. Therefore, we observe that both primes become further spread
# apart as n increases which can be seen by the longer lines on both graphs.

# Finally, we can observe which prime numbers are included in each of the 
# types of primes. We notice that no points correspond to each other on the 
# graphs. We can also confirm this by inputting 'mersenneprimes(500)' and 
# 'squareprimes(500)', these give lists with different primes and so, we can 
# conclude that for our set value of n (500) there is no crossover between these
# two types of primes. In other words, the same prime does not occur in both 
# lists - each list is completely distinct. 

# Overall, we have observed a lot of similarities between Mersenne primes and 
# primes in the form n^2 + 1. In particular, their count is much lower, 
# implying that these types of primes don't occur as often as other primes
# like normal primes, sexy primes and twin primes. Furthermore, we have also
# observed that between each particular prime, the distance becomes larger,
# that is, say, for each p in their own prime sequence, with p+1 the type of prime
# after p and p-1 the type of prime before p, we have:
# |(p+1) - p| > |p - (p-1)|
# We have also noticed that the two types of primes don't share any common
# primes for our set value of n at n = 500. So despite sharing much similarity, 
# the primes in their sequences are completely dissimilar. 



# We now extend our investigation by looking at prime numbers within Fibonacci
# Numbers. In particular, the sequences defined by:
    # Sn = GCD(n, Fibonacci(n+1))
    # Tn = GCD(n, Fibonacci(n-1))
# A very interesting result arises from these two sequences which we will discuss
# after we define some functions. 
    
# Fibonacci numbers are so widely studied and used in many areas of mathematics
# and in life in general. We take the opportunity to study them further in this 
# section of the mini-project. 
    
# First, we define a function that produces the nth fibonacci number for an 
# input, n, of our choice. We do this as follows:

# Fibonacci Function
def fibonacci(n): 
    if n<0: 
        print("Incorrect input")
    elif n==0:
        return 0 
    elif n==1: 
        return 1
    elif n==2: 
        return 1
    else: 
        return fibonacci(n-1)+fibonacci(n-2) 
    
# Now we have defined our fibonacci function, we can begin to establish what
# functions we need when exploring our sequences defined above. Clearly, we 
# need to define a Greatest Common Divisor Function. However, for n = 1 in 
# the sequence Tn, we will have GCD(1,fibonacci(0)) and we know that the 
# zeroth element of the fibonacci sequence is 0. Therefore, we must define 
# the gcd for b = 0. We define the whole function as follows:

# Greatest Common Divisor Function    
def gcd(a,b):
    if b == 0 and a == 1:
        return 1
    while b > 0:
       a, b = b, a % b
       gcd = a
    return gcd

# Now we have our two fundamental functions, we can set up functions that 
# produce lists for Sn and Tn. We can do this as follows:
   

# Sn = GCD(n,Fib(n+1))
def gcd_seq(n):
    mylist = []
    for i in range(1,n+1): 
        k = gcd(i,fibonacci(i+1))
        mylist.append(k)
    return mylist

# This produces a list of integers where the nth element corresponds to 
# GCD(n,Fib(n+1))

# Tn = GCD(n,Fib(n-1))
def gcd_seq1(n):
    mylist = []
    for i in range(1,n+1):
        k = gcd(i,fibonacci(i-1))
        mylist.append(k)
    return mylist

# This produces a list of integers where the nth element corresponds to 
# GCD(n,Fib(n-1))

# We have everything we need to explore both the sequences, Sn and Tn. Since
# we are dealing with large numbers, we will consider smaller n since the 
# running time for Python will be much longer. So we command Python to print each 
# sequence for n up to and including 50. 
    
# Doing so, we get:

# For Sn:
# The first 10 terms - [1, 2, 3, 1, 1, 1, 7, 2, 1, 1]
# Terms between 11 and 20 - [1, 1, 13, 2, 3, 1, 17, 1, 1, 2]
# Terms between 21 and 30 - [1, 1, 23, 1, 1, 2, 3, 1, 1, 1]
# Terms between 31 and 40 - [1, 2, 1, 1, 1, 1, 37, 2, 3, 1 ]
# Terms between 41 and 50 - [1, 1, 43, 2, 1, 1, 47, 1, 1, 2,]

# For Tn:
# The first 10 terms - [1, 1, 1, 2, 1, 1, 1, 1, 3, 2]
# Terms between 11 and 20 - [11, 1, 1, 1, 1, 2, 1, 1, 19, 1]
# Terms between 21 and 30 - [1, 3, 2, 1, 1, 1, 1, 1, 2, 29, 1]
# Terms between 31 and 40 - [31, 1, 3, 2, 1, 1, 1, 1, 1, 2]
# Terms between 41 and 50 - [41, 1, 1, 1, 3, 2, 1, 1, 7, 1]
    
# Immediately, we notice that the prime numbers appear frequently in these
# sequences. For the first 10 terms in Sn, we notice that the primes [2,3,7] 
# appear. Similarly, in the first 10 terms in Tn, we notice that no primes 
# appear. However, together, the lists contain all primes up to 10 except 5. 
# Furthermore, we observe that the primes occur at the nth entry. For
# example, [2,3,7] appear at the second, third and seventh entry in the Sn 
# sequence. 
    
# Is this a phenomenon that occurs further along the sequence? In the terms
# between 11 and 20, Sn includes the primes [13,17] at the 13th and 17th entry
# respectively and Tn includes [11,19] at the 11th and 19th entry respectively. 
# Therefore, the sequences between 11 and 20 include all the primes between 11
# and 20. Not only this, but they are the only numbers in the sequence that 
# correspond to their entry, i.e n appears at the nth element, 19 appears at the
# 19 element in the list. 

# This is an extremely wonderful relationship between
# these sequences and the primes. To explore further, we will create functions
# that produce the elements in the sequences that correspond to their entry. 
# For example, for an input 10, the functions would return [1,2,3,7] for Sn and [1]
# for Tn. Since we are considering the primes we will omit the 1 from the list so we 
# can observe whether all numbers in this form are prime. We do this as follows:


# Function for Sn:
def entry_seq(n):
    mylist = []
    a = list(range(1,n+1))
    b = gcd_seq(n)    
    for i in range(0,n):
        if a[i] == b[i]:
         mylist.append(i+1)
    mylist.remove(1)
    return mylist

# Function for Tn:
def entry_seq1(n):
    mylist = []
    a = list(range(1,n+1))
    c = gcd_seq1(n)    
    for i in range(0,n):
        if a[i] == c[i]:
         mylist.append(i+1)
    mylist.remove(1)
    return mylist

# We now input values of n into our functions and observe their outputs. We
# will consider n = 50. This took some running time so we will type the 
# command in comments so that it does not distrupt the running of my entire code.

# entry_seq(50) = [2,3,7,13,17,23,37,43,47]
# entry_seq1(50) = [11,19,29,31,41]
    
# Immediately, we notice that all the numbers produced are indeed primes. To 
# further our studies, we will combine the two lists and observe. 

# a = entry_seq(50) = [2,3,7,13,17,23,37,43,47]
# b = entry_seq1(50) = [11,19,29,31,41]
# a.extend(b)
# a.sort()
# a 
# [2, 3, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    
# We compare this with our primelist function for n = 50.
    
# primelist(50) 
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    
# We notice that the two lists are identical apart from list 1 omitting the 
# value 5. We can therefore say that for n > 5, all primes are accounted for. 

# This is a beautiful pattern of primes found in our Fibonacci sequences and 
# implies that (from 6 up to 100) if p is prime then p divides fibonacci(p+1) or
# p divides fibonacci(p-1) but not both. Further, it implies that, with exception 
# of p=5, p cannot divide fibonacci(p). 
    
# This is a remarkable discovery especially since both prime numbers and 
# fibonacci numbers are widely used and explored. We have been able to use 
# Python to reiterate a relationship between these two types of numbers. If 
# we desired to extend our study into this relationship, we could consider for
# larger n and observe whether a similar pattern approaches but this would 
# require Python to deal with excessively large numbers and result in long
# running times. However, it would be a relationship that sparks great discussion
# and would definitely be worth exploring further. 
    
# Overall, in Part 3 we have explored the similarities and differences between
# Mersenne primes and primes in the form n^2 + 1 through functions, varied 
# n values and graphs. Furthermore, we have established a relationship between
# types of Fibonacci sequences and prime numbers by creating functions, observing
# outputs and comparing lists. 












