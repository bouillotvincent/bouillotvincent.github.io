import turtle

nombreCote = 6
longueur = 100
angle = 360/nombreCote
maxTraits = 30
# largeur = 8

""" Exercice 10 """
fred = turtle.Turtle()	
fred.goto(0, 0)
nTraits = 0
while nTraits < maxTraits:
    if longueur >= 0:
        fred.forward(longueur)
        fred.right(angle)
        longueur = longueur - 8
        print(longueur)
        nTraits = nTraits + 1
    else:
        nTraits = nTraits + 1

turtle.exitonclick()

# fred = turtle.Turtle()
# fred.goto(0,0)
# fred.speed(0)
# nombreTraits = 0   # initialisation
# while nombreTraits < nombreCote:
#     fred.forward(longueur)
#     fred.right(angle)
#     nombreTraits = nombreTraits + 1


# fred = turtle.Turtle()
# fred.goto(0,0)
# fred.speed(0)
# rouge = 1
# fred.color(0,1, 0)
# fred.width(largeur)
# nombreTraits = 0   # initialisation
# while nombreTraits < maxTraits:
#     nombreTraits = nombreTraits + 1    
#     if longueur >= 0:
#         fred.forward(longueur)
#         fred.right(angle)
#         longueur = longueur-3
#         rouge = rouge*0.95
#         fred.color(0, rouge,0)
#     if nombreTraits % 5 == 0:
#         largeur = largeur*0.75
#         fred.width(largeur)



# longueur = 1
# largeur = 8
# fred = turtle.Turtle() 
#turtle.tracer(0,0)
# fred.pu()
# fred.goto(0,0)
# fred.pd()
# fred.speed(0)
# rouge = 1
# fred.color(0, 1, 0)
# fred.width(largeur)
# nombreTraits = 0   # initialisation
# while nombreTraits < maxTraits:
#     if longueur >= 0:
#         fred.forward(longueur)
#         fred.left(angle)
#         longueur = longueur+0.3
#         rouge = rouge*0.95
#         fred.color(0, 1-rouge,0)
#     nombreTraits = nombreTraits + 1    
#     #if nombreTraits % 5 == 0:
#         #largeur = largeur*1.10
#         #fred.width(largeur)