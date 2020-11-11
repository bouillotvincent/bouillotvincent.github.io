trousseDeImene = ['stylo', 'colle', 'ciseaux à bout rond']
trousseDeRenzo = ['fluo', 'colle', 'souris']


def ajouteObjet(trousse):
    # on demande si un utilisateur veux rajouter quelque chose dans sa trousse, 
    # représentée par un tableau.
    objet = input('Quel objet veux-tu mettre dans ta trousse?')
    # tant que l'utilisateur répond quelque chose (rien se note : "" ), on fait :
    while objet != "":
        # on rajoute l'objet
        trousse.append(objet)
        # on affiche le contenu de la trousse
        print(trousse)
        # on redemande si on veux rajouter des objets
        objet = input('D"autres objets ?')

ajouteObjet(trousseDeImene)

def jetteContenuTrousse(trousse):
    # pour vider une trousse, le plus simple est de toujours enlever l'objet n°0 tant qu'il existe
    # quand il n'existe plus, la trousse (sous forme de tableau) est vide, soit []
    while trousse != []: # tant que j'ai quelque chose dans ma trousse :
        # j'enlève le 0ème
        objetEnlever = trousse.pop(0)
        print(objetEnlever, trousse)
    print('trousse vidée')
    
jetteContenuTrousse(trousseDeImene)

# # ajouteObjet(trousseDeImene)
# # print(trousseDeImene
# # ajouteObjet(trousseDeRenzo)
# # print(trousseDeRenzo)


tableau = [0,10,20,30,40,50,60,70,80]
for i in range(5):
    print(i, tableau[i])
print("tableau[-1]", tableau[-1])

tableau.pop(-1)

print(tableau[2:6]) # tous les éléments du n° 2 à n° 6-1 !
print(tableau[:6]) # tous les éléments du n° 0 à n° 6-1 !
print(tableau[2:]) # tous les éléments du n° 2 à la fin !

print(10 in tableau) # test : est-ce 10 est dans tableau?


"""Exercice 1"""

tab = [1,2,3,2,2,5]
""" 
ETAPE 1
exemple papier/crayon : on cherche 2 dans le tableau tab
un ordinateur va épeler le tableau nombre par nombre.
 - 1 = 2 ? non
 - 2 = 2 ? oui, je fais +1
 - 3 = 2 ? non
 - 2 = 2 ? oui, je fais +1
Ok, mais ca veut dire quoi "faire +1". Il faut enregistrer mes +1 dans une variable pour
connaitre le nombre de fois où j'ai fait +1
On peut alors écrire le programme ci-dessous:
"""

""" ETAPE 2 """
nb2 = 0
for valeur in tab:
    if valeur == 2: 
        nb2 = nb2 + 1
        print(valeur, nb2)
print(nb2)

""" ETAPE 3 """
# Je n'ai plus qu'à remplacer 2 par v car on peut vouloir cherche n'importe quel entier v
# Je replace tab par t car je ne veux pas me restreindre au tableau tab mais je veux étudier n'importe quel
# tableau t.
def occurrences(v, t):
    nb2 = 0
    for valeur in t:
        if valeur == v: 
            nb2 = nb2 + 1
            #print(valeur, nb2) # enlever le # pour débugguer et tester.
    return nb2 # A ne pas oublier !!

resultat = occurrences(2, tab)
print(resultat)

# nombreOccurrences = occurrences(2, tab)
# print(nombreOccurrences)

from random import randint

""" ETAPE 1 
On prend une feuille vide : c'est notre tableau vide.
On lance un dé et on écrit le résultat dans notre tableau vide (.append en Python)
On relance le dé et on réécrit le résultat etc.
On fait donc une boucle.
"""


""" ETAPE 2 """
# je teste la génération de 10 entiers aléatoires
# tableau = []
# for i in range(10):
#     a = randint(1,1000) # tirage aléatoire
#     tableau.append(a)  # on l'enregistre dans un tableau
#     print(tableau)

""" ETAPE 3 """
# on généralise pour un nombre n d'entiers
def aleatoire(n):
    tableau = []
    for i in range(n):
        a = randint(1,1000) # tirage aléatoire
        tableau.append(a)  # on l'enregistre dans un tableau
#        print(tableau)
    return tableau

tabAleatoire = aleatoire(10)
print(tabAleatoire)