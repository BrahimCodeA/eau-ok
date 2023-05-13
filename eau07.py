
import sys

def mettre_majuscule_premiere_lettre(chaine):
    mots = chaine.split()  # Divise la chaîne en mots
    mots_majuscule = [mot.capitalize() for mot in mots]  # Met en majuscule la première lettre de chaque mot
    return ' '.join(mots_majuscule)  # Réunit les mots modifiés en une seule chaîne de caractères

chaine = sys.argv[1]  # Récupère la chaîne de caractères passée en argument

# Si un nombre est passé en argument alors on affichera error
if chaine.isdigit():
     print("error")
     sys.exit()

try:
    resultat = mettre_majuscule_premiere_lettre(chaine)  # Applique la fonction pour mettre en majuscule la première lettre de chaque mot
    print(resultat)
    

except AttributeError:
    print("error")
    