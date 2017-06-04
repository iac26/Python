#problem 1 project Euler

results = []
for n in range(1000):
    if n % 3 == 0 or n % 5 == 0:
        results.append(n)

print results
