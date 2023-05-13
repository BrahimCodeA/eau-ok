
import sys

# Vérification du nombre d'arguments
if len(sys.argv) == 1:
    print("error")
    sys.exit(1)

# Affichage des arguments en ordre inverse
for i in range(len(sys.argv)-1, 0, -1):
    print(sys.argv[i])