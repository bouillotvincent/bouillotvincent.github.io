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

def filtrerLigne(tableau : list, critere : str, valeur : str):
    filtrerTab = []
    for i in range(len(tableau)):   
        eleve = tableau[i]
        if eleve[critere] == valeur:
            filtrerTab.append(eleve)
            print(i, eleve, eleve["Nom"])
    return filtrerTab


table = importCSV('exemple.csv')
print(table)
eleve = {'Nom': 'Julien', 'Francais':12, 'Science':15, 'Histoire':3}
table.append(eleve)

tableF = filtrerLigne(tableau = table, critere = 'Francais', valeur = '14')
exportCSV(tableF, 'exemple_Julien.csv')

