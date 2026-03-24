# 2 nombres qui font 0
def somme_nulle_deux(t):
    result = []
    n = len(t)

    # On utilise les indices (i et j) pour ne pas revenir en arrière
    for i in range(n):
        # On commence j juste apres i pour ne jamais comparer 
        # un nombre avec luimême ou une paire déjà vue
        for j in range(i + 1, n):
            if t[i] + t[j] == 0:
                result.append([t[i], t[j]])

    return result

z = [1, 20, 15, 3, 5, -3, 41]
print(somme_nulle_deux(z))

def somme_nulle_trois(t):
    result = []
    n = len(t)

    # Première boucle : on choisit le 1er nombre
    for i in range(n):
        # Deuxième boucle : on commence apres le 1er nombre
        for j in range(i + 1, n):
            # Troisième boucle : on commence apres le 2ème nombre
            for k in range(j + 1, n):
                if t[i] + t[j] + t[k] == 0:
                    result.append([t[i], t[j], t[k]])

    return result

t = [1, 20, 15, 3, 5, -4, 41]
print(somme_nulle_trois(t))