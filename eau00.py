
# Liste pour stocker les nombres générés
nombres_generes = []

# Boucle pour la première position dans le nombre (centaines)
for chiffre_centaine in range(10):
    
    # Boucle pour la deuxième position dans le nombre (dizaines)
    for chiffre_dizaine in range(chiffre_centaine, 10):
        
        # Boucle pour la troisième position dans le nombre (unités)
        for chiffre_unite in range(chiffre_dizaine, 10):
            
            # Vérifier que tous les chiffres sont différents
            if chiffre_centaine != chiffre_dizaine and chiffre_centaine != chiffre_unite and chiffre_dizaine != chiffre_unite:
                
                # Construire le nombre à partir des chiffres actuels
                nombre_actuel = chiffre_centaine * 100 + chiffre_dizaine * 10 + chiffre_unite
                
                # Vérifier que le nombre n'a pas déjà été généré
                if nombre_actuel not in nombres_generes:
                    
                    # Imprimer le nombre
                    print(nombre_actuel)
                    
                    # Ajouter le nombre à la liste des nombres générés
                    nombres_generes.append(nombre_actuel)