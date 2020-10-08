def separateur():
    print("-"*10)
    

separateur()
print("Exercice 3")
class CompteBancaire:
    """ 
    le but de ce programme est d'écrire des méthodes et des attributs.
    attention, ce programme ne respecte pas l'encapsulation 
    """
    def __init__(self, montant):
        self.solde = montant
    
    def transfert(self, autreCompte, montant):
        autreCompte.solde +=  montant
        self.solde -= montant
    
    def prelevement(self, autreCompte, montant):
        self.solde += montant
        autreCompte.solde -= montant

    def etat(self):
        if self.solde > 0 :
            return "Positif"
        elif self.solde < 0 :
            return "Négatif"
        return "Nul"

alan = CompteBancaire(2000)
tim = CompteBancaire(1500)

alan.transfert(tim, 2200)  # alan transfert à tim
print(alan.etat())

separateur()
print("Exercice 4")
from math import pi, cos, sin
class Angle:

    def __init__(self, angle: int):
        self.angle = angle % 360
    
    def __str__(self):
        """ Accesseur = accède à la variable privée et la renvoie """
        return f"{self.angle} degrés"
    
    def ajoute(self, autreAngle):
        """ Mutateur = change la valeur de l'attribut """
        self.angle = (self.angle + autreAngle.angle) % 360

    def deg2rad(self):
        return (self.angle * pi)/180
    
    def cos(self):
        return round(cos(self.deg2rad()),3)

    def sin(self):
        return round(sin(self.deg2rad()),3)
    
a = Angle(45)
b = Angle(90)
a.ajoute(b)
print(a)
print(a.cos())
print(a.sin())  

"""Exercice 5"""
separateur()
class Fraction:

    def __init__(self, jean, pierre):
        self.num = jean
        if pierre <=0 : raise ValueError('Le dénominateur doit être strictement positif.')
        self.denom = pierre # on arrive à cette ligne seulement si pierre > 0
        self.reduire()

    def __str__(self):
        return f"{self.num} / {self.denom}" if self.denom !=1 else f"{self.num}"

    def __eq_old__(self, autreFraction):
        if self.num/self.denom == autreFraction.num/autreFraction.denom:
            return True
        return False

    def __eq__(self, autreFraction):
        if self.num == autreFraction.num and self.denom == autreFraction.denom:
            return True
        return False

    def __lt__(self, autreFraction):
        if self.num/self.denom < autreFraction.num/autreFraction.denom:
            return True
        return False

    def __add__(self, autreFraction):
        p = self.num*autreFraction.denom +autreFraction.num *self.denom
        q = self.denom*autreFraction.denom
        return Fraction(p, q)

    def __mul__(self, autreFraction):
        p = self.num * autreFraction.num 
        q = self.denom * autreFraction.denom
        return Fraction(p, q)

    def reduire(self):
        """ méthode limitant le nombre de calculs """
        # on cherche des diviseurs entre 2 et N/2+1
        intervalle = list(range(1, int(self.num/2)+1))
        i = 1
        div = []  # liste des diviseurs
        while i in intervalle :
            if self.num % i == 0: # si i est un diviseur alors N/i est aussi un diviseur car i * (N/i) = N
                intervalle = list(range(i,int(self.num/i)+1)) # l'intervalle devient plus petit.
                div.extend([i,int(self.num/i)]) # ajout dans la liste
            i += 1

        div.sort()

        for i in div:
            if self.denom % i == 0: pgcd = i

        self.num = int(self.num/pgcd)
        self.denom = int(self.denom/pgcd)



a = Fraction(14,7)
print(a)
b = Fraction(4,8)
print(b)
print(a == b)
print(a*b)
print(a+b)
c = Fraction(4, 16)
print(c)

"""Exercice 6"""
separateur()
class Intervalle:

    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def __str__(self):
        return f"[{self.a} , {self.b}]" if self.estVide() else "∅"

    def estVide(self):
        """ 
        si a < b est True, on renvoie True
        sinon (si a < b est False), on renvoie False
        donc, on peut écrire : return a < b 
        """
        return self.a < self.b
    
    def __len__(self):
        """ 
        si b > a, b-a est positif.
        si b < a, b-a est négatif alors que l'on veut renvoyer une longueur 0
        On prend donc le maximum entre b-a et 0 :
        """
        return max(self.b - self.a, 0)

    def __contains__(self, x):
        return self.b >= x >= self.a
    
    def intersection(self, intv):
        """
            Imaginons le cas suivant :
              self.a   self.b
                |--------|
                intv.a   intv.b
                   |--------|
            L'intersection est : 
                   |-----|
            La borne minimum est le maximum des a et la borne maximum le minimum des b.
        """
        return Intervalle(max(self.a, intv.a), min(self.b, intv.b))

    def union(self, intv):
        """
            Imaginons le cas suivant :
              self.a   self.b
                |--------|
                intv.a   intv.b
                   |--------|
            L'intersection est : 
                |-----------|
            La borne minimum est le minimum des a et la borne maximum le maximum des b
            SI self.a ou intv.a est compris dans l'autre intervalle. 

        """
        if self.a in intv or intv.a in self:
            return Intervalle(min(self.a, intv.a), max(self.b, intv.b))
        else:
            return Intervalle(self.a, self.b), Intervalle(intv.a, intv.b)

I1 = Intervalle(1,4)
I2 = Intervalle(3,5)
I3 = I1.union(I2)
print(I3)


"""Exercice 6"""
separateur()
class Tableau:

    def __init__(self, imin, imax, v):
        """
            on initialise les attributs premiers et contenu
            pour contenu, on utilise le raccourci : ['a']*3 = ['a', 'a', 'a']
        """
        self.premier = imin
        self.contenu = [v]*(imax-imin+1)
    
    def __len__(self):
        return len(self.contenu)
    
    def _indiceValide(self, i):
        """ on regarde si l'indice est contenu dans l'intervalle [imin, imax] """
        if i < self.premier or i >=self.premier + len(self):
            raise IndexError(i)
    
    def __getitem__(self, i):
        """ pour avoir le i-ème indice, il faut tout décaler de self.premier """
        self._indiceValide(i)
        return self.contenu[i-self.premier]
    
    def __setitem__(self, i, v):
        self._indiceValide(i)
        self.contenu[i-self.premier] = v
    
    def __str__(self):
        return str(self.contenu)
    
t = Tableau(-5, 12, 1)
print(t)
t[-5] = 0
t[-3] = 88
t[12] = -7
print(t)
print(t[-3])
print(len(t))