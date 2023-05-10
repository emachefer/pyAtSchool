import turtle
import random as rd
import time

WIDTH  = 600
HEIGHT = 800

SIZE = 100

PX = 0
PY = 0

TIC = 0

def gagne(noprint = False):
    x, y = turtle.pos()
    if int(x) == PX and int(y) == PY:
        toc = time.perf_counter()
        if noprint == False:
            print("Vous avez gagné en {:0.2f} secondes!".format(toc-TIC))
        turtle.clear()
        return True
    return False

gauche = lambda : turtle.left(90)
droite = lambda : turtle.right(90)

def avance():
    turtle.forward(SIZE)
    gagne()

def recule():
    turtle.backward(SIZE)
    gagne()

def start():
    screen = turtle.Screen()
    screen.setup(HEIGHT, WIDTH)

    xm = int(WIDTH/2 - SIZE)
    ym = int(HEIGHT/2 - SIZE)

    global PX, PY, TIC
    PX = rd.randrange(-xm, xm, SIZE)
    PY = rd.randrange(- ym, ym, SIZE)
    TIC = time.perf_counter()

    try:
        turtle.penup()
        turtle.goto(PX, PY)
        turtle.color("red")
        turtle.shape("circle")
        turtle.stamp()
        turtle.shape("arrow")
        turtle.color("black")
        turtle.home()
        turtle.pendown()
    except:
        print("Erreur inattendue, recommencer.")
    return PX, PY, TIC

if __name__ == "__main__":
    start()

    win = gagne()
    while(win == False):
        fname = input("Entrer le nom du fichier : ")

        with open(fname) as finput:
            for line in finput:
                exec(line)
                win = gagne(True)
                if win == True:
                    break
            else:
                continue
            break

