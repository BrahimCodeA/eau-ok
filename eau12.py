
import sys

def tri_bulle(liste):
    n = len(liste)
    
    for i in range(n):
        for j in range(0, n-i-1):
            if liste[j] > liste[j+1]:
                liste[j], liste[j+1] = liste[j+1], liste[j]
    
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
        print("error")
        sys.exit(1)
    nombres.append(int(nombre))

# Appel de la fonction tri_bulle pour trier la liste de nombres
nombres_tries = tri_bulle(nombres)

# Affichage des nombres triés
for nombre in nombres_tries:
    print(nombre, end=" ")
