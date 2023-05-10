"""Propagation

Ce script modélise la propagation d'une onde unidimensionnelle.

@author  : E. Machefer <evan.machefer@ac-dijon.fr>
@project : pyAtSchool <https://github.com/emachefer/pyAtSchoool>
@license : GPL-3.0
"""

from math import sin, pi
from matplotlib import pyplot, animation

π = pi

Xmax = 10.0
Tmax = 10.0
A = 2.0


NbEchantillons = 100
Δt = Tmax/NbEchantillons
Δx = Xmax/NbEchantillons

fig = pyplot.figure()
ax = pyplot.axes(xlim=(0,Xmax), ylim=(-1.3*A,1.3*A))


X = [i*Δx for i in range(NbEchantillons)]
temps = [i*Δt for i in range(NbEchantillons)]

def entrerValeur(nom, vMax, vMin = 0):
    val = vMin - 1
    while val > vMax or val < vMin:
        val = float(input("Entrer la valeur de {} : ".format(nom)))
    return val

T = entrerValeur("période", Tmax)
v = entrerValeur("vitesse", Xmax/Tmax)

courbes = [[A * sin(2*π/T * (t-x/v)) for x in X] for t in temps]

courbe, = ax.plot(X, courbes[0])

def increment(i):
    courbe.set_ydata(courbes[i])
    return courbe,

ax.set_xlabel("X")
ax.set_ylabel("Y")

xA = Xmax/3
dx = v*T
pyplot.axvspan(xA, xA+dx, color='r', alpha=0.5, lw=0)
pyplot.arrow(xA,A, dx,0, color='r', label="λ")

line_ani = animation.FuncAnimation(fig, increment, 100, interval=50, blit=False)

onpause = False
def onclick(event):
    global onpause
    if onpause:
        line_ani.resume()
    else:
        line_ani.pause()
    onpause = not onpause

fig.canvas.mpl_connect('button_press_event', onclick)
pyplot.legend()
pyplot.show()
