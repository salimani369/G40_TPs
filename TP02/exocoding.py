def contains_duplicate(tableau):
    
    taille_avant = len(tableau)       # on compte combien d'éléments il y a
    taille_apres = len(set(tableau))  # on remet dans un set (sans doublons)
    
    if taille_avant != taille_apres:  # si la taille a changé...
        return True                   # c'est qu'il y avait des doublons 
    else:
        return False                  # sinon pas de doublons
    


 
def is_anagram(mot1, mot2):
    
    mot1_trie = sorted(mot1)  # on trie les lettres de mot1 dans l'ordre alphabétique
    mot2_trie = sorted(mot2)  # on trie les lettres de mot2 dans l'ordre alphabétique
    
    if mot1_trie == mot2_trie:  # si les deux listes triées sont pareilles...
        return True             # c'est un anagramme
    else:
        return False            # sinon non
    