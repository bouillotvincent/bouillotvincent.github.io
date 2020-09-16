import turtle

nombreCote = 10
longueur = 100
maxTraits = 50
largeur = 8
angle = 360/nombreCote

fred = turtle.Turtle()
fred.goto(0,0)
fred.speed(0)
vert = 1
fred.color(0, 1, 0)
fred.width(largeur)
nombreTraits = 0   # initialisation
while nombreTraits < maxTraits:
    nombreTraits = nombreTraits + 1    
    if longueur >= 0:
        fred.forward(longueur)
        fred.right(angle)
        longueur = longueur-2
        vert = vert*0.95
        fred.color(0, vert, 0)
    if nombreTraits % 5 == 0:
        largeur = largeur*0.75
        fred.width(largeur)



turtle.exitonclick()