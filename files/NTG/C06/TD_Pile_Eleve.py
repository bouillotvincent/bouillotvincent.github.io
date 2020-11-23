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


class Pile:
    """ classe Pile : 
    création d’une instance Pile avec à partir d'une liste """
    def __init__(self):
        "Initialisation d’une pile vide"
        self.L = []

    def est_vide(self):
        """teste si la pile est vide""" 
        return

    def depiler(self): 
        """dépile si la pile n'est pas vide"""

        return

    def empiler(self,x): 
        """empile"""
        