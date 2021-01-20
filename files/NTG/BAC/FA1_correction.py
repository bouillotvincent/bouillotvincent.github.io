'''
Préparation de l'Epreuve Pratique :

Fiche Algorithmique 1
Algorithmes de parcours d'un tableau
'''

def moyenne_tableau_2d(tableau: list) -> float:
    '''Calcule la moyenne d'un tableau à double entrée'''
    somme = 0
    n = 0
    for i in tableau:
        for j in i:
            somme += j
            n += 1  # prend en compte des tailles différentes pour chaque ligne
    return somme/n


def maximum_tableau_1d(tableau: list) -> tuple:
    '''Trouve le maximum d'un tableau à une entrée :
    Renvoie un tuple constitué du (maximum, indice_du_maximum)
    Si deux éléments sont égaux, renvoie l'indice du premier élément trouvé'''
    maxi = (tableau[0], 0)
    for i, elt in enumerate(tableau):
        if elt>maxi[0]:
            maxi = (elt, i)
    return maxi

def recherche_dans_chaine_iterative(chaine: str, v: str) -> bool:
    '''Recherche une valeur v dans une chaine de caractères.
    v peut être constitué de plus d'une lettre.
    Toute amélioration algorithmique sera appréciée mais 
    l'algorithme de Boyer-Moore n'est pas demandée.
    
    Renvoie True si v est dans chaine. False sinon.
    
    Version itérative
    '''
    taille = len(v)
    pos = 0
    while pos<=len(chaine)-taille:
        i = 1
        while chaine[pos+i-1]==v[i-1] and i <= taille:
            if i == taille: return True
            i += 1
        pos += i
    return False

def recherche_dans_chaine_recursive(chaine: str, v: str) -> bool:
    '''Recherche une valeur v dans une chaine de caractères

    Renvoie True si v est dans chaine. False sinon.

    Version récursive, à faire si vous avez le temps.
    '''
    if len(chaine) < len(v):
        return False
    return v == chaine[0:len(v)] or recherche_dans_chaine_recursive(chaine[1:], v)



def tests():
    '''Réalise des tests sur les fonctions créées. Lève une exception si les
    conditions ne sont pas remplies
    Ne pas modifier cette fonction'''

    def affichage(i, vs, vc):
        print(f'Test {i}:')
        print(f'{vs} = {vc}')
        print(f'*'*20)

    # premier test
    tableau_1 = [[1]]
    valeur_souhaitee = 1.0
    valeur_comparee = moyenne_tableau_2d(tableau_1)
    affichage(1, valeur_souhaitee, valeur_comparee)
    assert abs(valeur_souhaitee-valeur_comparee)<1e-6, 'Test 1 échoué' 

    # second test
    tableau_2 = [[1, 2, 3],
                 [1, 2, 3],
                 [1, 2, 3]]
    valeur_souhaitee = 2.0
    valeur_comparee = moyenne_tableau_2d(tableau_2)
    affichage(2, valeur_souhaitee, valeur_comparee)
    assert abs(valeur_souhaitee-valeur_comparee)<1e-6, 'Test 2 échoué' 

    # troisième test
    tableau_3 = [[3, 3, 6],
                 [5, 3, 4],
                 [10, 1, 1],
                 [2, 3, 7]]
    valeur_souhaitee = 4.0
    valeur_comparee = moyenne_tableau_2d(tableau_3)
    affichage(3, valeur_souhaitee, valeur_comparee)
    assert abs(valeur_souhaitee-valeur_comparee)<1e-6, 'Test 3 échoué' 

    # quatrième test
    tableau_4 = [[1, 1, 10],
                 [1, 2, 2],
                 [3, 3, 4]]
    valeur_souhaitee = 3.0
    valeur_comparee = moyenne_tableau_2d(tableau_4)
    affichage(4, valeur_souhaitee, valeur_comparee)
    assert abs(valeur_souhaitee-valeur_comparee)<1e-6, 'Test 4 échoué' 

    print('-'*20)
    print('-'*20)

    tableau1 = [5]
    assert maximum_tableau_1d(tableau1) == (5,0), 'Test 1 échoué'
    tableau2 = list(range(10))
    assert maximum_tableau_1d(tableau2) == (9,9), 'Test 2 échoué'
    tableau3 = [-20000, -26700, -32000, -78904, -19000]
    print(maximum_tableau_1d(tableau2))
    print(maximum_tableau_1d(tableau3))
    assert maximum_tableau_1d(tableau3) == (-19000,4), 'Test 3 échoué'
    tableau4 = [5, 28, 6, 28, 4, 28]
    assert maximum_tableau_1d(tableau4) == (28,1), 'Test 4 échoué'

    print('-'*20)
    print('-'*20)

    chaine = "L'arbre qui cache la foret."
    assert recherche_dans_chaine_iterative(chaine, 'q') == True, 'Test 1 échoué'
    assert recherche_dans_chaine_iterative(chaine, 'z') == False, 'Test 2 échoué'
    assert recherche_dans_chaine_iterative(chaine, 'fo') == True, 'Test 3 échoué'
    assert recherche_dans_chaine_iterative(chaine, "foret.") == True, 'Test 4 échoué'

    assert recherche_dans_chaine_recursive(chaine, 'q') == True, 'Test 1 échoué'
    assert recherche_dans_chaine_recursive(chaine, 'z') == False, 'Test 2 échoué'
    assert recherche_dans_chaine_recursive(chaine, 'fo') == True, 'Test 3 échoué'
    assert recherche_dans_chaine_recursive(chaine, "foret.") == True, 'Test 4 échoué'

if __name__ == "__main__":
    tests()
