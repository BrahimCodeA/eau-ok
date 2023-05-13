
import sys

def ne_contient_que_chiffres(chaine):
    return chaine.isdigit()  # Vérifie si la chaîne ne contient que des chiffres

# Vérifie le nombre d'arguments passés en ligne de commande
if len(sys.argv) != 2:
    print("error")
    sys.exit()

chaine = sys.argv[1]  # Récupère la chaîne de caractères passée en argument
try:
    if ne_contient_que_chiffres(chaine):
        print("true")
    else:
        print("false")
except AttributeError:
    print("error")