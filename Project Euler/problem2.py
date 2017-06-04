#problem2 project Euler

a = 1
b = 2
total = 0
while a <= 4000000:
    if a % 2 == 0:
        total += a
    a , b = b, a+b
print total
