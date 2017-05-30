
alphabet =  ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def cipher(clear, key):
    m = clear.upper()
    m = m.replace(' ','')
    k = key.upper()
    if len(k) <= len(m):
        k += k*(len(m)/len(k))
        k += k
        k = k[:len(m)]
    c = ''
    for i,l in enumerate(m):
        n = alphabet.index(l)
        dec = alphabet.index(k[i])
        c += alphabet[(n+dec) % 26]
    return c

def decipher(crypt, key):
    c = crypt.upper()
    c = c.replace(' ','')
    k = key.upper()
    if len(k) <= len(c):
        k += k*(len(c)/len(k))
        k += k
        k = k[:len(c)]
    m = ''
    for i,l in enumerate(c):
        n = alphabet.index(l)
        dec = alphabet.index(k[i])
        m += alphabet[(n-dec) % 26]
    return m

while True:   
    choice = raw_input('cipher or decipher ?')
    if choice.startswith('c'):
        message = raw_input('message:')
        key = raw_input('key:')
        crypt = cipher(message, key)
        print 'cryptogram:', crypt
    if choice.startswith('d'):
        crypt = raw_input('crypt:')
        key = raw_input('key:')
        message = decipher(crypt, key)
        print 'message:', message
    if choice == 'quit':
        break




        
