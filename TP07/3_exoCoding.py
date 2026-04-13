
###################Version avec espace supplémentaire######################

"""def fusionner(nums1, nums2):
    i = 0  # pointeur sur nums1 (index du prochain élément à comparer)
    j = 0  # pointeur sur nums2
    resultat = []  # tableau final fusionné

    # Tant qu'il reste des éléments dans les deux tableaux
    while i < len(nums1) and j < len(nums2):
        # On compare les deux éléments courants
        if nums1[i] < nums2[j]:
            # Si l'élément de nums1 est plus petit, on l'ajoute au résultat
            resultat.append(nums1[i])
            i += 1  # on avance dans nums1
        else:
            # Sinon, on ajoute l'élément de nums2
            resultat.append(nums2[j])
            j += 1  # on avance dans nums2

    # À ce stade, un des deux tableaux est entièrement parcouru.
    # On ajoute donc les éléments restants de nums1 (si i n'est pas au bout)
    resultat.extend(nums1[i:])
    # Et les éléments restants de nums2 (si j n'est pas au bout)
    resultat.extend(nums2[j:])

    return resultat  # tableau fusionné et trié


# Tests
print(fusionner([1, 2, 3], [2, 5, 6]))
print(fusionner([1], []))               """


##########Version sans espace supplémentaire (fusion en place)##########################

def fusionner_inplace(nums1, m, nums2, n):
    # i = dernier index utile de nums1
    i = m - 1
    # j = dernier index de nums2
    j = n - 1
    # k = dernier index total de nums1
    k = m + n - 1

    # Tant qu'il reste des éléments dans nums2
    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1


nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
fusionner_inplace(nums1, 3, nums2, 3)
print(nums1) 




