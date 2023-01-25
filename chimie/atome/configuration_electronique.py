#! /bin/python
"""Configuration électronique

Script permettant de déterminer la configuration électronique
d'un atome en fonction de son numéro atomique.

@author:  E. Machefer <evan.machefer@ac-dijon.fr>
@project: pyAtSchool  <https://github.com/emachefer/pyAtSchool>
@license: GPL-3.0
"""


# Nombre maximum d'électrons par sous couche
NB_MAX_E = {"1s": 2, "2s": 2, "2p": 6, "3s": 2, "3p": 6}

# Initialisation de la configuration de l'atome
configuration = {"1s":0, "2s":0, "2p":0, "3s":0, "3p":0}
val  = int(input("Entrer un nombre d'électrons (<18) : "))

nbEl = 0
if val >= 0 and val <= 18:
    nbEl = val
else:
    print("[ERROR] Le nombre d'électrons n'est pas cohérent (Z = {})".format(val))
    exit()

# Remplissage des couches électroniques
while nbEl > 0:
    for couche in NB_MAX_E:
        # couche = 1s, 2s, 2p, 3s ou 3p
        nbMax = NB_MAX_E[couche]
        nbElCouche = 0 # Nb d'électrons sur la sous couche actuelle

        # Si le nombre d'électrons restants est plus grand que le max, on garde le max
        if (nbEl > nbMax):
            nbElCouche = nbMax
        # sinon on met les électrons restants
        else:
            nbElCouche = nbEl

        configuration[couche] = nbElCouche
        # Ne pas oublier d'enlever les électrons déjà mis
        nbEl -= nbElCouche

# Pour l'affichage en fin de script
for couche in configuration:
    if (configuration[couche] != 0):
        print("{}^{}".format(couche, configuration[couche]), end=" ")
    else:
        break
print("")
