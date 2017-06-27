#problem 10 Project Euler
import time
import math
t = time.time()
n = 2000000
primes = []
notprimes = []
p = 2
i = 1

##while p <= n:
##    i = 1
##    if p not in notprimes:
##        primes.append(p)
##        while True:
##            np = p*i
##            if np > n:
##                break
##            if np not in notprimes:
##                notprimes.append(np)
##            i += 1
##    p += 1
##        
##    
##s = sum(primes)


    

for i in range(2,n+1):
    for j in range(2,int(math.sqrt(i))+1):
        if i % j == 0:
            break
    else:
        primes.append(i)
s = sum(primes)



t2 = time.time()-t
print s
print "solved in",t2,"seconds"
