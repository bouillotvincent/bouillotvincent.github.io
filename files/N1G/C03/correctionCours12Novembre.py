def echangeAttendu(tab, i, j):
    # on sauvegarde le i-ème élément
    save = tab[i]
    # on écrase la valeur du i-ième élément par la valeur du j-ième
    tab[i] = tab[j]
    # le j-ième élément prend la valeur du ième élément telle que sauvegardée ligne 3
    tab[j] = save
    # on renvoie le tableau avec les deux éléments échangés
    return tab


def echange(tab, i, j):
    # Python permet d'échanger des éléments "sur place"
    tab[i], tab[j] = tab[j], tab[i]
    # on renvoie le tableau avec les deux éléments échangés
    return tab

print(echange([4,5,6,1,9],0,3)) #

def inverser(tab):
    """
    On utilise ici la fonction échange. On échange alors le premier élément (n°0) avec le dernier (n° -1),
    puis le n°1 avec l'avant dernier (n°-2) etc.
    len(tab)//2 nous indique qu'il faut que nous échangions seulement la moitié de notre tableau.
    """
    for i in range(len(tab)//2):
        tab = echange(tab, i, -1-i)
    return tab

def inverser2(tab):
    """
    L'idée la plus générale : on lit les éléments de la liste originale à l'envers en accédant au dernier élément
    via son indice. Son indice est N-1 (si la liste est constituée de N éléments). On fait ensuite :
    N-1
    N-1-1
    N-1-2
    N-1-3
    On lit donc le tableau initial à l'envers.
    """
    nouveauTab = []
    for i in range(len(tab)):
        nouveauTab.append(tab[len(tab)-i-1])
    return nouveauTab

def inverser3(tab):
    """ une idée encore différente! On va complètement démanteler la première ligne en récupérant le dernier élément avec pop
    On met ce dernier élément dans un nouveau tableau avec append (qui rajoute à la fin)
    """
    nouveauTab = []
    while tab != []:
        last = tab.pop(-1)
        nouveauTab.append(last)
        print(tab , nouveauTab)
    return nouveauTab

print(inverser([1,3,6,12,7]))
print(inverser2([1,3,6,12,7]))
print(inverser3([1,3,6,12,7]))

def verifierTaille(tab1, tab2):
    if len(tab1) == len(tab2):
        return True
    else:
        return False

def hamming(tab1, tab2):
    if verifierTaille(tab1, tab2) == True:
        diff = 0
        for i in range(len(tab1)):
            if tab1[i] != tab2[i]:
                diff = diff +1
        return diff
    else:
        return -1


print(hamming([1,4,5,6],[1,5,4,6]))