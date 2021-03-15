import timeit


def plusLeger(T: list, idebut:int = 0) -> list:
    """
    Trouve la valeur la plus petite d'un tableau d'entirs
    Paramètres d'entrée : 
        - T : tableau d'entiers
        - idebut : paramètre optionnel (valeur par défaut : 0)
    """
    n = len(T)
    imin = idebut  
    for i in range(idebut, n):
        if T[i] < T[imin]:
            imin = i
    return imin


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
        - boitePoids : tableau d'entiers
    """
    n = len(boitePoids)
    for i in range(n):
        valeurEchangee = boitePoids[i]
        iLeger = plusLeger(boitePoids, i)
        boitePoids[i] = boitePoids[iLeger]
        boitePoids[iLeger] = valeurEchangee
    return boitePoids



def triInsertion(L: list)-> list:
    """
    Réalise un tri par insertion
    Paramètres d'entrée : 
        - L : tableau d'entiers
    """  
    pass  # à supprimer


listeNombresTriee = triSelection([10, 3, 7 ,5 ,6, 1]) # trie la liste
print(listeNombresTriee) # affiche la liste

# listes triées
# pour trier dans l'ordre inverse, on fait sorted(L100, reverse = True)
L100 = [i for i in range(100)]
L1000 = [i for i in range(1000)]
L2000 = [i for i in range(2000)]
print(100, timeit.timeit('triSelection(L100)', globals=globals(), number= 5)/5)
print(1000, timeit.timeit('triSelection(L1000)', globals=globals(), number= 5)/5)
print(2000, timeit.timeit('triSelection(L2000)', globals=globals(), number= 5)/5)


tailleTableau = [ 200+i*200 for i in range(8) ]


# Création d'un graphique
# from matplotlib.pyplot import *
# x = [1,2,3,4]
# y = [10, 23, 45, 7]
# plot(x, y, 'x-r')
# show()