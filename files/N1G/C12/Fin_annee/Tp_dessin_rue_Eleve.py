import turtle
from random import randint, shuffle

def trait(x1,y1,x2,y2):
    '''
    Paramètres
        x1, y1 : coordonnées du début du trait
        x2, y2 : coordonnées de la fin du trait
    '''
    turtle.penup()
    turtle.goto(x1,y1)
    turtle.pendown()
    turtle.goto(x2,y2)
    


# --------------------------------
# -----Programme principal--------
# --------------------------------

if __name__ == "__main__":
    turtle.setup(800, 600)
    turtle.speed(0)
    turtle.hideturtle()

    y_sol = -200
    # Dessin du sol de la rue
    turtle.pensize(3)
    trait(-380, y_sol, 380, y_sol)
    
    turtle.mainloop()