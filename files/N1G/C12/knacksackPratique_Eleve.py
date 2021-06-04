""" créer les objets à voler avec leurs caractéristiques """
dicoObjet = {}


def f(dicoObjet):
    # Que font ces deux lignes ?
    tableau_trié = sorted(dicoObjet.items(), key = lambda a: a[1][2], reverse=True)
    return {clé:valeur for clé, valeur in tableau_trié}

print(dicoObjet)
print(f(dicoObjet))

aVoler = []
poidsMax = 30
poids = 0

