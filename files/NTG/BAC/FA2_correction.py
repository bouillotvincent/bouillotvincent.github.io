'''
Préparation de l'Epreuve Pratique :

Fiche Algorithmique 2
Recherche dichotomique
'''

def recherche_dichotomique(element: int, tableau_trie : list ) -> bool:
    '''Recherche si un entier appartient à un tableau d'entiers triés
    Renvoie un booléen : 
     - True si l'entier appartient à tableau_trie, 
     - False sinon.
    
    Version itérative.
    '''    
    a = 0
    b = len(tableau_trie)-1
    m = (a+b)//2
    while a <= b :
        if tableau_trie[m] == element :
            return True
        elif tableau_trie[m] > element :
            b = m-1
        else :
            a = m+1
        m = (a+b)//2
    return False


def recherche_dichotomique_recursive( element, liste_triee, a = 0, b = -1 ):
    '''Recherche si un entier appartient à un tableau d'entiers triés
    Renvoie un booléen : 
     - True si l'entier appartient à tableau_trie, 
     - False sinon.
    
    Version récursive, à faire si vous avez le temps.    
    '''   
    if b == -1 :   # à conserver
        b = len(liste_triee)-1    # à conserver
    m = (a+b)//2   
    if liste_triee[m] == element :  # Cas d'arrêt
        return True
    if a == b :     # Cas d'arrêt
        return False        
    if liste_triee[m] > element :
        return recherche_dichotomique_recursive(element, liste_triee, a, m-1)
    else :
        return recherche_dichotomique_recursive(element, liste_triee, m+1, b)



def tests():
    '''Réalise des tests sur les fonctions créées. Lève une exception si les
    conditions ne sont pas remplies
    Ne pas modifier cette fonction'''

    T = [1,2, 3,12,16,18,20,21,25,34]
    assert recherche_dichotomique(16, T) == True, 'Test 1 échoué'
    assert recherche_dichotomique(17, T) == False, 'Test 2 échoué'
    assert recherche_dichotomique(1, T) == True, 'Test 3 échoué'
    assert recherche_dichotomique(34, T) == True, 'Test 4 échoué'
    assert recherche_dichotomique(45, T) == True, 'Test 5 échoué'

    assert recherche_dichotomique_recursive(16, T) == True, 'Test 1 échoué'
    assert recherche_dichotomique_recursive(17, T) == False, 'Test 2 échoué'
    assert recherche_dichotomique_recursive(1, T) == True, 'Test 3 échoué'
    assert recherche_dichotomique_recursive(34, T) == True, 'Test 4 échoué'
    assert recherche_dichotomique_recursive(45, T) == True, 'Test 5 échoué'

if __name__ == "__main__":
    tests()
