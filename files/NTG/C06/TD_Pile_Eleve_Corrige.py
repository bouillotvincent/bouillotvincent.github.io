def pile():
    """ crée de la pile vide """ 
    return []

def est_vide(p):
    """renvoie True si la pile est vide
     et False sinon"""
    return p == []

def empiler(p, x):
    """Ajoute l’élément x à la pile p"""
    p.append(x)

def depiler(p):
    """dépile et renvoie l’élément au sommet de la pile p""" 
    assert not est_vide(p), "Pile vide"
    return p.pop()

def taille(p):
    pTemp = pile()
    compteur = 0
    print(p)
    while not est_vide(p): # pile non vide
        val = depiler(p)
        empiler(pTemp, val)
        compteur += 1
    while not est_vide(pTemp): # pile non vide
        val = depiler(pTemp)
        empiler(p, val)
    return compteur

def sommet(p):
    a = depiler(p)  # dépilage et lecture de la valeur
    empiler(p, a)   # rempilage
    return a        # renvoi de la valeur



p = pile()
for i in range(6):
    empiler(p, 2*i)

print(taille(p))


class Pile:
    """ classe Pile : 
    création d’une instance Pile avec à partir d'une liste """
    def __init__(self):
        "Initialisation d’une pile vide"
        self.L = []

    def est_vide(self):
        """teste si la pile est vide""" 
        return self.L == []

    def depiler(self): 
        """dépile si la pile n'est pas vide"""
        assert not self.est_vide(), 'Pile vide'
        return self.L.pop(-1)

    def empiler(self,x): 
        """empile"""
        self.L.append(x)

P = Pile()
P.est_vide()
P.empiler(3)
P.empiler(5)
P.empiler(7)
print(P.L)