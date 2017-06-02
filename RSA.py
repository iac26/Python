#RSA encryption by Iacopo Sprenger
import math

private_keys = [] 
public_keys = [] 
stdcode = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

class private_key():
    def __init__(self, name, p, q, e, d):
        self.name = name
        self.p = p
        self.q = q
        self.n = p*q
        self.phin = (p-1)*(q-1)
        self.e = e
        self.d = d
class public_key():
    def __init__(self, name, e, n):
        self.name = name
        self.e = e
        self.n = n


def menu():
    while True:
        print '---MENU---'
        print '1) Manage keys'
        print '2) Encrypt message'
        print '3) Decrypt message'
        print '4) About'
        print '5) Quit'
        choice = raw_input(':')
        if choice == '1':
            key_manager()
        elif choice == '2':
            encrypter()
        elif choice == '3':
            decrypter()
        elif choice == '4':
            about()
        elif choice == '5':
            save()
            break
        else:
            print 'input error'
    return

def key_manager():
    while True:
        print '---KEY MANAGER---'
        print '1) Create key'
        print '2) Add key'
        print '3) Remove key'
        print '---private---'
        n = 4
        for key in private_keys:
            print str(n)+')', key.name
            n += 1
        print '---public---'
        for key in public_keys:
            print str(n)+')', key.name
            n += 1
        print str(n)+')', 'exit'
        choice = raw_input(':')
        if choice == '1':
            create_key()
        elif choice == '2':
            add_key()
        elif choice == '3':
            remove_key()
        elif choice == str(n):
            break
        else:
            n = int(choice)-4
            if n < len(private_keys):
                key = private_keys[n]
                print 'private key:', key.name
                print 'e          :', key.e
                print 'd          :', key.d
                print 'n          :', key.n
                print 'phi(n)     :', key.phin
                print 'p          :', key.p
                print 'q          :', key.q
            else:
                key = public_keys[n-len(private_keys)]
                print 'private key:', key.name
                print 'e          :', key.e
                print 'n          :', key.n
            waste = raw_input('ENTER')
    return

            
def create_key():
    print '---CREATE KEY---'
    name = raw_input('name:')
    print 'p and q are two different prime numbers'
    p,q = 0,0
    while True:
        try:
            p = int(raw_input('p:'))
            q = int(raw_input('q:'))
        except:
            continue
        c = 0
        if p < 2 or q < 2:
            continue
        if p != q:
            for i in range(2,int(math.sqrt(p))+1):
                if p % i == 0:
                    print 'p =',p,'is not prime'
                    break
            else:
                print 'p =',p,'OK'
                c += 1
            for i in range(2,int(math.sqrt(q))+1):
                if q % i == 0:
                    print 'q =',q,'is not prime'
                    break
            else:
                print 'q =',q,'OK'
                c += 1
            if c == 2:
                break
            
        else:
            print 'p equals q'
    n = p*q
    print 'n =',n,'OK'
    phin = (p-1)*(q-1)
    print 'phi(n) =',phin,'OK'
    for i in range(2,phin):
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            a = phin
            b = i
            while b != 0:
                b , a = a % b, b
            if a == 1:
                e = i
                break
    print 'e =',e,'OK'
    a = phin
    b = e
    t = 0
    tn = 1
    while b != 0:
        r = a / b
        tn, t = t-(r*tn), tn
        b, a = a % b, b
    d = t
    if d < 0:
        d += phin
        n
    print 'd =',d,'OK'
    key = private_key(name, p, q, e, d)
    private_keys.append(key)
    key = public_key(name, e, n)
    public_keys.append(key)
    return
    
def add_key():
    print '---ADD KEY---'
    name = raw_input('name:')
    e = int(raw_input('e:'))
    n = int(raw_input('n:'))
    key = public_key(name,e,n)
    public_keys.append(key)
    return

def remove_key():
    print '---REMOVE KEY---'
    choice = raw_input('key name:')
    for i,key in enumerate(public_keys):
        if key.name == choice:
            public_keys.pop(i)
            print 'key deleted'
            break
    else:
        for i,key in enumerate(private_keys):
            if key.name == choice:
                private_keys.pop(i)
                print 'key deleted'
                break
        else:
            print 'no key named',choice

def base10(message, bloc_len):
    blocs = []
    numericblocs = []
    message = message.upper()
    message = message.replace(' ', '')
    for letter in message:
        if letter not in stdcode:
            return False
    while True:
        if len(message) % bloc_len == 0:
            break
        else:
            message += 'A'
    for i in range(0,len(message),bloc_len):
        bloc = message[i:i+bloc_len]
        blocs.append(bloc)
    for bloc in blocs:
        numericbloc = 0
        for i,letter in enumerate(reversed(bloc)):
            num = stdcode.index(letter)
            numericbloc += num*(26**i)
        numericblocs.append(numericbloc)
    return numericblocs

def base26(blocs, bloc_len):
    message = ''
    for bloc in blocs:
        lbloc = ''
        for i in range(bloc_len):
            bloc, num = bloc / 26, bloc % 26
            letter = stdcode[num]
            lbloc += letter
        message += lbloc[::-1]
    return message

def RSA(blocs, e, n):
    cblocs = []
    for bloc in blocs:
        cbloc = int((bloc**e) % n)
        cblocs.append(cbloc)
    return cblocs
    

def encrypter():
    print '---ENCRYPTER---'
    while True:
        use_signature = raw_input('use signarure(yes/no)?:')
        if use_signature.startswith('y'):
            signature = True
            break
        elif use_signature.startswith('n'):
            signature = False
            break
    pukey = None
    while not pukey:
        key_choice = raw_input('public key name:')
        for i,key in enumerate(public_keys):
            if key.name == key_choice:
                pukey = key
                break
        else:
            print 'key not found'
    if signature:
        prkey = None
        while not prkey:
            key_choice = raw_input('private key name:')
            for i,key in enumerate(private_keys):
                if key.name == key_choice:
                    prkey = key
                    break
            else:
                print 'key not found'
    message = raw_input('message:')
    bloc_len = int(math.log(pukey.n)/math.log(26))
    blocs = base10(message, bloc_len)
    cblocs = RSA(blocs, pukey.e, pukey.n)
    cmessage = base26(cblocs, bloc_len+1)
    if signature:
        bloc_len = int(math.log(prkey.n)/math.log(26))
        blocs = base10(message, bloc_len)
        cblocs = RSA(blocs, prkey.d, prkey.n)
        csignature= base26(cblocs, bloc_len+1)
        bloc_len = int(math.log(pukey.n)/math.log(26))
        blocs = base10(csignature, bloc_len)
        cblocs = RSA(blocs, pukey.e, pukey.n)
        csigned = base26(cblocs, bloc_len+1)
        print 'encrypted and signed:', '('+cmessage+','+csigned+')'
    else:       
        print 'encrypted:', cmessage
    waste = raw_input('ENTER')



def decrypter():
    print '---DECRYPTER---'
    while True:
        use_signature = raw_input('use signarure(yes/no)?:')
        if use_signature.startswith('y'):
            signature = True
            break
        elif use_signature.startswith('n'):
            signature = False
            break
    prkey = None
    while not prkey:
        key_choice = raw_input('private key name:')
        for i,key in enumerate(private_keys):
            if key.name == key_choice:
                prkey = key
                break
        else:
            print 'key not found'
    if signature:
        pukey = None
        while not pukey:
            key_choice = raw_input('public key name:')
            for i,key in enumerate(public_keys):
                if key.name == key_choice:
                    pukey = key
                    break
            else:
                print 'key not found'
    cmessage = raw_input('message:')
    if signature: 
        signed = raw_input('signature:')

    bloc_len = int(math.log(prkey.n)/math.log(26))
    blocs = base10(cmessage, bloc_len+1)
    cblocs = RSA(blocs, prkey.d, prkey.n)
    message = base26(cblocs, bloc_len)
    print 'message:', message
    if signature:
        bloc_len = int(math.log(prkey.n)/math.log(26))
        blocs = base10(signed, bloc_len+1)
        cblocs = RSA(blocs, prkey.d, prkey.n)
        msigned = base26(cblocs, bloc_len)
        bloc_len = int(math.log(pukey.n)/math.log(26))
        blocs = base10(msigned, bloc_len+1)
        cblocs = RSA(blocs, pukey.e, pukey.n)
        msignature= base26(cblocs, bloc_len)
        if message.startswith(msignature) or msignature.startswith(message):
            print 'signature RELIABLE'
        else:
            print 'signature UNRELIABLE'
        

        
    waste = raw_input('ENTER')

def save():
    text = ''
    for key in private_keys:
        line = ''
        line += 'private:'
        line += key.name + ':'
        line += str(key.p) + ':'
        line += str(key.q) + ':'
        line += str(key.e) + ':'
        line += str(key.d)
        text += line + '\n'
    for key in public_keys:
        line = ''
        line += 'public:'
        line += key.name + ':'
        line += str(key.e) + ':'
        line += str(key.n)
        text += line + '\n'
    f = open('keys','w')
    f.write(text)
    f.close
    return
    
    


try:
    f = open('keys','r')
    text = f.read()
    lines = text.split('\n')
    for line in lines:
        arg = line.split(':')
        if arg[0] == 'private':
            key = private_key(arg[1],int(arg[2]),int(arg[3]),int(arg[4]),int(arg[5]))
            private_keys.append(key)
        if arg[0] == 'public':
            key = public_key(arg[1],int(arg[2]),int(arg[3]))
            public_keys.append(key)
    f.close
except:
    f = open('keys','w')
    f.close()

        
menu()
