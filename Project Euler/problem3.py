#problem 3 project Euler
import math
import time
t = time.time()
result = 0
num = 600851475143
red_num = int(math.sqrt(num))

def isprime(number):
    red_number = int(math.sqrt(number))
    if red_number % 2 == 0:
        red_number += 1
    if number % 2 == 0:
        return False
    while red_number > 1:
        if number % red_number == 0:
            return False
        red_number -= 2
    return True

if red_num % 2 == 0:
    red_num += 1

while True:
    if num % red_num == 0 and isprime(red_num):
        result = red_num
        break
    red_num -= 2
        
t2 = time.time() - t
print result
print 'solved in',t2,'sec'
