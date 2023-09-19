"""Propagation

Ce script modélise la propagation d'une onde unidimensionnelle.

@author  : E. Machefer <evan.machefer@ac-dijon.fr>
@project : pyAtSchool <https://github.com/emachefer/pyAtSchoool>
@license : GPL-3.0
"""

from math import sin, pi, exp
from matplotlib import pyplot, animation

π = pi

Xmax = 10.0
Tmax = 10.0
A = 2.0

def entrerValeur(nom, vMax, vMin = 0):
    """ Fonction permettant de récupérer une valeur et tester sa validité.
    """
    val = vMin - 1
    while val > vMax or val < vMin:
        val = float(input("Entrer la valeur de {} (∈ [{};{}]): ".format(nom, vMin, vMax)))
    return val

T = entrerValeur("période (s)", Tmax)
v = entrerValeur("vitesse (m·s⁻¹)", 10*Xmax/Tmax)


NbEchantillons = 1000
Δt = Tmax/NbEchantillons
Δx = Xmax/NbEchantillons

fig = pyplot.figure()
ax = pyplot.axes(xlim=(0,Xmax), ylim=(-1.3*A,1.3*A))


X = [i*Δx for i in range(NbEchantillons)]
temps = [i*Δt for i in range(NbEchantillons)]
ω = 2*π /T
k = ω/v
α = 0.1
z = lambda x, t: A*exp(-α*x) * sin(ω*t - k*x)

courbes = [[z(x,t) for x in X] for t in temps]

courbe, = ax.plot(X, courbes[0])

def increment(i):
    courbe.set_ydata(courbes[i])
    # Retrace fill_between
    fb = pyplot.fill_between(X, courbes[i], -10*A, color=(0.1, 0.2, 0.8, 0.25))
    return courbe, fb

ax.set_xlabel("X")
ax.set_ylabel("Y")

xA = Xmax/3
dx = v*T
pyplot.axvspan(xA, xA+dx, color='r', alpha=0.5, lw=0)
pyplot.arrow(xA,A, dx,0, color='r', label="λ", length_includes_head = True)

pyplot.arrow(0,0, Xmax, 0, linestyle='dashed', label="Niveau moyen")

line_ani = animation.FuncAnimation(fig, increment, 100, interval=50, blit=True)

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
