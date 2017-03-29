
#Bibliotheque
#par iacopo sprenger le 13 mars 2017

import os

lecteurs = []
livres = []
index = []

def clear():
    #os.system('cls')  #windows
    #os.system('clear')  #mac
    print "\n" * 100 #pour idle

def listerLivres(numeros = True):
    if numeros:
        for i, li in enumerate(livres):
            print i, ':', li, 'emprunte par', index[i]
    else:
        for i, le in enumerate(livres):
            print le, 'emprunte par', index[i]
            
def listerLecteurs():
    for i, le in enumerate(lecteurs):
        print i, ':', le
        
def listerLivresEmpruntes(lect = 0, lpres = True):
    if lpres:
        for i, li in enumerate(livres):
            if li != 'personne': print li, 'emprunte par', index[i]
    else:
        c = 0
        for li in livres:
            if li == lecteurs[lect]:
                print li
                c = 1
        if c == 0:
            print 'Aucun livre emprunte'
        
try:
    f = open('BiblioMem', 'r')
    print 'success'
    #waste = raw_input()
    line = f.readline()
    while line != '':
        line = f.readline()
        print(line[:-1])
        if line == ':\n':
            break
        lecteurs.append(line[:-1])
    while line != '':
        line = f.readline()
        print(line[:-1])
        if line == ':\n':
            break
        livres.append(line[:-1])
    while line != '':
        line = f.readline()
        print(line[:-1])
        if line == ':\n':
            break
        index.append(line[:-1])
    #waste = raw_input()
    f.close()
except:
    f = open('BiblioMem', 'w')
    f.close()
    print 'fail'





while True:

    clear()
    print 'Bibliotheque'
    print ''
    print '1 : emprunter/rendre'
    print '2 : lecteurs'
    print '3 : catalogue'
    print '4 : nouveau livre'
    print '5 : nouveau lecteur'
    print '6 : sauvegarder et quitter'

    try:
        choix = int(raw_input('choix: '))
    except:
        print 'erreur'

    if choix == 1: #emprunter/rendre
        while True:
            clear()
            print 'Choisir un livre: '
            print  ''
            listerLivres()
            try:
                livre = int(raw_input('livre: '))
                if livre in range(len(livres)):
                    break
            except:
                print 'erreur'
        if index[livre] == 'personne':
            while True:
                clear()
                print 'Choisir un Lecteur: '
                print  ''
                listerLecteurs()
                try:
                    lecteur = int(raw_input('lecteur: '))
                    if lecteur in range(len(lecteurs)):
                        break
                except:
                    print 'erreur'
            index[livre] = lecteurs[lecteur]
        else:
            index[livre] = 'personne'
    elif choix == 2: #lecteurs
        while True:
            clear()
            print 'Choisir un lecteur: '
            print  ''
            listerLecteurs()
            try:
                lecteur = int(raw_input('lecteur: '))
                if lecteur in range(len(lecteurs)):
                    break
            except:
                print 'erreur'
        clear()
        listerLivresEmpruntes(lecteur, False)
        waste = raw_input()
    elif choix == 3: #catalogue
        clear()
        print 'Catalogue: '
        print ''
        listerLivres(False)
        waste = raw_input()
    elif choix == 4: #nouveau livre
        clear()
        print 'Nouveau livre: '
        print ''
        livre = raw_input('nom du livre: ')
        livres.append(livre)
        index.append('personne')
        
    elif choix == 5: #nouveau lecteur
        clear()
        print 'Nouveau lecteur: '
        print ''
        lecteur = raw_input('nom du lecteur: ')
        lecteurs.append(lecteur)
    elif choix == 6: #sauvegarder et quitter
        try:
            f = open('BiblioMem', 'w')
            f.write('--BiblioMem--\n')
            for le in lecteurs:
                f.write(le)
                f.write('\n')
            f.write(':')
            f.write('\n')
            for li in livres:
                f.write(li)
                f.write('\n')
            f.write(':')
            f.write('\n')
            for i in index:
                f.write(i)
                f.write('\n')
            f.write(':')
            f.write('\n')
            f.close()
        except:
            print "save error"
        break
    else:
        print 'erreur'
    
