import csv

donneesDuFichier = open( 'exemple.csv', "r")
print(donneesDuFichier)

def importCSV(fichier : str, separateur = ";"):
    tCSV = csv.DictReader(open(fichier, 'r'), delimiter = separateur)
    tableau = []
    for ligne in tCSV:
        tableau.append( dict(ligne) )
        # print(ligne, dict(ligne))
    return tableau

def exportCSV(tableau : list, fichier : str):
    header = tableau[0].keys()   # récupère les en-têtes du fichier CSV à exporter
    fichierCSV = csv.DictWriter(open(fichier, 'w'), fieldnames = header)
    fichierCSV.writeheader()
    for ligne in tableau:
        fichierCSV.writerow(ligne)
    return None

table = importCSV('exemple.csv')
print(table)
exportCSV(table, 'exemple2.csv')