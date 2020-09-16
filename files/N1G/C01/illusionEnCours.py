import turtle

""" Variables globales """
cote = 100
nCarre = 10
nLigne = 10
xBas = -400   # ne pas modifier
yHaut = 300   # ne pas modifier

fred = turtle.Turtle()
fred.shape('turtle')
fred.speed(6)

def carreColore(x, nombre):	
    """ 
    Exercice 10 
    Code à compléter
    """
    #couleur = choixCouleur(nombre)   # ...................	
    #fred.begin_fill()                # commence le coloriage	
    #fred.fillcolor(.........)        # remplit de la couleur choisie	
    #...............                  # trace un carré de côté x	
    #fred.end_fill()                  # fin du coloriage
    pass # à supprimer une fois la fonction complétée


def ligneDeCarre(posx, posy, x, n):	
    """ 
    Exercice 11
    Code à compléter
    """
    fred.pu()	
    fred.goto(posx, posy)	
    fred.pd()	
    #.........   # Code du a) 	
    #.........   # Code du a) 	
    #.........   # Code du a)


def damier(posx, posy, n, x):
    """ 
    Exercice 12
    Dessine un damier coloré
    """
    pass


turtle.exitonclick()