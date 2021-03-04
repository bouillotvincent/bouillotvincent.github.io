from GViz import *

class Noeud:
    
    def __init__(self, g = None, v=0, d=None):
        self.gauche = g
        self.valeur = v
        self.droit = d

class GrapheDico:
    """
        Représentation d'un graphe par dictionnaire d'adjacence
        
        Paramètres d'entrée : aucun.

        Exemple : 
        g = GrapheDico()
        g.ajouteArc('A', 'B')
        g.ajouteArc('B', 'A')
        g.ajouteArc('B', 'C')
        g.ajouteArc('C', 'B')
    
        Pour la représentation de votre Graphe, voir le manuel de la bibliothèque GViz.py
    """

    def __init__(self):
        """ constructeur : initialise le dictionnaire d'adjacence """

    def ajouteSommet(self, s):
        """ Ajoute un sommet au Graphe """
        if s not in self.adj:
            self.adj[s] = list()

    def ajouteArc(self, s1, s2):
        """ Ajoute un arc entre deux sommets s1 et s2. Crée le sommet s1 ou s2 si celui-ci n'existe pas."""

    def ajouteArcs(self, s1, s2list):
        """ Ajoute n arc entre un sommet s1 et une liste de sommets s2list. 
        Crée le sommet s1 ou tous les sommets de s2list si ceux-ci n'existent pas.
        
        Exemple : 
        ajouterArcs("A", "B,C,D,F") crée 4 arcs d'un coup !
        """


    def testArc(self, s1, s2):
        """ test si un arc relie le sommet s1 au sommet s2"""
        return 

    def listeSommets(self):
        """ renvoie la liste des sommets du graphe """
        return

    def listeVoisins(self, s):
        """ renvoie la liste des voisins d'un sommet s """
        return 

    def isDoubleArc(self, s1, s2):
        """ détermine si un sommet s1 est relié à s2 et s2 relié à s1.
        Utile uniquement pour les graphes orientés. """
        return 




G = GrapheDico()
G.ajouteArc('A','B')
G.ajouteArc('B','A')
G.ajouteArc('C','H')
G.ajouteArc('H','C')

Application(G).mainloop()