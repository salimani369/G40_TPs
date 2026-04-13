def nombre_de_mots(texte):
    # split() découpe le texte en mots en utilisant les espaces comme séparateurs
    mots = texte.split()

    # len(mots) renvoie le nombre d'éléments dans la liste : donc le nombre de mots
    return len(mots)


print("\n=== Nombre de mots ===")
texte = "Bonjour tout le monde, commencez à coder."
print("Texte :", texte)
print("Nombre de mots :", nombre_de_mots(texte))   