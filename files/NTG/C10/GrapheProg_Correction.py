from GViz_Correction import *

class Noeud:
    
    def __init__(self, g = None, v=0, d=None):
        self.gauche = g
        self.valeur = v
        self.droit = d

class GrapheDico:
    def __init__(self):
        self.adj = {}

    def ajouteSommet(self, s):
        # Expliquer aux élèves ce qu'est un ensemble set() et quel est l'intérêt (logique ensembliste)
        if s not in self.adj:
            self.adj[s] = dict()

    def ajouteArc(self, s1, s2):
        # Préciser aux élèves l'utilisation de add() pour les ensembles
        self.ajouteSommet(s1)
        self.ajouteSommet(s2)
        if s2 not in self.adj[s1]: self.adj[s1][s2] = 1
        else: self.adj[s1][s2] += 1
        #print('ligne 29', s1, s2, self.adj[s1], self.adj[s1][s2])

    def ajouteArcs(self, s1, s2list):
        # Préciser aux élèves l'utilisation de add() pour les ensembles
        self.ajouteSommet(s1)
        for s2 in s2list.split(','):
            self.ajouteSommet(s2)
            if s2 not in self.adj[s1]: self.adj[s1][s2] = 1
            else: self.adj[s1][s2] += 1            

    def testArc(self, s1, s2):
        # test si un arc relie le sommet s1 au sommet s2
        return s2 in self.adj[s1]

    def listeSommets(self):
        return list(self.adj)

    def listeVoisins(self, s):
        return self.adj[s]

    def isDoubleArc(self, s1, s2):
        return self.testArc(s1,s2) and self.testArc(s2,s1)

    def symAjouteArc(self, s1, s2list):
        """ 
        Symmetrize the weights of a non-oriented graph 
        The adjacency matrix is now symmetric.
        """
        self.ajouteArcs(s1, s2list)
        for s2 in s2list.split(','):
            self.ajouteArc(s2, s1)

    def degre(self, s):
        return len(self.adj[s])


g = GrapheDico()
g.symAjouteArc('A','B,F')
g.symAjouteArc('B','C,D,G')
g.symAjouteArc('F','G,H')
g.symAjouteArc('C','E')
g.symAjouteArc('D','I')
g.symAjouteArc('G','I')
g.symAjouteArc('I','H,E')
Application(g, weight = False, arrow = False, width=300, height=300).mainloop()
