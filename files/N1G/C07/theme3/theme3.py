import timeit                     # mesure de temps de calcul
from matplotlib.pyplot import *   # bibliothèque graphique


def plusLeger(T: list, idebut:int = 0) -> list:
    """
    Trouve la valeur la plus petite d'un tableau d'entiers
    et renvoie la position de cette valeur
    Paramètres d'entrée : 
        - T : tableau d'entiers
        - idebut : paramètre optionnel (valeur par défaut : 0)
    """
    n = len(T)
    

    return 0 # à modifier


def triSelectionSimple(boitePoids: list)-> list:
    """
    Réalise un tri par sélection simplifié
    Paramètres d'entrée : 
        - boitePoids : tableaux d'entiers
    """
    n = len(boitePoids)
    boitePoidsTrie = []
    
    for _ in range(0,n):
        iLeger = plusLeger(boitePoids)
        boiteLegere = boitePoids.pop(iLeger)
        boitePoidsTrie.append(boiteLegere)

    return boitePoidsTrie


def triSelection(boitePoids: list)-> list:
    """
    Réalise un tri par sélection
    Paramètres d'entrée : 
        - boitePoids : tableaux d'entiers
    """
    n = len(boitePoids)
    
    return boitePoids


#--------- Faites vos tests ci-dessous ---------#
listeNombresTriee = triSelectionSimple([10, 3, 7 ,5 ,6, 1]) # trie la liste
print(listeNombresTriee) # affiche la liste



tailleTableau = [ 10**1,10**2,10**3,10**4,10**5,10**6 ]
tempsSelection = []

# Création d'un graphique
# x = [1,2,3,4]
# y = [10, 23, 45, 7]
# plot(x, y, 'x-r')
# show()