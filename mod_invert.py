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
