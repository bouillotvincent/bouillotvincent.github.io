class Maillon:
    def __init__(self):
            self.valeur = None
            self.suivant = None # Pas de maillon suivant


class ListeC:
	def __init__(self):
		# création d'une liste vide
		self.tete = None

	def est_vide(self):
		# test si la liste est vide
		return self.tete is None
	
	def __len__(self): 
		""" Renvoie le nombre de Maillons de la liste L 
		méthode POO équivalente à la fonction taille()""" 
		m = self.tete
		l = 0 
		while m is not None:
			l += 1
			m = m.suivant
		return l

	def _getlastitem(self): 
		""" Donne la valeur du dernier Maillon de la liste L ( L[-1] )""" 
		m = self.tete
		l = 0
		while m is not None:  # Le maillon actuel est-il None ?
			a = m.valeur      # j'enregistre la valeur du maillon actuel
			m = m.suivant     # le maillon que l'on va regarder est le suivant du maillon actuel
		return a # on renvoie la valeur du dernier maillon (avant que m soit None.)

	def __getitem__(self, i): 
		""" Renvoie Maillon d'indice i dans la liste L """ 
		j = 0
		m = self.tete 
		if i == -1:  # astuce pour programmer le L[-1]
			return self._getlastitem()
		while j < i: # on fait comme pour la taille mais on s'arrête à un i donné.
			j += 1
			if m is None : raise IndexError("Ton indice est trop grand!")  # gestion des erreurs
			m = m.suivant
		return m.valeur

	def __str__(self):
		m = self.tete
		affichage = f"L->"
		j = 0
		while m is not None:
			print(m.suivant, m.valeur)
			affichage += f"[M{j} | {m.valeur}] -> " 
			m = m.suivant
			j += 1
		affichage += "None"
		return affichage

	def pop(self): 
		""" Supprime le 1er maillon de la liste L et le renvoie """
		t = self.tete
		self.tete = self.tete.suivant
		return t.valeur

	def lenR(self):
		""" lenR initialise la fonction récusrive compteMaillon : on se débarasse de la tete """
		if self.tete is None: return 0
		return 1+self.compteMaillon(self.tete)

	def compteMaillon(self, m):
		""" Pour compter les Maillons de manière récursive on fait +1 et on compte combien de 
		maillons sont présents parmi les suivants """
		if m.suivant is None:
			return 0
		return 1 + self.compteMaillon(m.suivant)

	def getitemR(self, n):
		return self.nieme_element(n, self.tete)
	
	def nieme_element(self, n, m):
		try :
			if n == 0:
				return m.valeur
			return self.nieme_element(n-1, m.suivant)
		except : 
			raise IndexError('Index trop grand ou trop petit')

	def reverse(self):
		self.tete = self.renverser()

	def renverser(self):
		""" méthode renverser est la méthode bonus...
		essayer de comprendre son fonctionnement, spécialement en faisant un dessin.
		C'est très joli algorithmiquement !
		"""
		r = None
		c = self.tete
		while c is not None:
			p = Maillon()
			p.valeur = c.valeur
			p.suivant = r
			r = p
			c = c.suivant
		return r

L = ListeC()
M1, M2 = Maillon(), Maillon()
M2.suivant = M1
M1.valeur = 'canard'
M2.valeur = 'cygne'
M3 = Maillon()
M3.valeur = "poule d'eau"
M1.suivant = M3
L.tete = M2
print(L.tete.suivant)
print(len(L))
print(L[0])
print(L[1])
print(L[-1])
print(L)
print(L.pop())
print('ici',L)

def est_vide(L):
   return L.tete is None

def taille(L): 
	""" Renvoie le nombre de Maillons de la liste L """ 
	m = L.tete
	l = 0 
	while m is not None:
		l += 1
		m = m.suivant
	return l

def genererGrosseListe(n):
	""" génère une liste des n premiers entiers au carré """
	L = ListeC()
	M = [Maillon() for i in range(n+1)]
	for i in range(n):
		M[i].valeur = i**2
		M[i].suivant = M[i+1]
	M[n].valeur = n**2
	L.tete=M[0]
	return L

print(genererGrosseListe(2))
print(taille(genererGrosseListe(2)))