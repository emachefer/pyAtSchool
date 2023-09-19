doc="""COURBE CARACTÉRISTIQUE


@author  : E. Machefer <evan.machefer@ac-dijon.fr>
@project : pyAtSchool <https://github.com/emachefer/pyAtSchool>
@license : GPL-3.0
"""
print(doc)

from matplotlib import pyplot as plt

moyenne = lambda X: sum(X)/len(X)
def stdev(X):
    Xm = moyenne(X)
    s = [(X[i] - Xm)**2 for i in range(len(X))]
    return (sum(s))**0.5

def affine(X, Y):
    """Détermine un équation du type Y = a * X + b
    retourne les paramètres a et b.

    a = moyenne(Δy)/moyenne(Δx)
    b = ((∑ y) - a(∑ x))/len(x)
    """
    ΔY = [Y[n] - Y[n-1] for n in range(1,len(Y))]
    ΔX = [X[n] - X[n-1] for n in range(1,len(X))]
    A = [ΔY[n]/ΔX[n] for n in range(len(ΔX))]
    a = moyenne(A)
    σa = stdev(A)

    b = (sum(Y) - a*sum(X))/len(X)
    return a, b, σa


def R2(Yexp, Yth):
    num = [(Yexp[n]-Yth[n])**2 for n in range(len(Yexp))]
    den = [(Yexp[n]-moyenne(Yexp))**2 for n in range(len(Yexp))]
    return 1 - sum(num)/sum(den)

X = {"nom": "", "val":[]}
Y = {"nom": "", "val":[]}

def getValeurs(V):
    nom = input("Nom de la variable : ")
    V["nom"] = nom
    while (val:=input("Entrer valeur : ")) != "":
        V["val"].append(float(val))

if __name__ == "__main__":
    print("Valeurs des X :")
    getValeurs(X)
    print("Valeurs des Y :")
    getValeurs(Y)
    print(X)
    print(Y)
    if len(X["val"]) != len(Y["val"]):
        exit("X et Y n'ont pas la même taille !")

    Yth = []
    print("Calcul de la régression linéaire...")
    a, b, σa = affine(X["val"],Y["val"])
    Yth = [a * X["val"][n] + b for n in range(len(X["val"]))]

    r2 = R2(Y["val"], Yth)
    print("{Y} = {a:.2f} × {X} + {b:.2f}\t σ = {stdev:.2f}\t R2 = {R2:.2f} %".format(a=a, b=b, R2=r2*100, Y=Y["nom"], X=X["nom"], stdev=σa))

    plt.plot(X["val"],Y["val"], 'bo')
    plt.plot(X["val"],Yth, 'r-')
    plt.xlabel(X["nom"])
    plt.ylabel(Y["nom"])

    plt.show()
