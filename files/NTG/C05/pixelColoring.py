# Dessin du départ à remplacer par une ouverture de fichier le contenant
# puis/ou une vraie image à terme
dessin_depart= [
"01111110",
"01000001",
"10000010",
"10001111",
"01100010",
"00011100",
]

def affiche(dessin):
    for i in range (len(dessin)):
#        print(end='"')
        for j in range (len(dessin[0])):
            if dessin[i][j] == '1':
                #print(dessin[i][j],end="")
                print(u'\u25a0',end="")
            elif dessin[i][j] == '2':
                print(u'\u25ce',end="")
            else:
                print(u'\u25a1',end="")
#        print(end='",\n')
        print(end='\n')
    print()

# Fonction récursive (à terminer pour la gestion des bords puis couleurs à terme)
def colorier(t, pos_i, pos_j, taillePile):
    # Bien expliquer pourquoi la taille du problème diminue
    print(pos_i,pos_j, taillePile)
    if t[pos_i][pos_j]!="0":
        taillePile -= 1
        return
    else:
        t[pos_i][pos_j]="2"
        affiche(t)
        taillePile +=1 
        colorier(t, pos_i+1, pos_j,taillePile)
        colorier(t, pos_i-1, pos_j,taillePile)
        colorier(t, pos_i, pos_j+1,taillePile)
        colorier(t, pos_i, pos_j-1,taillePile)
  
def rotationIterative(dessin):
    return [''.join([dessin[i][len(dessin[0]) - j-1] for i in range(len(dessin))]) for j in range(len(dessin[0]))]


def dessin2px(dessin):
    return [list(dessin[i]) for i in range(len(dessin))]

affiche(rotationIterative(dessin_depart))
depart_tourner =[
"010100",
"101110",
"100101",
"100101",
"100001",
"100010",
"110010",
"001100",
]
# Ajouter une UI à terme avec clic souris (cf générateur image du jeu de la vie)

# Remplissage du tableau T (a terme une image)
Nb_lig=len(dessin_depart)
Nb_col=len(dessin_depart[0])
T=[["0" for i in range(Nb_col)] for i in range(Nb_lig)]
for i in range(Nb_lig):
    for j in range(Nb_col):
        T[i][j]=dessin_depart[i][j]

if __name__ == '__main__':

    affiche(dessin_depart)
    colorier(T,2,3,0)
#  affiche(T)

    


#pix[20,20] = value  # Set the RGBA Value of the image (tuple)