
import sys

# Vérification du nombre d'arguments
if len(sys.argv) < 2:
    print("error.")
    sys.exit(1)

# Récupération des éléments à trier à partir des arguments de la ligne de commande
elements_a_trier = sys.argv[1:]

# Tri des éléments par ordre ASCII
elements_tries = sorted(elements_a_trier)

# Affichage des éléments triés
for element in elements_tries:
    print(element, end=" ")