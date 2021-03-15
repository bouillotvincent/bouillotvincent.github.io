class GrapheDico:

    def __init__(self):
        self.adj = {}
        self.couleur = {}

    def ajouteSommet(self, s):
        # Expliquer aux élèves ce qu'est un ensemble set() et quel est l'intérêt (logique ensembliste)
        if s not in self.adj:
            self.adj[s] = dict()
            self.couleur[s] = 'BLANC'

    def resetCouleur(self):
        for s in self.couleur:
            self.couleur[s] = 'BLANC'

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


    def parcoursLargeur(self, s):
        self.resetCouleur() # tous les sommets deviennent blancs
        self.couleur[s] = 'NOIR'
        distance = {s: 0}
        f = []
        f.append(s)
        while len(f) != 0:
            u = f.pop(0)
            for v in self.listeVoisins(u):
                if self.couleur[v] != 'NOIR':       
                    self.couleur[v] = 'NOIR'
                    f.append(v)
                    distance[v] = distance[u]+1
        return dico

    def parcoursProfondeurChemin(self, s):
        self.couleur[s] = 'NOIR'
        vus = {s}   # ensemble
        f = []
        f.append(s)
        while len(f) != 0:
            u = f.pop(-1)
            for v in self.listeVoisins(u):
                if self.couleur[v] != 'NOIR':
                    self.couleur[v] = 'NOIR'
                    f.append(v)
                    vus.add(v)
        return vus

    def parcoursProfondeur(self, s):
        self.resetCouleur()
        self.couleur[s] = 'NOIR'
        vus = {s:None}
        f = []
        f.append(s)
        while len(f) != 0:
            u = f.pop(-1)
            for v in self.listeVoisins(u):
                if self.couleur[v] != 'NOIR':
                    self.couleur[v] = 'NOIR'
                    f.append(v)
                    vus[v] = u
        return vus

    def existeChemin(self, u, v):
        return v in self.parcoursProfondeur(u)

    def construireChemin(self, u, v):
        if self.existeChemin(u, v):
            arrivee = v
            chemin = []
            vus = self.parcoursProfondeur(u)
            while arrivee != u :
                chemin.append(arrivee)
                arrivee = vus[arrivee]
            chemin.append(u)
            return chemin[::-1]
        return None