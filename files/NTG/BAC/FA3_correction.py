'''
Préparation de l'Epreuve Pratique :

Fiche Algorithmique 3
Arbres binaires : taille et hauteur
'''

# Partie fournie au candidat : aucune modification n'est à apporter
def est_vide(arbre: tuple) -> bool:
    '''Prédicat vrai si et seulement si l'arbre est vide'''
    return arbre == ()


def sous_arbre_gauche(arbre: tuple) -> tuple:
    '''renvoie le sous-arbre gauche d'un arbre non vide'''
    if est_vide(arbre):
        print(arbre)
        raise ValueError("L'arbre vide n'a pas de sous-arbre gauche")
    return arbre[1]


def sous_arbre_droit(arbre: tuple) -> tuple:
    '''renvoie le sous-arbre droit d'un arbre non vide'''
    if est_vide(arbre):
        print(arbre)
        raise ValueError("L'arbre vide n'a pas de sous-arbre droit")
    return arbre[2]


def valeur(arbre: tuple) -> tuple:
    '''renvoie la valeur de l'étiquette d'un arbre non vide'''
    if est_vide(arbre):
        print(arbre)
        raise ValueError("L'arbre vide n'a pas de valeur")
    return arbre[0]


VIDE = ()


# réponses du candidat : rédigez votre code ici


def taille(arbre: tuple) -> int:
    '''calcule la taille d'un arbre binaire'''
    if est_vide(arbre):
        return 0
    gauche = sous_arbre_gauche(arbre)
    droit = sous_arbre_droit(arbre)
    return 1 + taille(gauche) + taille(droit)


def hauteur(arbre: tuple) -> int:
    '''calcule la taille d'un arbre binaire'''
    if est_vide(arbre):
        return -1
    gauche = sous_arbre_gauche(arbre)
    droit = sous_arbre_droit(arbre)
    return 1 + max(hauteur(gauche), hauteur(droit))


def parcours_infixe(arbre: tuple, liste_valeur: list) -> list:
    '''réalise un parcours infixe de l'arbre et renvoie un tableau des valeurs rencontrées
    liste_valeur est un tableau contenant la liste des valeurs lues dans l'ordre infixe'''
    if est_vide(arbre):
        return
    parcours_infixe(sous_arbre_gauche(arbre), liste_valeur)
    liste_valeur.append(valeur(arbre))
    parcours_infixe(sous_arbre_droit(arbre), liste_valeur)
    return liste_valeur


# tests fournis aux candidat. Rien n'est à modifier.


def tests():
    '''réalise des tests sur les fonctions du candidat'''
    assert taille(VIDE) == 0
    assert hauteur(VIDE) == -1

    arbre_1 = (1, VIDE, VIDE)
    assert taille(arbre_1) == 1
    assert hauteur(arbre_1) == 0

    arbre_2 = (2, VIDE, VIDE)
    assert taille(arbre_2) == 1
    assert hauteur(arbre_2) == 0

    arbre_3 = (3, arbre_1, arbre_2)
    assert taille(arbre_3) == 3
    assert hauteur(arbre_3) == 1

    arbre_4 = (4, arbre_3, arbre_1)
    assert taille(arbre_4) == 5
    assert hauteur(arbre_4) == 2

    arbre_5 = (1, (2, (3, (4, (), ()), ()), (5, (6, (7, (), ()), ()), ())), ())
    assert taille(arbre_5) == 7
    assert hauteur(arbre_5) == 4

    assert parcours_infixe(arbre_1, []) == [1]
    assert parcours_infixe(arbre_2, []) == [2]
    assert parcours_infixe(arbre_3, []) == [1, 3, 2]
    assert parcours_infixe(arbre_4, []) == [1, 3, 2, 4, 1]
    assert parcours_infixe(arbre_5, []) == [4, 3, 2, 7, 6, 5, 1]

if __name__ == "__main__":
    tests()
