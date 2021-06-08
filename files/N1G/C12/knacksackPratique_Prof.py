""" créer les objets à voler avec leurs caractéristiques """
#inventaire = {"A": [13,700],"B": [12,650], "C": [6,250], "D": [6,400],"E": [5, 100], 'F':[7, 200]}
inventaire = {"A": [13,700],"B": [12,650], "C": [6,250], "D": [6,400],"E": [5, 100]}
#inventaire = {"A": [13,250],"B": [12,400], "C": [18,100], "D": [5,100], "E": [5,250], "F": [3,200], "G": [15,400], "H": [16,1100], "I": [8,250]}

for objet, caracteristics in inventaire.items():
    inventaire[objet].append(caracteristics[1]/caracteristics[0])


def f(dico, col=2):
    tableau_trié = sorted(dico.items(), key = lambda a: a[1][col], reverse=True)
    return {clé:valeur for clé, valeur in tableau_trié}

inventaire = f(inventaire, 2)


aVoler = []
poidsMax = 30
poids = 0

for objet, valeur in inventaire.items():
    
    if  poids <= poidsMax:
        aVoler.append(objet)
        poids += valeur[0]

print(aVoler)