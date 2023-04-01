#!/bin/python3
"""
This script compute the limited reactant and graph the evolution
of the quantity of matter.

Copyright (C) 2022  Evan MACHEFER (evan.machefer@ac-dijon.fr)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

# Dans ce script, j'utilise surtout des 'dict' pour avoir quelque
# chose du type :
# {"reactif_1" : {"coef": a_1, "n": n_1}, "reactif_2": {"coef": a_2, "n": n_2}}
# cela permet de faire des boucles 'for' sur
# les noms des réactifs et des produits

print("======= REACTIF LIMITANT ET COURBE D'AVANCEMENT =========")
print("Importation des librairies, veuillez patienter...")
from  matplotlib import pyplot as plt

def get_reaction():
    """
    Permet d'obtenir les réactifs et les produits d'une réaction du type :
    a*A + b*B = c*C + d*D
    """
    # TODO : vérifier l'intégrité de la réaction
    reaction = input("Entrer la réaction (du type a*A + b*B = c*C + d*D): ")
    return reaction

def parse_reaction(reaction:str):
    """
    Cette fonction parse la chaine de charactères mise par l'utilisateur
    """
    # exemple: reactifs = {"H2": {"coef": 2, "n0": 1.0}, "O2": {"coef": 1, "n0": 2.0}}, produits = {"H2O": {"coef": 2}}
    reactifs = {}
    produits = {}
    # pour séparer la réaction en une partie réactifs et une autre produits
    gauche, droite = reaction.split('=')
    # Boucle sur les réactifs
    for reactif in gauche.split('+'):
        # Si pas de coefficient, l'exécution échoue et peut terminer
        # le programme sans cette vérification
        try :
            # FIXME: utiliser plutôt 'x' ?
            a, A = reactif.split('*')
        except:
            A = reactif
            a = 1
        reactifs[A] = {}
        reactifs[A]["coef"] = int(a)
    # Boucle sur les produits de la réaction
    for pdt in droite.split('+'):
        # Idem qu'au dessus
        try:
            # FIXME: utiliser plutôt 'x' ?
            a, A = pdt.split('*')
        except:
            A = pdt
            a = 1
        produits[A] = {}
        produits[A]["coef"] = int(a)
        produits[A]["n0"] = 0
    return reactifs, produits

def get_n_reactifs(reactifs):
    """
    Permet d'obtenir les quantité de matière initiale des réactifs.
    Il est possible d'utiliser les formules 'c*V' ou 't*V/M'
    """
    for reactif in reactifs:
        val = input("Entrer la quantité de matière de '{}' (en mol): ".format(reactif))
        n = eval(val) # ligne permettant l'évaluation d'un calcul
        reactifs[reactif]["n0"] = n


def get_limitants(reactifs):
    """
    Fonction pour déterminer l'avancement maximal de la réaction et les réactifs limitants.
    """
    x_max_reactifs = {}
    # Cette boucle permet de déterminer quels seraient les avancements
    # max de chaque réactif
    for reactif in reactifs:
        x_max_reactifs[reactif] = reactifs[reactif]["n0"] / reactifs[reactif]["coef"]
    x_max = min(x_max_reactifs.values())
    # Renvoie xmax et la liste des réactifs limitants
    return x_max, [key for key in x_max_reactifs if x_max_reactifs[key] == x_max]

def show_plots(n):
    # Plot les quantités de matière selon l'avancement
    for elem in n:
        plt.plot(x, n[elem], label="$n({})$".format(elem))

    # L'utilisation de ${reaction}$ permet d'afficher
    # quelque chose en indice
    plt.title("Courbes d'avancement de la réaction :\n${}$".format(reaction))
    plt.xlabel("Avancement (en mol)")
    plt.ylabel("Quantité de matière (en mol)")
    plt.legend()
    plt.show()



########## MAIN ##########
# On récupère les informations de l'utilisateur
reaction = get_reaction()
reactifs, produits = parse_reaction(reaction)
get_n_reactifs(reactifs)


x_max, limitants = get_limitants(reactifs)
print("L'avancement maximal est : {:.2f} mol".format(x_max))
print("Les réactifs limitants sont : {}".format(limitants))

step = x_max/10.0
# On défini un axe comportant les 'x'
# Plutôt que : x = np.arange(0, x_max + step, step)  ### (évite d'importer numpy)
x = [x*step for x in range(11)]# valeurs entre 0 et 1.1 * xmax (courbe plus lisible)
n = {}
for reactif in reactifs:
    n0 = reactifs[reactif]["n0"]
    a = reactifs[reactif]["coef"]
    # Plutôt que : n_A = - a * x + n_A ### (évite d'importer numpy)
    n_A = [n0 - a * x * step for x in range(11)]
    n[reactif] = n_A

for produit in produits:
    # Plutôt que : n_A = a * x ### (évite d'importer numpy)
    a = produits[produit]["coef"]
    n_A = [a * x * step for x in range(11)]
    n[produit] = n_A

line = (len("Réaction |") + len(reaction)) * '-'
newline = lambda : print("\n{}".format(line))
print_line = lambda s1, s2 : print("{} | {}".format(s1, s2), end=" | ")

print_line("Réaction", reaction)
# print("Réaction | {}".format(reaction), end=" ")
newline()
print("x = 0    | ", end= " ") # print sans saut à la ligne
for elem in n:
    print("{} |".format(n[elem][0]), end = " ")
newline()
print("x = xf   | ", end=" ")
for elem in n:
    print("{} |".format(n[elem][10]), end = " ")
newline()
show_plots(n)
