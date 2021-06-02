""" créer les objets à voler avec leurs caractéristiques """
dicoObjet = {}


# Que font ces deux lignes ?
tableau_trié = sorted(dicoObjet.items(), key = lambda a: a[1][2], reverse=True)
dicoObjet = {clé:valeur for clé, valeur in tableau_trié}

print(dicoObjet)

aVoler = []
poidsMax = 30
poids = 0

