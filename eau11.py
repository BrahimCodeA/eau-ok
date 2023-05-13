

import sys

# Vérifier le nombre d'arguments
if len(sys.argv) < 3:
    print("Error.")
    sys.exit(1)

# Convertir les arguments en liste de nombres
try:
    nombres = [int(arg) for arg in sys.argv[1:]]
except ValueError:
    print("Error.")
    sys.exit(1)

# Vérifier la longueur de la liste de nombres
if len(nombres) < 2:
    print("Error.")
    sys.exit(1)

# Calculer la différence minimum absolue
diff_min_abs = None

for i in range(len(nombres)):
    for j in range(i+1, len(nombres)):
        diff = abs(nombres[i] - nombres[j])
        if diff_min_abs is None or diff < diff_min_abs:
            diff_min_abs = diff

# Afficher le résultat
print(diff_min_abs)