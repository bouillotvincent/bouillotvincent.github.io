import turtle

nombreCote = 8
longueur = 100
angle = 360/nombreCote
maxTraits = 30

fred = turtle.Turtle()
fred.goto(0,0)
nombreTraits = 0   # initialisation
while nombreTraits < 8:
    fred.forward(longueur)
    fred.right(angle)
    nombreTraits = nombreTraits + 1

turtle.exitonclick()