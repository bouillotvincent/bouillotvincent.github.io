import turtle

#-----------------------#
# Exercice 1 : A tester
def dessiner(courbe, longueur, angle):
    turtle.tracer(0,0)            # accélération du tracé
    turtle.screensize(2000,2000)  # taille fenêtre graphique
    
    for caractere in courbe:
        if caractere == '+': turtle.left(angle)
        elif caractere == '-': turtle.right(angle)
        elif caractere in ['F', 'G']: turtle.forward(longueur)

    turtle.update()      # accélération du tracé
    turtle.exitonclick() # permet la fermeture de la fenêtre graphique

# tests de la fonction dessiner :
# dessiner()  # à décommenter


#-----------------------#
# Exercice 3 : A corriger
def regleKoch(chaine):
    """ 
        cette fonction applique la regle de Koch
        à une chaine de caractères 
    """
#     nouvelleChain = ''     # chaine vide
#     for lettre in chaine
#         if lettre = 'F':
#             nouvelleChaine = nouvelleChaine + 'F+F--F+F'
#         else :
#             nouvelleChaine = lettre
#     return nouvelleChaine
    pass

# tests de la fonction regleKoch
# print(regleKoch('F+F--F+F')) renvoie "F+F--F+F+F+F--F+F--F+F--F+F+F+F--F+F"

#-----------------------#
# Exercice 4 : A corriger
def courbeKoch(motifInitial, niter):
    """ 
        appelle niter fois regleKoch pour créer la courbe de Koch
        dont la finesse dépend de niter.

        niter : doit être inférieur à 6
    """
    assert niter <= 6, 'niter trop grand'  # test sur niter
    
    courbe = motifInitial
    compteur = 0
    while compteur < niter:
        nouveauMotif = regleKoch(courbe)
        courbe = nouveauMotif
        compteur = compteur + 1
    
    return courbe

# tests de la fonction courbeKoch
# pensez à commenter la ligne 18
# dessiner(courbeKoch('F',2), 50, 60)

#-----------------------#
# Exercice 5 : A créer
def floconKoch(motifInitial, niter):
    """ 
        crée une courbe représente un flocon de Koch complet
        en reproduisant 3 fois la courbe de Koch avec un finesse
        niter.
    """    
    flocon = ''
    # à compléter
    # à compléter
    # à compléter
    # à compléter
    # à compléter
    return flocon
    pass

# Tests exercice 5
longueur = 10
angle = 60
niter = 2
dessiner(floconKoch('F', niter), longueur, angle)