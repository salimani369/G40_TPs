def nombre_de_facons(n):
    # Cas de base :
    # Si l'escalier a 1 marche → 1 seule façon (1)
    if n == 1:
        return 1

    # Si l'escalier a 2 marches → 2 façons (1+1 ou 2)
    if n == 2:
        return 2

    # a = f(1), b = f(2)
    a = 1
    b = 2

    # On commence à calculer à partir de la 3e marche
    i = 3

    # Tant qu'on n'a pas atteint n
    while i <= n:
        # c = f(i) = f(i-1) + f(i-2)
        c = a + b

        # On décale les valeurs :
        # l'ancien f(i-1) devient f(i-2)
        a = b
        # l'ancien f(i) devient f(i-1)
        b = c

        # On passe à la marche suivante
        i = i + 1

    # b contient maintenant f(n)
    return b

print("Escaliers")
print("4 marches :", nombre_de_facons(4))  
print("5 marches :", nombre_de_facons(5))  