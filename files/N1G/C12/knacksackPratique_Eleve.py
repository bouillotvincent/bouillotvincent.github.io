""" créer les objets à voler avec leurs caractéristiques """
dicoObjet = {}


def f(dicoObjet, col):
    # Que font ces deux lignes ?
    print(dicoObjet.items())
    tableau_trié = sorted(dicoObjet.items(), key = lambda a: a[1][col], reverse=True)
    return {clé:valeur for clé, valeur in tableau_trié}

print(dicoObjet)

for objet, caracteristique in dicoObjet.items():
    print(objet, caracteristique)

aVoler = []
poidsMax = 30
poids = 0

