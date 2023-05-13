
import sys

# Vérifie le nombre d'arguments passés en ligne de commande
if len(sys.argv) < 3:
    print("error")
    sys.exit()

# Récupère le tableau (tous les arguments sauf le dernier)
tableau = sys.argv[1:-1]

# Récupère l'élément recherché (le dernier argument)
element_recherche = sys.argv[-1]

# Recherche l'indice de l'élément dans le tableau
if element_recherche in tableau:
    index = tableau.index(element_recherche)
    print(index)
else:
    print(-1)