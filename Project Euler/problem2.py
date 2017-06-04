#problem2 project Euler
import time
t = time.time()
a = 1
b = 2
total = 0
while a <= 4000000:
    if a % 2 == 0:
        total += a
    a , b = b, a+b
t2 = time.time()-t
print total
print 'solved in',t2,'sec'
