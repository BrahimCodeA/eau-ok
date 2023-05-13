
import sys

def tri_selection(liste):
    n = len(liste)
    
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if liste[j] < liste[min_idx]:
                min_idx = j
        
        liste[i], liste[min_idx] = liste[min_idx], liste[i]
    
    return liste

# Vérification du nombre d'arguments
if len(sys.argv) < 2:
    print("error.")
    sys.exit(1)

# Récupération des nombres à trier à partir des arguments de la ligne de commande
nombres_a_trier = sys.argv[1:]

# Conversion des nombres en entiers
nombres = []
for nombre in nombres_a_trier:
    if not nombre.isdigit():
        print("error.")
        sys.exit(1)
    nombres.append(int(nombre))

# Appel de la fonction tri_selection pour trier la liste de nombres
nombres_tries = tri_selection(nombres)

# Affichage des nombres triés
for nombre in nombres_tries:
    print(nombre, end=" ")
