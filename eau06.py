
import sys

# Fonction qui met en majuscule une lettre sur deux
def mettre_en_majuscule_une_lettre_sur_deux(chaine_entree):
    
    chaine_sortie = ""    # Initialisation de la chaîne de sortie
    if chaine_sortie.isdigit():
        print("error")
        sys.exit(1)
    compteur_lettres = 0  # Compteur de lettres pour savoir si on doit mettre en majuscule ou non
    for caractere in chaine_entree:
        if caractere.isalpha():  # Si le caractère est une lettre
            if compteur_lettres % 2 == 0:
                chaine_sortie += caractere.upper()  # Mettre en majuscule une lettre sur deux
            else:
                chaine_sortie += caractere.lower()  # Mettre en minuscule une lettre sur deux
            compteur_lettres += 1  # Incrémenter le compteur de lettres
        else:
            chaine_sortie += caractere  # Ajouter les caractères qui ne sont pas des lettres (espaces, ponctuation, etc.)
    return chaine_sortie

# Récupération de la chaîne de caractères en entrée
chaine_entree = sys.argv[1]

# Appel de la fonction 'mettre_en_majuscule_une_lettre_sur_deux' et affichage du résultat
chaine_sortie = mettre_en_majuscule_une_lettre_sur_deux(chaine_entree)
print(chaine_sortie)
