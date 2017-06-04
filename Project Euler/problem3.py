#problem 3 project Euler
import math
result = 0
number = 600851475143
red_num = int(math.sqrt(number))
if red_num % 2 == 0:
    red_num += 1

while True:
    if number % red_num == 0:
        result = red_num
        break
    red_num -= 2

print result
    
