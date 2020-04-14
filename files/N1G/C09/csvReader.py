import csv

def importCSV(fichier : str, separateur = ";"):
    tCSV = csv.DictReader(open(fichier,'r'), delimiter = separateur)
    tableau = []
    for ligne in tCSV:
        tableau.append(dict(ligne))
    return tableau

def exportCSV(tableau : list, fichier : str):
    header = tableau[0].keys()
    fichierCSV = csv.DictWriter(open(fichier, 'w'), fieldnames = header)
    fichierCSV.writeheader()
    for ligne in tableau:
        fichierCSV.writerow(ligne)
    return None

def filtrerLigne(tableau : list, critere : str, valeur : str):
    filtrerTableau = []
    for dico in tableau:
        if(dico[critere] == valeur):
            filtrerTableau.append(dico)
    return filtrerTableau
    #return [filtrerTableau for dico in tableau if dico[critere] == valeur]


def filtrerColonne(tableau : list, listeCriteres : list):
    filtrerTableau = []
    for dico in tableau:
        dicoFiltrer = {}
        for (cle,valeur) in dico.items():
            if cle in listeCriteres:
                dicoFiltrer[cle]=valeur
        filtrerTableau.append(dicoFiltrer)
    return filtrerTableau
    #return [{cle:dico[cle] for cle in dico.keys() if cle in listeCriteres} for dico in tableau]

def triTable(tableau: list, critere: str, decroissant = False ):
    return sorted(tableau, key=lambda k: k['Nom'], reverse=decroissant)