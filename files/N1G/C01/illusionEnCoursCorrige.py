import turtle

greg = turtle.Turtle()
greg.shape('turtle')

cote = 100
angle = 90
nCarre = 10
nLigne = 10
xBas = -400
yHaut = 300

def decalage(x):
    if(x % 6 == 0): return 20
    elif(x % 6 == 1): return 20
    elif(x % 6 == 2): return 20
    else : return -20

greg.speed(0)
k = 0
# xpos = xBas
# while k < nLigne:
#     xpos = xpos + decalage(k)
#     # if(k % 6 == 0): xpos = xpos + 20
#     # elif(k % 6 == 1): xpos = xpos + 20
#     # elif(k % 6 == 2): xpos = xpos + 20
#     # elif(k % 6 == 3): xpos = xpos - 20
#     # elif(k % 6 == 4): xpos = xpos - 20
#     # elif(k % 6 == 5): xpos = xpos - 20
#     greg.penup()
#     greg.goto(xpos, yHaut - lon*k)
#     greg.pendown()
#     j = 0
#     while j < nCarre:

#         if j % 2 == 0:
#             greg.fillcolor('black')
#         else:
#             greg.fillcolor('white')

#         greg.begin_fill()
#         i = 0
#         while i < 4:
#             i = i + 1
#             greg.forward(lon)
#             greg.left(angle)
#         greg.end_fill()

#         greg.forward(lon)
#         j = j + 1

#     k = k + 1

def choixCouleur(nombre):
    if nombre % 2 == 0:
        couleur = 'black'
    else:
        couleur = 'white'
    return couleur   

def carre(x):
    for _ in range(4):
        greg.forward(x)
        greg.left(90)

def carreColore(x, nombre):
    couleur = choixCouleur(nombre)
    greg.begin_fill()
    greg.fillcolor(couleur)
    carre(x)
    greg.end_fill()

def ligneDeCarre(posx, posy, x, n):
    greg.pu()
    greg.goto(posx, posy)
    greg.pd()
    for j in range(n):
        carreColore(x, j)
        greg.forward(x)


# #carreColore(100,2)
# #carreColore(50,1)
# ligneDeCarre(-400,200,longueur,nCarre)
# ligneDeCarre(-400,100,longueur,nCarre)
# ligneDeCarre(-400,0,longueur,nCarre)
# ligneDeCarre(-400,-100,longueur,nCarre)

def damier(xpos, ypos, x, n):
    for k in range(n):
        xpos = xpos + decalage(k)
        ligneDeCarre(xpos, ypos-x*k, x, nLigne)

turtle.tracer(0,0)
damier(xBas, yHaut, cote, nLigne)
turtle.update()

def maFonction(x):
    variableInterne = 2*x + 4
    return variableInterne

res = maFonction(0)  # res vaut 2*0 + 4

turtle.exitonclick()