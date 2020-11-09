dessin_depart= [
"00011000",
"01111110",
"01000001",
"10000010",
"10001111",
"01100010",
"00011100",
"00001000",
]


def affiche(dessin):
    for i in range (len(dessin)):
        for j in range (len(dessin[0])):
            print(dessin[i][j], end="")
        print(end='\n')
    print()

def rotationAux(px, x, y, t):
    """ 
    description de la fonction à ajouter
    """
    if t == 1: return
    t = t // 2
    rotationAux(px, x  , y  , t)
    rotationAux(px, x+t, y  , t)
    rotationAux(px, x  , y+t, t)
    rotationAux(px, x+t, y+t, t)
    #print(t, px)
    for i in range(x, x+t):
        for j in range(y, y+t):
            px[i][j], px[i+t][j], px[i+t][j+t], px[i][j+t] = \
                px[i][j+t], px[i][j], px[i+t][j], px[i+t][j+t]
    print(t)
    affiche(px)

    
def rotation(px):
    """ 
    description de la fonction à ajouter
    """
    pass

def rotationIterative(dessin):
    return [''.join([dessin[i][len(dessin[0]) - j-1] for i in range(len(dessin))]) for j in range(len(dessin[0]))]


affiche(dessin_depart)
px = rotation(dessin_depart)
affiche(px)
affiche(rotationIterative(dessin_depart))