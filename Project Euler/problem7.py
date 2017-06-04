#problem 7 project Euler
import time
import math

primes = [2]
a = 3
n = 0
t = time.time()
while not n == 10001:
    for i in primes:
        if (a % i) == 0:
            break
    else:
        primes.append(a)
        n += 1
    a += 1
t2 = time.time()-t
print primes[10000]
print 'solved in',t2,'sec'

