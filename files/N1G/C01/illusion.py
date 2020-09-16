import turtle

greg = turtle.Turtle()
greg.shape('turtle')

lon = 80
angle = 90
nCarre = 10
nLigne = 10
xBas = -400
yHaut = 300

greg.speed(0)
k = 0
xpos = xBas
while k < nLigne:
    greg.penup()
    if(k % 6 == 0): xpos = xpos + 20
    elif(k % 6 == 1): xpos = xpos + 20
    elif(k % 6 == 2): xpos = xpos + 20
    elif(k % 6 == 3): xpos = xpos - 20
    elif(k % 6 == 4): xpos = xpos - 20
    elif(k % 6 == 5): xpos = xpos - 20
    greg.goto(xpos, yHaut - lon*k)
    greg.pendown()
    j = 0
    while j < nCarre:

        if j % 2 == 0:
            greg.fillcolor('black')
        else:
            greg.fillcolor('white')

        greg.begin_fill()
        i = 0
        while i < 4:
            i = i + 1
            greg.forward(lon)
            greg.left(angle)
        greg.end_fill()

        greg.forward(lon)
        j = j + 1

    k = k + 1


turtle.exitonclick()