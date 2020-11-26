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


def verification(expr):
    """
    verification vérifie qu'une expression contient le bon nombre de parenthèses ouvrantes et fermantes.
    """
    P = Pile()             # on utilise l'objet Pile
    for car in expr:       # on parcourt tous les cacactères de l'expression
        if car == '(':     # si le caractère est une parenthèse ouvrante, on empile.
            P.empiler(car)
        elif car == ')':   # si la pile contient une parenthèse fermante
            if P.est_vide(): # si la pile est vide, clairement, on essaie de fermer une parenthèse que l'on n'a pas ouverte. On renvoie False
                return False
            P.depiler()    # sinon on dépile
    '''
    Cette notation est très lourde : Si P.est_vide est True, alors on renvoie True
    Sinon, on renvoie False. En fait, autant renvoyer P.est_vide()
    if P.est_vide() == True:
        return True
    else:
        return False
    '''
    return P.est_vide()

print(verification('(a+b)'))
print(verification('(a+b))'))
print(verification('(a+b'))
print(verification('(sin(x+y*(2+1))+b))'))

def verificationGros(expr):
    """
    verification vérifie qu'une expression contient le bon nombre de parenthèses ouvrantes et fermantes.
    """
    P = Pile()             # on utilise l'objet Pile
    for car in expr:       # on parcourt tous les cacactères de l'expression
        if car == '(':     # si le caractère est une parenthèse ouvrante, on empile.
            P.empiler(car)
        elif car == ')':   # si la pile contient une parenthèse fermante
            if P.est_vide(): # si la pile est vide, clairement, on essaie de fermer une parenthèse que l'on n'a pas ouverte. On renvoie False
                return False
            val = P.depiler()    # sinon on dépile
            if not(val == '('): return False

        if car == '[':     # si le caractère est une parenthèse ouvrante, on empile.
            P.empiler(car)
        elif car == ']':   # si la pile contient une parenthèse fermante
            if P.est_vide(): # si la pile est vide, clairement, on essaie de fermer une parenthèse que l'on n'a pas ouverte. On renvoie False
                return False
            val = P.depiler()    # sinon on dépile
            if not(val == '['): return False
            
    return P.est_vide()


print('---')
print(verificationGros('(a+b)'))
print(verificationGros('([a+1]**2+b)'))
print(verificationGros('([a+1)]**2+b)'))
print(verificationGros('([(a+1)]**2+b)'))



def verification2(expr):
    """
    verification vérifie qu'une expression contient le bon nombre de parenthèses et de crochets ouvrantes et fermantes.
    """
    P = Pile()             # on utilise l'objet Pile
    for car in expr:       # on parcourt tous les cacactères de l'expression
        if car in ['(', '[']:     # si le caractère est une parenthèse ouvrante, on empile.
            P.empiler(car)
        elif car in [')', ']']:   # si la pile contient une parenthèse fermante
            if P.est_vide(): # si la pile est vide, clairement, on essaie de fermer une parenthèse que l'on n'a pas ouverte. On renvoie False
                return False
            symbole = P.depiler()  # sinon on dépile 
            # problème : quelles sont les cas qui sont correctes ? Seulement DEUX.
            # La parenthèse/crochet fermante correspond à la parenthèse/crochet ouvrante. 
            #
            # Si les parenthèses correspondent OU les crochets correspondent, on aura TRUE. 
            # Mais, nous souhaitons savoir les cas qui sont faux pour renvoyer FALSE. On utilise 
            # donc la négation NOT pour prendre l'inverse.
            if not ((symbole == '(' and car == ')') or (symbole == '[' and car == ']')):
                return False
    return P.est_vide()

print('---')
print(verification2('(a+b)'))
print(verification2('([a+1]**2+b)'))
print(verification2('([a+1)]**2+b)'))
print(verification2('([(a+1)]**2+b)'))
