import turtle
import random as rd
import time

import os


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


######### Début du programme #########
if __name__ == "__main__":
    fdir = os.path.dirname(__file__)
    start()

    win = gagne()
    while(win == False):
        fname = input("Entrer le nom du fichier : ")
        if fname == "":
            exit()

        fpath = fdir + "/" + fname
        with open(fpath) as finput:
            print("Openning : '{}'".format(fpath))
            for line in finput:
                exec(line)
                win = gagne(True)
                if win == True:
                    break
            else:
                continue
            break
