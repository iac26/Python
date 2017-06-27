#problem 1 project Euler
import time
t = time.time()
results = []
for n in range(1000):
    if n % 3 == 0 or n % 5 == 0:
        results.append(n)
t2 = time.time()-t
result = sum(results)
print result
print 'solved in',t2,'sec'
