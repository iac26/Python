#problem5 project Euler
import math
import time
t = time.time()
multiples = range(1,21)
def prime_numbers(n):
    primes = []
    for i in range(2,n+1):
        for j in range(2,int(math.sqrt(i))+1):
            if i % j == 0:
                break
        else:
            primes.append(i)
    return primes



def factorize(n, primes):
    factors = []
    a = n
    b = 0
    if n == 1:
        return [1]
    while not a == 1:
        for p in primes:
            if a % p == 0:
                a = a/p
                factors.append(p)
                break
        else:
            factors.append(a)
            return factors
    return factors

primes = prime_numbers(20)
fact = []

for m in multiples:
    f = factorize(m, primes)
    for i in f:
        a = f.count(i)
        b = fact.count(i)
        if a > b:
            for j in range(a-b):
                fact.append(i)
result = 1
for n in fact:
    result = result*n
t2 = time.time()-t
print result
print 'solved in',t2,'sec'
