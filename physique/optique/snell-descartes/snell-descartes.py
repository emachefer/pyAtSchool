#! /bin/python3
import time
# import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox
from math import cos, sin, asin, atan, fabs, pi

to_deg = lambda x : x * 180./pi
to_rad = lambda x : x * pi / 180.

def tellme(s):
    print(s)
    plt.title(s, fontsize=16)
    plt.draw()


n1 = float(input("n1 = "))
n2 = float(input("n2 = "))

# Init figure
fig = plt.figure()
ax  = fig.add_subplot(111, facecolor='#FFFFFF')

plt.xlim(-1, 1)
plt.ylim(-1, 1)

# Modifie la couleur pour la partie basse
plt.fill_between([-1,1], -1, color="#03A9EE")
plt.arrow(0,-1,0,2, color="gray", linestyle="dashed")

tellme('Réfraction de la lumière (cliquer pour commencer)')

plt.waitforbuttonpress()
l = 5

while True:
    tellme("Sélectionner la position de la source")
    # Récupère les coordonnées de la source
    x, y = plt.ginput(1, timeout=-1)[0]
    tellme("Source à ({}, {})".format(x,y))

    if y < 0:
        tellme("Pas encore pris en compte")
        continue

    # Angles incident et réfracté
    θi = atan(x/fabs(y))
    θr = asin(n1*sin(θi)/n2)

    tellme('θi = {:.2f} ; θr = {:.2f}'.format(to_deg(θi), to_deg(θr)))

    ri = plt.arrow(0, 0, l*x, l*y, color='r')
    rr = plt.arrow(0, 0, -l*sin(θr), -l*cos(θr), color='g')

    if plt.waitforbuttonpress():
        break

    # Get rid of fill
    ri.remove()
    rr.remove()

tellme('All Done!')
plt.show()
