"""
Fonction qui renvoie le nombre de mots contenus dans la phrase
passé en paramètre.

PS : on considère comme mots les ensembles de caractères inclus
entre les espaces.
"""

def nombre_mots(phrase):
    longueur_phrase = len(phrase)
    nb_mots = 1
    i = 0
    while i < longueur_phrase:
        lettres = phrase[i]
        if lettres == " ":
            nb_mots += 1
        i += 1
    return nb_mots

print(nombre_mots("Python est un langage formidable"))


"""
la fonction renvoi: 5
"""


# ****** AUTRE SOLUTION ******


def nombre_mots(phrase):
    mots = phrase.split(" ")  # transforme une chaîne de caractère en liste
    return len(mots)

print(nombre_mots("Python est un langage formidable"))


"""
la fonction renvoi: 5
"""