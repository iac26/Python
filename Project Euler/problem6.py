#problem 6 project Euler
import time
numbers = []
squares = []
t = time.time()
for i in range(1,101):
    numbers.append(i)
    squares.append(i**2)

diff = (sum(numbers)**2)-sum(squares)
t2 = time.time()-t
print diff
print 'solved in',t2,'sec'
