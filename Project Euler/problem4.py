#problem 4 project Euler
import time
t = time.time()

biggest = 999

def is_pal(n):
    s = str(n)
    for c1,c2 in zip(s, reversed(s)):
        if not c1 == c2:
            return False
    else:
        return True

def multiply(biggest):
    a = biggest
    b = biggest
    res = []
    for i in range(100,a):
        for j in range(100,i):
            r = i*j
            if is_pal(r):
                res.append(r)
    return max(res)

def false(biggest):
    a = biggest
    b = biggest
    res = []
    for i in range(a,0,-1):
        for j in range(a,i-1,-1):
            r = i*j
            print i,j,r
            if is_pal(r):
                res.append(r)
    return max(res)

def mul((a,b)):
    return a*b

def optimized(biggest):
    pass
    
        
result = multiply(999)

t2 = time.time()-t
print result
print 'solved in',t2,'sec'
        
    


