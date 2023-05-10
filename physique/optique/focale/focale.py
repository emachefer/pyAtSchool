"""Focale

Script permettant de déterminer la distance focale d'une lentille selon différentes méthodes:
- Conjugaison
- Bessel

@author  : E. Machefer <evan.machefer@ac-dijon.fr>
@project : pyAtSchool <https://github.com/emachefer/pyAtSchool>
@license : GPL-3.0
"""

from matplotlib import pyplot as plt


def Bessel():
    D  = eval(input("D = "))
    x1 = eval(input("x1 = "))
    x2 = eval(input("x2 = "))
    d = x2 - x1
    f = (D**2 - d**2)/(4*D)
    return(f)


def conjugaison():
    OA  = eval(input("OA = "))
    OAp = eval(input("OA' = "))
    inverse = 1/OA - 1/OA
    return 1./inverse

def quitter():
    return True

def menu():
    try:
        f = eval(input("'Bessel', 'conjugaison' ou 'quitter' : ") + "()")
        if f !=  True:
            print(f"f' = {f} ; V = {1/f}")
        else:
            print("Bye!")
            exit()
    except Exception as err:
        print(f"[ERROR] {err}")

while(True):
    menu()
