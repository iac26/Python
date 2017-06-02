import math

def invert(e, mod):
    a = mod
    b = e % mod
    t = 0
    tn = 1
    while b != 0:
        q = a / b
        tn, t = t-(q*tn), tn
        b, a = a % b, b
    d = t
    if d < 0:
        d += mod
    return d

def exp_mod(num, e, mod):
    R = []
    rp = num
    p = e
    r = 0
    while p >= 1:
        r = (rp ** 2) % mod
        if p % 2 == 1:
            R.append(rp)
            
        p, rp = p / 2, r
    s = 1
    for r in R:
        s *= r
    return s % mod

def guess(n):
    for i in range(2,int(math.sqrt(n))):
        if n % i == 0:
            p = n/i
            q = i
            return [p,q]
                   
                   
            
