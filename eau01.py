
def afficher_combinaisons():
    # Itération sur les nombres de 0 à 99 inclus
    for premier_nombre in range(100):
        
        # Itération sur les nombres qui suivent le premier nombre (de premier_nombre+1 à 99 inclus)
        for deuxieme_nombre in range(premier_nombre+1, 100):
            
            # Affichage de la paire de nombres formatée
            print("{:02d} {:02d}".format(premier_nombre, deuxieme_nombre), end=", ")
            
    # Suppression de la virgule et de l'espace en fin de ligne
    print("\b\b")

# Exemple d'utilisation de la fonction
afficher_combinaisons()
