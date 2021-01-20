'''
Préparation de l'Epreuve Pratique :

Fiche Algorithmique 3
Arbres binaires : taille et hauteur
'''


def rendu_glouton(s: int, devise: list) -> list:
    '''rendu glouton renvoie une liste du nombre de pièces et de billets à rendre
    Exemple :     
    devise = [1, 2, 5, 10, 20, 50, 100, 200]
    s = 279 = 0x1 + 2x2 + 1x5 + 0x10 + 1x20 + 1x50 + 0x100 + 1x200
    rendu_glouton(s, devise) renvoie [0, 2, 1, 0, 1, 1, 0, 1]
    '''
    i = len(devise)-1
    p = [0]*len(devise)    
    while s > 0:
        if devise[i] <= s:
            s = s- devise[i]
            p[i] += 1
        else:
            i -= 1
        if i<0 : return 'Aucun rendu possible'
    return p


# tests fournis aux candidat. Rien n'est à modifier.


def tests():
    '''réalise des tests sur les fonctions du candidat'''
    devise_1 = [1, 10, 20, 50, 100, 200]
    assert rendu_glouton(8, devise_1) == [8, 0, 0, 0, 0, 0]

    devise_2 = [1, 2, 5, 10, 20, 50, 100, 200]
    assert rendu_glouton(279, devise_2) == [0, 2, 1, 0, 1, 1, 0, 1]

    devise_3 = [1, 2, 5, 10, 20, 50]
    assert rendu_glouton(279, devise_3) == [0, 2, 1, 0, 1, 5]

    devise_4 = [1, 6, 10]  # Cas non optimal...
    assert rendu_glouton(22, devise_4) == [2, 0, 2] 


if __name__ == "__main__":
    tests()
