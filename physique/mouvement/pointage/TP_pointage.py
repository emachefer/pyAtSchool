##################################################
########## NE PAS TOUCHER (voir ligne 40) ########
##################################################
from matplotlib import pyplot as plt

def tracer(x, y, titre = "Titre du graphique"):
   """
   Fonction à appeler pour tracer le graphique.
   Exemple pour tracer y = f(x) :
   tracer(x, y)
   """
   plt.plot(x, y, 'bo')
   plt.title(titre)
   plt.ylabel("Altitude y (en m)")
   plt.xlabel("Temps t (en s)")


def vitesse(x, y):
   """
   Fonction permettant de calculer les vitesses et de les tracer
   sur le graphique.
   Exemple d'appel :
   vitesse(x,y)
   """
   vy = []
   vx = []
   for i in range(len(y) - 1):
      ### TODO : Ajouter la formule correspondante
      vy_i = 0
      ### TODO : Ajouter la formule correspondante
      vx_i = 0
      vy.append(vy_i)
      vx.append(vx_i)

   for i in range (len(vy)):
      plt.arrow(x[i], y[i], vx[i]/20., vy[i]/20., length_includes_head=True, head_width = 0.05)

##################################################
############# TRAVAIL A FAIRE ICI ################
##################################################
#### Pour une aide sur une fonction s'appelant FONCTION, dans la console écrire : help(FONCTION)
### TODO : coller le résultat du pointage t, x et y

### TODO : Lire les fonctions définies au dessus
### TODO : appeler la fonction pour tracer y en fonction de x

### TODO : appeler la fonction pour tracer les vitesses

### TODO : modifier la fonction vitesse au niveau des TODO (lignes 28 et 30)
########### LAISSER EN FIN DE SCRIPT ################
plt.show()
