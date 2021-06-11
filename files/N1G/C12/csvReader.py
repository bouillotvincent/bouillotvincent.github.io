import csv

def importCSV(fichier : str, separateur = ";"):
    tCSV = csv.DictReader(open(fichier,'r'), delimiter = separateur)
#    print(tCSV)
    tableau = []
    for ligne in tCSV:
        #print(dict(ligne))
        tableau.append(dict(ligne))
    return tableau
    #return [dict(ligne) for ligne in tCSV]

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
        for (clé,valeur) in dico.items():
            if clé in listeCriteres:
                dicoFiltrer[clé]=valeur
        filtrerTableau.append(dicoFiltrer)
    return filtrerTableau
    #return [{clé:dico[clé] for clé in dico.keys() if clé in listeCriteres} for dico in tableau]

def triTable(tableau: list, critere: str, decroissant = False ):
    return sorted(tableau, key=lambda k: k[critere], reverse=decroissant)

def jointure(table1, table2, cle):
    if cle not in table1[0] or cle not in table2[0]:
        print(f"Aucun descripteur {cle} trouve dans ces tables.")
    else :
        tableJointe = []
        for ligne1 in table1:
            for ligne2 in table2:
                if ligne1[cle] == ligne2[cle]:
                    newDict = {cle1: value1 for (cle1, value1) in ligne1.items()}
                    for (cle2, value2) in ligne2.items():
                        if cle2 != cle:
                            newDict[cle2] = value2
                    tableJointe.append(newDict)
        return(tableJointe)


def verifieCle(table1, table2):
    print(table1[0],table2[0])
    for cle1 in table1[0]:
        if cle1 not in table2[0]:
            return False
    for cle2 in table2[0]:
        if cle2 not in table1[0]:
            return False
    return True

def fusion(table1, table2):
    if verifieCle(table1,table2):
        # on met les entêtes dans l'ordre du tableau 1
        table1 = filtrerColonne(table1, table1[0].keys())
        table2 = filtrerColonne(table2, table1[0].keys())
        #tableFusion = [dict(ligne) for ligne in (table1 + table2)]
        tableFusion = []
        for ligne in (table1 + table2):
            tableFusion.append(dict(ligne))
        return tableFusion
    else :
        print('Tables non fusionables')


#table = importCSV('exemple.csv')

#print(filtrerLigne(table, 'Nom', 'Céline'))
#print(filtrerColonne(table, ['Nom', 'Science']))
#print(triTable(table, 'Nom'))
#print(sorted(table, key=lambda k: k['Nom'], reverse=False))

#print(table[1]['Nom'])

#exportCSV(table,'exemple2.csv')



# donnéesDuFichier = open( 'exemple.csv', 'r')
# print(donnéesDuFichier)
# table = []
# hdr = []
# for ligne in donnéesDuFichier:
#     if len(hdr) == 0:
#         hdr = ligne.split(';')
#     else :
#         listLigne = ligne.split(';')
#         dico = {}
#         for i in range(len(listLigne)) :
#             dico[hdr[i]] = listLigne[i]
#         table.append(dico)
# print(table)

def fonction(x: list):
	return str(x**2)

#print('le carré de 4 est '+ fonction(4))
#carré = lambda x: str(x**2)
#print(f(4))
#print('le carré de 4 est ' +f(4))
