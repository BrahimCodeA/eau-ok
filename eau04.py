
import sys

# Récupération de l'argument
if len(sys.argv) != 2:
    print("-1")
    sys.exit(-1)

try:
    n = int(sys.argv[1])
except ValueError:
    print("-1.")
    sys.exit(-1)

if n < 0:
    print("-1.")
    sys.exit(-1)

# Détermination du premier nombre premier supérieur à n
def est_premier(x):
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

nombre_premier = n + 1
while not est_premier(nombre_premier):
    nombre_premier += 1

# Affichage du résultat
print(nombre_premier)
