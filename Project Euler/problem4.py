#problem 4 project Euler



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
    for i in range(a):
        for j in range(i):
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
    a = biggest
    b = biggest
    g = biggest
    last = [(99,99)]
    r = (biggest+1)**2
    rp = r
    while b > 0:
        if a*b < (a-1)*g:
            if not a == b:
                last.append((a,b))
            a -= 1
            b = g
        try:
            t = last[0]
        except:
            t = (0,0)
        if mul(t) > a*b:
            if mul(t) < rp:
                a = t[0]
                b = t[1]
                print 'insert'
            last.pop(0)
        rp = r
        r = a*b
        print a,b,r,rp
        b -= 1
    
        
result = multiply(999)
print result
        
    


