
import sys

def afficher_valeurs_entre(minimum, maximum):
    if minimum >= maximum:
        return None  # Si le minimum est supérieur ou égal au maximum, retourne None
    valeurs = range(minimum, maximum)  # Génère une séquence de nombres entre le minimum (inclus) et le maximum (exclus)
    return ' '.join(str(valeur) for valeur in valeurs)  # Convertit les valeurs en chaînes de caractères et les réunit en une seule chaîne

# Vérifie le nombre d'arguments passés en ligne de commande
if len(sys.argv) != 3:
    print("erreur")
    sys.exit()

try:
    minimum = min(int(sys.argv[1]), int(sys.argv[2]))  # Convertit les deux arguments en entiers et prend le minimum des deux
    maximum = max(int(sys.argv[1]), int(sys.argv[2]))  # Convertit les deux arguments en entiers et prend le maximum des deux
    result = afficher_valeurs_entre(minimum, maximum)  # Appelle la fonction pour afficher les valeurs entre le minimum et le maximum
    if result is not None:
        print(result)
    else:
        print("erreur")
except ValueError:
    print("erreur")
