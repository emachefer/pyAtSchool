#!/bin/python3
"""Simulation désintégration

Ce script permet de simuler les désintégrations nucléaires.

@author  : E. Machefer <evan.machefer@ac-dijon.fr>
@project : pyAtSchool <https://github.com/emachefer/pyAtSchool>
@license : GPL-3.0
"""
from matplotlib import pyplot as plt
from math import exp
import random


# Initialisation des valeurs
try:
    N0    = float(input("Nombre initial de noyaux : "))
    proba = float(input("Probabilite de desintegration (en pourcentage) : "))/100.
    if (proba > 1 or proba < 0):
        raise()
    pas   = int(input("Nombre de lancer par essais ({}/{}) : ".format(N0, N0/10)))
except:
    print("[ERREUR] Les valeurs renseignées sont invalides !")
    exit()

# Un noyau atomique a une probabilité de désintégration
# plus cette probabilité est élevée, plus vite la
# population diminuera.
isDesintegre = lambda : random.random() < proba

noyauxRestants = int(N0)
listeNoyaux = [N0]

def desintegration():
    nb = noyauxRestants
    for n in range(nb):
        if (isDesintegre() == True):
            nb -= 1
    return nb

temps = [0]
nombreDeLance = 0

plt.ion()
plt.figure()
plt.show()
plt.ylim(0, N0+1)
while(noyauxRestants > 0):
    for lancer in range (pas):
        nombreDeLance += 1
        temps.append(nombreDeLance)
        noyauxRestants = desintegration()
        listeNoyaux.append(noyauxRestants)
    plt.title("{} noyaux restants".format(noyauxRestants))
    plt.plot(temps, listeNoyaux, 'b')
    plt.pause(0.1)


f = [N0*exp(-temps[i]*proba) for i in range(len(temps))]
plt.plot(temps,f,'r', label="Modélisation")
plt.legend()

plt.title("Cliquer pour quitter, temps écoulé {}".format(temps[-1]))
plt.waitforbuttonpress()
