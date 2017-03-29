import random

couleurs = ['R', 'V', 'B', 'J', 'N', 'O']
combinaison = []
histoire = []
count = 0
victoire = False
solution = ''

def clear():
    print '\n'*100 # on affiche 100 lignes vides pour netoyer l'ecran 

for i in range(4): # choix de la combinaison
    combinaison.append(random.choice(couleurs))

print 'entrez une combinaison (4 lettres appendues)'
print 'les couleurs possibles sont: R V B J N O'
print ''

while count < 10: # max 10 coups
    MP = 0
    BP = 0
    #print combinaison #affiche la solution pour debugger
    print '       XXXX'
    print '       ----'
    for i, h in enumerate(histoire): # affichage de l'historique des coups
        print i+1, h
    while True: # entree du prochain coup 
        essay = raw_input('essay: ')
        if len(essay)==4: # l'essay doit etre de la bonne longeur
            for e in essay: 
                if e not in couleurs: # l'essay ne peut contenir que des couleurs parmis RVBJNO
                    break
            else:
                break
    print essay

    for i,c in enumerate(combinaison): 
        if c == essay[i]: # on compte le nombre de lettres au bon endroit
            BP = BP + 1
        if c in essay: # on compte le nb de lettre presentes dans combinaison
            MP = MP + 1
    MP = MP-BP # on enleve les lettres qui sont au bon endroit comme ca on a que celles qui sont au mauvais endroit
    print MP, 'couleur est mal placee' if MP == 1 else 'couleurs sont mal placees'
    print BP, 'couleur est bien placee' if BP == 1 else 'couleurs sont bien placees' 
    ligne = '     '+essay+' '+str(MP)+' '+ str(BP) #on cree une nouvelle ligne pour l'historique des coups
    histoire.append(ligne)
    count = count + 1 #on compte le nombre de coups(max 10)
    waste = raw_input() #on attend enter pour afficher le prochain coup
    clear() 
    if BP == 4: #condition de victoire
        victoire = True
        break
    

for c in combinaison:
    solution = solution + c
clear()    
print '      ', solution #on affiche la solution
print '       ----'
for i, h in enumerate(histoire): #on affiche l'historique des coups
        print i, h
if victoire:
    print 'Victoire!!!'
else:
    print 'Defaite!!!'
print 'en', count, 'coup' if count == 1 else 'coups' # on affiche le nb de coups
            
