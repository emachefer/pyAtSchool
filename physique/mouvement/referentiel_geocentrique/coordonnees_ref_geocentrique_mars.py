#! /bin/python3
"""Coordonnées géocentriques

Script simulant l'orbite de la planète Mars dans le référentiel
géocentrique.

Dans cette simuation, on considère une orbite circulaire autour du
Soleil.

@author:  E. Machefer <evan.machefer@ac-dijon.fr>
@project: pyAtSchool  <https://github.com/emachefer/pyAtSchool>
@license: GPL-3.0
"""

from matplotlib import pyplot as plt
from matplotlib import animation
from math import pi
from math import cos
from math import sin

# Distances par rapport au Soleil
ua = 1.50e8 #km
Rt = 1.00 * ua
Rm = 1.52 * ua

# Période de révolution autour du Soleil
an = 365.26 # j
Tt = 1.00 * an
Tm = 1.88 * an

# Vitesses angulaires : constantes dans le cas d'une orbite circulaire
Wt = 2 * pi / Tt
Wm = 2 * pi / Tm

# Pouvant être modifié
nb_annees = int(input("Entrer un nombre d'année a étudier : "))
step = 0.01
duree = int(nb_annees/step)

# Angles formés dans les coordonnées polaires
aT = [Wt * t * an * step % (2*pi) for t in range(duree)]
aM = [Wm * t * an * step % (2*pi) for t in range(duree)]

# Coordonnées cartésiennes
## Terre
xT = [Rt * cos(aT[i]) for i in range(len(aT))]
yT = [Rt * sin(aT[i]) for i in range(len(aT))]
## Mars
xM = [Rm * cos(aM[i]) for i in range(len(aM))]
yM = [Rm * sin(aM[i]) for i in range(len(aM))]


fig, ax = plt.subplots()
plt.plot([0], [0], 'bo')

## Coordonnées géocentrique de Mars
if (str(input("Faire l'animation ? [O/N] ")).upper() == "N"):
    xMg = [xM[i] - xT[i] for i in range(len(aT))]
    yMg = [yM[i] - yT[i] for i in range(len(aT))]
    plt.plot(xMg, yMg, 'r')
    ax.title(f"Trajectoire de Mars dans le référentiel géocentrique ({nb_annees} ans)")
else:
    xMg = []
    yMg = []
    def animate(i):
        ans = int(i * step)
        xMg.append(xM[i] - xT[i])
        yMg.append(yM[i] - yT[i])
        plt.plot(xMg, yMg, 'r')
        ax.set_title(f"Trajectoire de Mars dans le référentiel géocentrique ({ans} ans)")
    animation = animation.FuncAnimation(fig, animate, interval=1)


ax.set_aspect('equal')
plt.show()


# Pour déterminer la période de révolution (retour à la position d'origine)
T = []
for i in range(1, len(xMg)): # On ne compare pas le premier point avec lui même
    if abs(xMg[i]-xMg[0]) < 0.01 and abs(yMg[i] - yMg[0]) < 0.01:
        ans = int(i*step)
        T.append(ans)
        print(f"{ans} ans :\n\t x0 = {xMg[0]} , x{ans} = {xMg[i]}\n\t y0 = {yMg[0]}, y{ans} = {yMg[i]}")
else:
    print(f"Il y a {len(T)} révolutions complètes en {nb_annees} ans.")
