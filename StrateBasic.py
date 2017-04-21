# -*- coding: cp1252 -*-
import random

norm = True

def cls():
    print "\n"*100

#retourne un booleen selon des probabilit�s 
def fight(p):
    r = random.randint(1,100)
    if p > r:
        return True
    else:
        return False
    

#permet de calculer le r�sultat d'un duel en se basant sur les probabilit�s donn�es
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

#compte le nombre de soldats d'un certain type dans une arm�e  
def count(armee, t): 
    c = 0
    for s in armee:
        if s == t:
            c += 1
    return c

#retourne le nom complet d'un type de soldat
def tpe(t):
    if t == 'F':
        return 'Fantassin'
    if t == 'C':
        return 'Cavalier'
    if t == 'A':
        return 'Artilleur'


resp = raw_input('Enter pour commencer...')
cls()
if resp == 'special':
    norm = False
while True:
    if norm: #configuration normale des arm�es
        armeeRouge = ['F','F','F','F','F','F','F','F','F','F','F','C','C','C','C','C','A','A'] #contient les soldats vivants (Rouges) (dure toute la battaille)
        armeeBleue = ['F','F','F','F','F','F','F','F','F','F','F','C','C','C','C','C','A','A'] #contient les soldats vivants (Bleus) (dure toute la battaille)
    else: #configuration speciale (choix de l'utilisateur) des arm�es
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
    #initialisation des tableaux
    blessesRouges = [] #contient les index des soldats tu�s (Rouges) (dure un affrontement)
    blessesBleus = [] #contient les index des soldats tu�s (Bleus) (dure un affrontement)
    cadavresRouges = [] #contient les soldats morts (Rouges) (dure toute la battaille)
    cadavresBleus = [] #contient les soldats morts (Bleus) (dure toute la battaille)
    meleeRouge = [] #contient les index des soldats vivants (Rouges) (dure un affrontement)
    meleeBleue = []  #contient les index des soldats vivants (Bleus) (dure un affrontement)
    champ = 0 # taille de l'arm�e la plus petite
    aff = 1 # numero de l'affrontement

    cls()
    print '------ Nouvelle Battaille ------'
    while True:
        #arrangements des duels 
        meleeRouge = random.sample(range(len(armeeRouge)), len(armeeRouge))
        meleeBleue = random.sample(range(len(armeeBleue)), len(armeeBleue))
        blessesBleus = []
        blessesRouges = []
        glandeurs = [] #contient les soldtas qui n'ont pas d'adversaire
        #calcul de la taille de l'arm�e la plus petite et du non('ga') de l'arm�e la plus grande
        if len(meleeRouge) <= len(meleeBleue):
            champ = len(meleeRouge)
            ga = 'Bleue'
        else:
            champ = len(meleeBleue)
            ga = 'Rouge'
        #affichage des effectifs
        print '\n------ Affrontement', aff, '------'
        print "\nl'arm�e rouge est constitu�e de", len(armeeRouge), 'soldat:' if len(armeeRouge) == 1 else 'soldats:'
        print count(armeeRouge, 'F'), 'Fantassin' if count(armeeRouge, 'F') == 1 else 'Fantassins' , '(', count(cadavresRouges, 'F'), 'mort )' if count(cadavresRouges, 'F') == 1 else 'morts )'
        print count(armeeRouge, 'C'), 'Cavalier' if count(armeeRouge, 'C') == 1 else 'Cavaliers' , '(', count(cadavresRouges, 'C'), 'mort )' if count(cadavresRouges, 'C') == 1 else 'morts )'
        print count(armeeRouge, 'A'), 'Artilleur' if count(armeeRouge, 'A') == 1 else 'Artilleurs' , '(', count(cadavresRouges, 'A'), 'mort )' if count(cadavresRouges, 'A') == 1 else 'morts )'
        print "\nl'arm�e bleue est constitu�e de", len(armeeBleue), 'soldat:' if len(armeeBleue) == 1 else 'soldats:'
        print count(armeeBleue, 'F'), 'Fantassin' if count(armeeBleue, 'F') == 1 else 'Fantassins' , '(', count(cadavresBleus, 'F'), 'mort )' if count(cadavresBleus, 'F') == 1 else 'morts )'
        print count(armeeBleue, 'C'), 'Cavalier' if count(armeeBleue, 'C') == 1 else 'Cavaliers' , '(', count(cadavresBleus, 'C'), 'mort )' if count(cadavresBleus, 'C') == 1 else 'morts )'
        print count(armeeBleue, 'A'), 'Artilleur' if count(armeeBleue, 'A') == 1 else 'Artilleurs' , '(', count(cadavresBleus, 'A'), 'mort )' if count(cadavresBleus, 'A') == 1 else 'morts )'
        waste = raw_input("\ncommencer l'affrontement (Enter) ?") 
        ct = 0
        #calcul des duels et des gagnants + affichage
        for d in range(champ):
            ct += 1
            print '\nun', tpe(armeeRouge[meleeRouge[d]]), 'rouge se bat contre un', tpe(armeeBleue[meleeBleue[d]]), 'bleu:',
            if duel(armeeRouge[meleeRouge[d]], armeeBleue[meleeBleue[d]]):
                cadavresBleus.append(armeeBleue[meleeBleue[d]])
                blessesBleus.append(meleeBleue[d])
                print 'l\'' if armeeRouge[meleeRouge[d]] == 'A' else 'le', tpe(armeeRouge[meleeRouge[d]]), 'rouge gangne!'
            else:
                cadavresRouges.append(armeeRouge[meleeRouge[d]])
                blessesRouges.append(meleeRouge[d])
                print 'l\'' if armeeBleue[meleeBleue[d]] == 'A' else 'le', tpe(armeeBleue[meleeBleue[d]]), 'bleu gangne!'
        #calcul des soldats sans adversaire + affichage
        if ga == 'Rouge':        
            for g in range(ct, len(meleeRouge)):
                print '\nun', tpe(armeeRouge[meleeRouge[g]]), 'rouge ne se bat pas'
                glandeurs.append(armeeRouge[meleeRouge[g]])
        elif ga == 'Bleue':
            for g in range(ct, len(meleeBleue)):
                print '\nun', tpe(armeeBleue[meleeBleue[g]]), 'bleu ne se bat pas'
                glandeurs.append(armeeBleue[meleeBleue[g]])
        #r�partition des soldats dans le champ de battaille 
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
        #affichage du champ de battaille 
        ct1 = 0
        ct2 = 0
        ct3 = 0
        st = ' '
        st += '\n'
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
        st += ' '
        print st
        #suppression des morts des tableaux armee...
        blessesBleus.sort(reverse=True)
        blessesRouges.sort(reverse=True)
        for b in blessesBleus:
            armeeBleue.pop(b)
        for r in blessesRouges:
            armeeRouge.pop(r)
        #conditions de victoire + affichage des effectifs de l'arm�e vaincqueure 
        if len(armeeRouge) == 0:
            print "\n\n\nl'arm�e bleue gagne!"
            print "\nelle est encore constitu�e de", len(armeeBleue), 'soldat:' if len(armeeBleue) == 1 else 'soldats:'
            print count(armeeBleue, 'F'), 'Fantassin' if count(armeeBleue, 'F') == 1 else 'Fantassins' , '(', count(cadavresBleus, 'F'), 'mort )' if count(cadavresBleus, 'F') == 1 else 'morts )'
            print count(armeeBleue, 'C'), 'Cavalier' if count(armeeBleue, 'C') == 1 else 'Cavaliers' , '(', count(cadavresBleus, 'C'), 'mort )' if count(cadavresBleus, 'C') == 1 else 'morts )'
            print count(armeeBleue, 'A'), 'Artilleur' if count(armeeBleue, 'A') == 1 else 'Artilleurs' , '(', count(cadavresBleus, 'A'), 'mort )' if count(cadavresBleus, 'A') == 1 else 'morts )'
            break
        if len(armeeBleue) == 0:
            print "\nl'arm�e rouge gagne!"
            print "\nelle est encore constitu�e de", len(armeeRouge), 'soldat:' if len(armeeRouge) == 1 else 'soldats:'
            print count(armeeRouge, 'F'), 'Fantassin' if count(armeeRouge, 'F') == 1 else 'Fantassins' , '(', count(cadavresRouges, 'F'), 'mort )' if count(cadavresRouges, 'F') == 1 else 'morts )'
            print count(armeeRouge, 'C'), 'Cavalier' if count(armeeRouge, 'C') == 1 else 'Cavaliers' , '(', count(cadavresRouges, 'C'), 'mort )' if count(cadavresRouges, 'C') == 1 else 'morts )'
            print count(armeeRouge, 'A'), 'Artilleur' if count(armeeRouge, 'A') == 1 else 'Artilleurs' , '(', count(cadavresRouges, 'A'), 'mort )' if count(cadavresRouges, 'A') == 1 else 'morts )'
            break
        aff += 1
        waste = raw_input("\nvoir le prochain affrontement (Enter) ?")
        cls()
    resp = raw_input("\nrejouer? ")
    if resp == 'non':
        break
    if resp == 'normal':
        norm = True
    if resp == 'special':
        norm == False

