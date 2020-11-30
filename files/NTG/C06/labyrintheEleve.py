laby = \
[[0,1,0,0,0,0],
 [0,1,1,1,1,0],
 [0,1,0,1,0,0],
 [0,1,0,1,1,0],
 [0,1,1,0,1,0],
 [0,0,0,0,1,0],]


#lignes = 
#colonnes =  

def voisins(T, v):
    """
    >>> voisins(laby, [2,2])
    [(1, 2), (2, 1), (2, 3)]
    >>> voisins(laby, [5,0])
    []
    """
    V = []
    i, j = v[0], v[1] 
    for a in ......:
        if 0 <= i+a < lignes and T[i+a][j] == 1:
            ......
        if 0 <= j+a < colonnes and T[i][j+a] == 1: 
            ......
    return V


def depiler(pile):
    pile.pop(-1)


def empiler(pile, elt):
    pile.append(elt)


parcours(laby, (0,2), (5,5))






# Jeu de tests. 
# Si une AssertionError s'affiche, votre fonction ne passe 
# pas les tests et doit être modifiée !
assert(voisins(laby, [2,2]) == [(1, 2), (2, 1), (2, 3)])
assert(voisins(laby, [5,0]) == [])
assert(voisins(laby, [5,5]) == [(5,4)])

# if __name__=="__main__":
#     import doctest
#     doctest.testmod()