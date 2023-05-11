"""Lentilles

Script permettant de tracer l'image d'un objet en fonction de la distance objet-lentille et de la distance focale.

@author  : E. Machefer <evan.machefer@ac-dijon.fr>
@project : pyAtSchool <https://github.com/emachefer/pyAtSchool>
@license : GPL-3.0
"""

from matplotlib import pyplot as plt

def conjugaison(xA, f):
    """
    Permet de déterminer la distance de l'image avec la relation de conjugaison :
    1/xA' = 1/f' + 1/xA
    """
    inverse = 1/f + 1/xA
    return 1/inverse


def image(xA, xAp, AB):
    """
    Permet de déterminer le sens et la taille de l'image par la relation de grandissement:
    γ = A'B'/AB = OA'/OA
    """
    γ = xAp / xA
    return AB * γ


def init():
    unit = input("Entrer unité : ")
    f = float(input("Entrer la valeur de la distance focale. f = "))
    AB = float(input("Entrer la taille de l'objet. AB = "))
    OA = float(input("Entrer la distance objet-lentille. OA = "))
    OA = OA if OA < 0 else -OA # OA doit être négatif

    return f, AB, OA, unit

f, AB, OA, unit = init()

def traceRayon(x1, y1, x2, y2, x3='NaN', y3='NaN', couleur='r'):
    """traceRayon

    Permet de tracer un rayon lumineux
    @param:
    - xi, yi : coordonnées du point i
    """
    ddx = (x2 - x1)/2
    ddy = (y2 - y1)/2
    plt.arrow(x1, y1, ddx, ddy, color=couleur, width=largeur, head_width=0.1*hl, length_includes_head= True)
    plt.arrow(x1+ddx, y1+ddy, ddx, ddy, width=largeur, color=couleur)
    if x3 != 'NaN' and y3 != 'NaN':
        ddx2 = (x3 - x2)/2
        ddy2 = (y3 - y2)/2
        plt.arrow(x2, y2, ddx2, ddy2, width=largeur, color=couleur, head_width=0.1*hl, length_includes_head= True)
        plt.arrow(x2+ddx2, y2+ddy2, ddx2, ddy2, width=largeur, color=couleur)


def dessine(OA, AB, OAp, ABp):
    hl = 1.2 * AB if abs(AB) > abs(ABp) else 1.2 * ABp # Hauteur de la lentille
    fig = plt.figure()

    largeur = 0.001*hl

    plt.arrow(0, hl, 0, -2*hl) # Lentille

    plt.arrow(OA,0,0,AB, width=2*largeur)    # Objet
    plt.text(OA, 0, "A")
    plt.text(OA, AB, "B")
    plt.arrow(OAp,0, 0,ABp, width=2*largeur) # Image
    plt.text(OAp, 0, "A'")
    plt.text(OAp, ABp, "B'")

    plt.arrow(1.2*OA,0, 1.2*(OAp-OA),0, width=2*largeur,linestyle='dashed') # Axe optique


    traceRayon(OA, AB, OAp, ABp)
    traceRayon(OA, AB, 0, AB, OAp, ABp, couleur='b')
    traceRayon(OA, AB, 0, ABp, OAp, ABp, couleur='g')


    plt.title("OA' = {:.2f} cm; A'B' = {:.2f} {}".format(OAp, ABp, unit))

    plt.xlabel("Distance (en {})".format(unit))
    plt.ylabel("Taille (en {})".format(unit))

    plt.show()


OAp = conjugaison(OA,f)
ABp = image(OA, OAp, AB)

print("OA' = {:.2f} cm; A'B' = {:.2f} {}".format(OAp, ABp, unit))
if input("Tracer [Y/N] ? ").upper() == 'Y':
    dessine(OA, AB, OAp, ABp)
