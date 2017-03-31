# -*- coding: cp1252 -*-
import random


armeeRouge = ['F','F','F','F','F','F','F','F','F','F','F','C','C','C','C','C','A','A']
armeeBleue = ['F','F','F','F','F','F','F','F','F','F','F','C','C','C','C','C','A','A']
blessesRouges = []
blessesBleus = []
cadavresRouges = []
cadavresBleus = []
meleeRouge = []
meleeBleue = []
champ = 0
aff = 1
norm = True
def fight(p):
    r = random.randint(1,100)
    if p > r:
        return True
    else:
        return False
    


def duel(a,b):
    if a == 'F':
        if b == 'F':
            return fight(50)
        if b == 'C':
            return fight(30)
        if b == 'A':
            return fight(10)
    if a == 'C':
        if b == 'F':
            return fight(60)
        if b == 'C':
            return fight(50)
        if b == 'A':
            return fight(20)
    if a == 'A':
        if b == 'F':
            return fight(90)
        if b == 'C':
            return fight(80)
        if b == 'A':
            return fight(50)

def count(armee, t):
    c = 0
    for s in armee:
        if s == t:
            c += 1
    return c
def tpe(t):
    if t == 'F':
        return 'Fantassin'
    if t == 'C':
        return 'Cavalier'
    if t == 'A':
        return 'Artilleur'

resp = raw_input('Enter pour commencer...')
if resp == 'special':
    norm = False
while True:
    if norm:
        armeeRouge = ['F','F','F','F','F','F','F','F','F','F','F','C','C','C','C','C','A','A']
        armeeBleue = ['F','F','F','F','F','F','F','F','F','F','F','C','C','C','C','C','A','A']
    else:
        armeeRouge = []
        armeeBleue = []
        print "\ncustomisation de l'arm�e rouge:\n"
        while True:
            f = raw_input('Fantassins: ')
            c = raw_input('Cavaliers: ')
            a = raw_input('Artilleurs: ')
            try:
                for i in range(int(f)):
                    armeeRouge.append('F')
                for i in range(int(c)):
                    armeeRouge.append('C')
                for i in range(int(a)):
                    armeeRouge.append('A')
                break
            except:
                 print 'ERREUR Nombres Entiers Requis !'
        print "\ncustomisation de l'arm�e bleue:\n"
        while True:
            f = raw_input('Fantassins: ')
            c = raw_input('Cavaliers: ')
            a = raw_input('Artilleurs: ')
            try: 
                for i in range(int(f)):
                    armeeBleue.append('F')
                for i in range(int(c)):
                    armeeBleue.append('C')
                for i in range(int(a)):
                    armeeBleue.append('A')
                break
            except:
                print 'ERREUR Nombres Entiers Requis !'
    blessesRouges = []
    blessesBleus = []
    cadavresRouges = []
    cadavresBleus = []
    meleeRouge = []
    meleeBleue = []
    champ = 0
    aff = 1
    print '\n\n\n\n\n\n------ Nouvelle Battaille ------'
    while True:
        meleeRouge = random.sample(range(len(armeeRouge)), len(armeeRouge))
        meleeBleue = random.sample(range(len(armeeBleue)), len(armeeBleue))
        blessesBleus = []
        blessesRouges = []
        if len(meleeRouge) <= len(meleeBleue):
            champ = len(meleeRouge)
            ga = 'Bleue'
        else:
            champ = len(meleeBleue)
            ga = 'Rouge'
        print '\n------ Affrontement', aff, '------'
        print "\nl'arm�e rouge est constitu�e de:"
        print count(armeeRouge, 'F'), 'Fantassins', '(', count(cadavresRouges, 'F'), 'morts )'
        print count(armeeRouge, 'C'), 'Cavaliers', '(', count(cadavresRouges, 'C'), 'morts )'
        print count(armeeRouge, 'A'), 'Artilleurs', '(', count(cadavresRouges, 'A'), 'morts )'
        print "\nl'arm�e bleue est constitu�e de:"
        print count(armeeBleue, 'F'), 'Fantassins', '(', count(cadavresBleus, 'F'), 'morts )'
        print count(armeeBleue, 'C'), 'Cavaliers', '(', count(cadavresBleus, 'C'), 'morts )'
        print count(armeeBleue, 'A'), 'Artilleurs', '(', count(cadavresBleus, 'A'), 'morts )'
        waste = raw_input("\ncommencer l'affrontement (Enter) ?")
        ct = 0
        for d in range(champ):
            ct += 1
            print '\nun', tpe(armeeRouge[meleeRouge[d]]), 'rouge se bat contre un', tpe(armeeBleue[meleeBleue[d]]), 'bleu:',
            if duel(armeeRouge[meleeRouge[d]], armeeBleue[meleeBleue[d]]):
                cadavresBleus.append(armeeBleue[meleeBleue[d]])
                blessesBleus.append(meleeBleue[d])
                print 'le', tpe(armeeRouge[meleeRouge[d]]), 'rouge gangne!'
            else:
                cadavresRouges.append(armeeRouge[meleeRouge[d]])
                blessesRouges.append(meleeRouge[d])
                print 'le', tpe(armeeBleue[meleeBleue[d]]), 'bleu gangne!'
        if ga == 'Rouge':        
            for g in range(ct, len(meleeRouge)):
                print '\nun', tpe(armeeRouge[meleeRouge[g]]), 'rouge ne se bat pas'
        elif ga == 'Bleue':
            for g in range(ct, len(meleeBleue)):
                print '\nun', tpe(armeeBleue[meleeBleue[g]]), 'bleu ne se bat pas'
            
        blessesBleus.sort(reverse=True)
        blessesRouges.sort(reverse=True)
        for b in blessesBleus:
            armeeBleue.pop(b)
        for r in blessesRouges:
            armeeRouge.pop(r)
        if len(armeeRouge) == 0:
            print "\n\n\nl'arm�e bleue gagne!"
            print "\nelle est encore constitu�e de:\n"
            print count(armeeBleue, 'F'), 'Fantassins', '(', count(cadavresBleus, 'F'), 'morts )'
            print count(armeeBleue, 'C'), 'Cavaliers', '(', count(cadavresBleus, 'C'), 'morts )'
            print count(armeeBleue, 'A'), 'Artilleurs', '(', count(cadavresBleus, 'A'), 'morts )'
            break
        if len(armeeBleue) == 0:
            print "\nl'arm�e rouge gagne!"
            print "\nelle est encore constitu�e de:\n"
            print count(armeeRouge, 'F'), 'Fantassins', '(', count(cadavresRouges, 'F'), 'morts )'
            print count(armeeRouge, 'C'), 'Cavaliers', '(', count(cadavresRouges, 'C'), 'morts )'
            print count(armeeRouge, 'A'), 'Artilleurs', '(', count(cadavresRouges, 'A'), 'morts )'
            break
        aff += 1
        waste = raw_input("\nvoir le prochain affrontement (Enter) ?")
        print '\n' * 10
    resp = raw_input("\nrejouer? ")
    if resp == 'non':
        break
    if resp == 'normal':
        norm = True
    if resp == 'special':
        norm == False

