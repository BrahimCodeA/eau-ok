
import sys


# Récupération de l'argument
if len(sys.argv) != 2:
    print("erreur.")
    sys.exit(-1)

try:
    n = int(sys.argv[1])
except ValueError:
    print("-1.")
    sys.exit(-1)

if n <= 0:
    print("-1.")
    sys.exit(-1)

# Calcul de la suite de Fibonacci
premier_element = 0
deuxieme_element = 1
if n == 1:
    resultat = premier_element
else:
    for i in range(n - 1):
        premier_element, deuxieme_element = deuxieme_element, premier_element + deuxieme_element
    resultat = deuxieme_element

# Affichage du résultat
print(resultat)
