import random
import time
import timeit

maxVal = 2000
nVal = 1000
listeNombres = list(range(0,24,2))#sorted(random.choices(range(maxVal),k=nVal))

def rechercheNaive(L: list, elt: int)-> int:
    ''' Spécifications :
    Recherche d'un entier elt dans un tableau d'entiers. 
    Renvoie le nombre de fois où la comparaison a été faite si on trouve l'élément 
    Renvoie -1 sinon.
    '''
    for i in range(len(L)):
        #print("position ",i, " valeur ",L[i],elt)
        if elt == L[i]:
            return i
    return -1


def rechercheDicho(L: list, elt: int)-> int:
    tr = False
    deb = 0
    fin = len(L)-1
    cnt = 0
    while tr == False and deb <= fin:
        print('taille', len(L[deb:fin]))
        mil = (deb+fin) // 2
        #print(L[deb:fin+1])
        if L[mil] == elt:
            tr = True
        elif elt > L[mil] :
            deb = mil+1
        else :
            fin = mil-1
        cnt += 1
    return (-1 if not tr else cnt)

# taille Tableau
valeursX = [2**i for i in range(1,20)]

tDicho =[]
tNaive =[]
tableauIni = sorted(random.choices(range(maxVal),k=max(valeursX)))
for nVal in valeursX:
    print(nVal)
    listeNombres = tableauIni[:nVal]
    tDicho.append(timeit.timeit('rechercheDicho(listeNombres, -1)', globals=globals(), number=5)/5)
    tNaive.append(timeit.timeit('rechercheNaive(listeNombres, -1)', globals=globals(), number=5)/5)

print(valeursX)
print(tDicho)
print(tNaive)

from matplotlib.pyplot import *
subplot(121)
plot(valeursX, tNaive, '-xb')
plot(valeursX, tDicho, '--+r')
subplot(122)
loglog(valeursX, tNaive, '-xb')
loglog(valeursX, tDicho, '--+r')
show()