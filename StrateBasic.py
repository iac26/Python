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

print "l'armée rouge se bat contre l'armée bleue \n"

while True:
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
        print "\nl'armée rouge est constituée de:"
        print count(armeeRouge, 'F'), 'Fantassins', '(', count(cadavresRouges, 'F'), 'morts )'
        print count(armeeRouge, 'C'), 'Cavaliers', '(', count(cadavresRouges, 'C'), 'morts )'
        print count(armeeRouge, 'A'), 'Artilleurs', '(', count(cadavresRouges, 'A'), 'morts )'
        print "\nl'armée bleue est constituée de:"
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
                print 'le', tpe(armeeBleue[meleeRouge[d]]), 'bleu gangne!'
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
            print "\n\n\nl'armée bleue gagne!"
            print "\nelle est encore constituée de:\n"
            print count(armeeBleue, 'F'), 'Fantassins', '(', count(cadavresBleus, 'F'), 'morts )'
            print count(armeeBleue, 'C'), 'Cavaliers', '(', count(cadavresBleus, 'C'), 'morts )'
            print count(armeeBleue, 'A'), 'Artilleurs', '(', count(cadavresBleus, 'A'), 'morts )'
            break
        if len(armeeBleue) == 0:
            print "\nl'armée rouge gagne!"
            print "\nelle est encore constituée de:\n"
            print count(armeeRouge, 'F'), 'Fantassins', '(', count(cadavresRouges, 'F'), 'morts )'
            print count(armeeRouge, 'C'), 'Cavaliers', '(', count(cadavresRouges, 'C'), 'morts )'
            print count(armeeRouge, 'A'), 'Artilleurs', '(', count(cadavresRouges, 'A'), 'morts )'
            break
        
        waste = raw_input("\nvoir le prochain affrontement (Enter) ?")
    resp = raw_input("rejouer? ")
    if resp == 'non':
        break

