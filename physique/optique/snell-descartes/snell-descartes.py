#! /bin/python3
"""Refraction de la lumière

Ce script permet de tracer les rayons lumineux incident, réfléchi et réfracté
selon l'indice de réfraction de deux milieux.

@author: E. Machefer <evan.machefer@ac-dijon.fr>
@project: pyAtSchool  <https://github.com/emachefer/pyAtSchool>
@license: GPL-3.0
"""

import matplotlib.pyplot as plt
from math import cos, sin, asin, atan, fabs, pi

to_deg = lambda x : x * 180./pi
to_rad = lambda x : x * pi / 180.

def tellme(s):
    print(s)
    plt.title(s, fontsize=16)
    plt.draw()

l = 5 # longueur du faisceau
n1 = float(input("n1 = "))
n2 = float(input("n2 = "))

# Init figure
fig = plt.figure()
ax  = fig.add_subplot(111, facecolor='#FFFFFF')

plt.xlim(-1, 1)
plt.ylim(-1, 1)

# Modifie la couleur pour la partie basse
plt.fill_between([-1,1], -1, color="#03A9EE")
# Trace la normale
plt.arrow(0,-1,0,2, color="gray", linestyle="dashed")

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

    ri = plt.arrow(0, 0, l*x, l*y, color='r', label="Rayon incident")
    rr = plt.arrow(0, 0, -l*sin(θr), -l*cos(θr), color='g', label="Rayon réfracté")
    rx = plt.arrow(0,0, -l*x, l*y, color='b', label="Rayon réfléchi")

    ax.legend()

    if plt.waitforbuttonpress():
        break

    # Get rid of fill
    ri.remove()
    rr.remove()
    rx.remove()

tellme("Appuyer sur 'q' pour quitter")
plt.show()
