
import sys

# Récupération des arguments
if len(sys.argv) != 3:
    print("erreur.")
    sys.exit(-1)

chaine = sys.argv[1]
sous_chaine = sys.argv[2]

# Vérification des arguments
if not isinstance(chaine, str) or not isinstance(sous_chaine, str):
    print("erreur.")
    sys.exit(-1)

# Recherche de la sous-chaîne
if sous_chaine in chaine:
    print("true")
else:
    print("false")
