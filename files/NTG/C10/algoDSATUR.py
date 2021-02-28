def colorationDSATUR(G: GrapheDico):
    sommetsOrd = sorted(G.listeSommets(), key = lambda x: G.degre(x), reverse =True)
    couleur = {}
    degreMax = sommetsOrd.pop(0)
    couleur[degreMax] = 0 

    while sommetsOrd != []:
        maxDSAT = dsat(G, couleur)
        sommet2color = egalite(sommetsOrd, maxDSAT)

        for i, liste in enumerate(sommetsOrd):
            if liste[0] == sommet2color:
                iPop = i

        aColorier = sommetsOrd.pop(iPop)
        couleur[aColorier] = choixCouleur(G, aColorier, couleur)
    return couleur

def trouveMax(dico):
    maxi = -1
    for cle, valeur in dico.items():
        if maxi < valeur:
            maxVal = [cle]
            maxi = valeur
        elif maxi == valeur:
            maxVal.append(cle)
    return maxVal

def dsat(G, couleur):
    degreSat = {i:set() for i in G.listeSommets()}
    for sommet in couleur:
        for i in G.listeVoisins(sommet):
            degreSat[i].add(couleur[sommet])
    return trouveMax({s: len(col) for s, col in degreSat.items() if s not in couleur})

def egalite(sommetsOrd, maxDSAT):
    cles = [i for i in maxDSAT]
    for sommet in sommetsOrd:
        if sommet in cles:
            return sommet[0]
    raise Exception('Something went wrong')

def choixCouleur(G, sommet, couleur, n=10):
    A = {couleur[i] for i in G.listeVoisins(sommet) if i in couleur}  # Ceci est un set() = ensemble au sens mathématique
    for j in range(n):
        if j not in A:
            return j
    raise Exception('Please increase number of colors')

g.ajouteArcs("MATHEMATIQUES", "PHYSIQUE-CHIMIE,NUMERIQUE SC.INFORM.,HIST.GEO.GEOPOL.S.P.,SC.INGEN. & SC.PHYS.,SCIENCES VIE & TERRE,SC. ECONO.& SOCIALES,HUMAN.LITTER.PHILO.,LITT. ANGLAIS,LITT. ESPAGNOL")
g.ajouteArcs("PHYSIQUE-CHIMIE", "MATHEMATIQUES,SCIENCES VIE & TERRE")
g.ajouteArcs("HIST.GEO.GEOPOL.S.P.", "LITT. ANGLAIS,SC. ECONO.& SOCIALES,LITT. ESPAGNOL,MATHEMATIQUES,HUMAN.LITTER.PHILO.,LITT. ALLEMAND,SCIENCES VIE & TERRE")
g.ajouteArcs("LITT. ANGLAIS", "HIST.GEO.GEOPOL.S.P.,SC. ECONO.& SOCIALES,MATHEMATIQUES,SCIENCES VIE & TERRE,HUMAN.LITTER.PHILO.")
g.ajouteArcs("NUMERIQUE SC.INFORM.", "MATHEMATIQUES,LITT. ESPAGNOL,SCIENCES VIE & TERRE,SC. ECONO.& SOCIALES,SC.INGEN. & SC.PHYS.,HUMAN.LITTER.PHILO.")
g.ajouteArcs("SC. ECONO.& SOCIALES", "HIST.GEO.GEOPOL.S.P.,HUMAN.LITTER.PHILO.,MATHEMATIQUES,SCIENCES VIE & TERRE,LITT. ANGLAIS,LITT. ESPAGNOL,LITT. ALLEMAND,NUMERIQUE SC.INFORM.")
g.ajouteArcs("HUMAN.LITTER.PHILO.", "SC. ECONO.& SOCIALES,HIST.GEO.GEOPOL.S.P.,MATHEMATIQUES,NUMERIQUE SC.INFORM.,LITT. ANGLAIS")
g.ajouteArcs("LITT. ESPAGNOL", "HIST.GEO.GEOPOL.S.P.,NUMERIQUE SC.INFORM.,SC. ECONO.& SOCIALES,MATHEMATIQUES")
g.ajouteArcs("SC.INGEN. & SC.PHYS.", "MATHEMATIQUES,NUMERIQUE SC.INFORM.")
g.ajouteArcs("SCIENCES VIE & TERRE", "MATHEMATIQUES,PHYSIQUE-CHIMIE,SC. ECONO.& SOCIALES,NUMERIQUE SC.INFORM.,HIST.GEO.GEOPOL.S.P.,LITT. ANGLAIS")
g.ajouteArcs("LITT. ALLEMAND", "HIST.GEO.GEOPOL.S.P.,SC. ECONO.& SOCIALES")