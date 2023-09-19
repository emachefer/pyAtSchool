"""Energie



@author  : E. Machefer <evan.machefer@ac-dijon.fr>
@project : pyAtSchool <https://github.com/emachefer/pyAtSchool>
@license : GPL-3.0
"""

import math

# Bibliographie :
# - Énergie d'ionisation : https://fr.wikipedia.org/wiki/Énergies_d'ionisation_des_éléments_(données)

# Constantes
π = math.pi
h  = 6.62607015e-34  # J·s
c  = 299792458       # m/s
e  = 1.602176634e-19 # C

#
J  = 1/e
EI = -13.59944       # eV

# Pour obtenir l'énergie (en eV) d'une longueur d'onde donnée en nm
ΔE = lambda λ : h*c/(λ*1e-9) * J


Balmer = [656.210, 480.074, 434.010, 410.120]
ΔEh = [ΔE(Balmer[i]) for i in range(len(Balmer))]

print("Énergies de la série de Balmer pour l'hydrogène :")
for i,λ in enumerate(Balmer):
    print("ΔE({:.3f} nm) = {:.2f} eV".format(λ, ΔEh[i]))


# ΔEₙₘ = Eₙ - Eₘ = -Eᵢ × (1/n² - 1/m²)
ΔEnm = lambda n, m: -EI*(1/n**2 - 1/m**2)
ε = 2e-2

done = [0 for i in range(len(Balmer))]
for n in range(1,10):
    for m in range(n+1, 10):
        ΔEth = ΔEnm(n,m)

        for i, ΔEexp in enumerate(ΔEh):
            η = math.fabs((ΔEexp-ΔEth)/ΔEth)
            if η < ε:
                print("====== {} nm ======".format(Balmer[i]))
                print("Transition : {} → {}".format(m, n))
                print("Energie : ΔE(exp) = {:.3f} eV\t| ΔE(th) = {:.3f} eV".format(ΔEexp, ΔEth))
                print("Écart relatif : η = {:.2e}".format(η))
                done[i] = 1

for i,d in enumerate(done):
    if d == 0:
        print("La raie λ = {} nm n'a pas été trouvée".format(Balmer[i]))
