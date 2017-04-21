# -*- coding: cp1252 -*-
import random

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
            return fight(70)
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
        print "\ncustomisation de l'armée rouge:\n"
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
        print "\ncustomisation de l'armée bleue:\n"
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
        glandeurs = []
        if len(meleeRouge) <= len(meleeBleue):
            champ = len(meleeRouge)
            ga = 'Bleue'
        else:
            champ = len(meleeBleue)
            ga = 'Rouge'
        print '\n------ Affrontement', aff, '------'
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
                print 'le', tpe(armeeBleue[meleeBleue[d]]), 'bleu gangne!'
        if ga == 'Rouge':        
            for g in range(ct, len(meleeRouge)):
                print '\nun', tpe(armeeRouge[meleeRouge[g]]), 'rouge ne se bat pas'
                glandeurs.append(armeeRouge[meleeRouge[g]])
        elif ga == 'Bleue':
            for g in range(ct, len(meleeBleue)):
                print '\nun', tpe(armeeBleue[meleeBleue[g]]), 'bleu ne se bat pas'
                glandeurs.append(armeeBleue[meleeBleue[g]])

        while True:
            ctg = 0
            grid = [' ' for i in range(36)]
            comb1 = [' ' for i in range(36)]
            comb2 = [' ' for i in range(36)]
            for x in range(champ*2):
                    if grid[x] == ' ':
                        r1 = random.randint(0,1)
                        ok = False
                        a = armeeRouge[meleeRouge[ctg]] 
                        b = armeeBleue[meleeBleue[ctg]] 
                        if r1:
                            if x not in [5,11,17,23,29,35]:
                                if grid[x+1] == ' ':
                                    grid[x+1] = b 
                                    grid[x] = a
                                    comb2[x] = 'x'
                                    ok = True
                                    ctg += 1
                                elif x not in [30,31,32,33,34,35]:
                                    if grid[x+6] == ' ':
                                        grid[x+6] = b 
                                        grid[x] = a 
                                        comb1[x] = 'x'
                                        ok = True
                                        ctg += 1
                            elif x not in [30,31,32,33,34,35]:
                                if grid[x+6] == ' ':
                                    grid[x+6] = b 
                                    grid[x] = a 
                                    comb1[x] = 'x'
                                    ok = True
                                    ctg += 1
                        else:
                            if x not in [30,31,32,33,34,35]:
                                if grid[x+6] == ' ':
                                    grid[x+6] = b 
                                    grid[x] = a 
                                    comb1[x] = 'x'
                                    ok = True
                                    ctg += 1
                                elif x not in [5,11,17,23,29,35]:
                                    if grid[x+1] == ' ':
                                        grid[x+1] = b 
                                        grid[x] = a
                                        comb2[x] = 'x'
                                        ok = True
                                        ctg += 1
                            elif x not in [5,11,17,23,29,35]:
                                if grid[x+1] == ' ':
                                    grid[x+1] = b 
                                    grid[x] = a
                                    comb2[x] = 'x'
                                    ok = True
                                    ctg += 1
                    else:
                        ok = True
                    if not ok:
                        break
                    if not ctg < champ:
                        break
            if ok:
                break
        ct1 = 0
        ct2 = 0
        ct3 = 0
        st = '\n'
        for a in range(6):
            for b in range(6):
                if grid[ct1] == ' ' and ct3 < len(glandeurs):
                    st += glandeurs[ct3] + '   '
                    ct3 += 1
                else:
                    st += grid[ct1]+' '+ comb2[ct1]+' '
                ct1 += 1
            st += '\n'
            for c in range(6):
                st += comb1[ct2] + '   '
                ct2 += 1
            st += '\n'

        print st
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

