
#######nombre de bits à 1 ##########

n = int(input("Entrez un nombre : "))

binaire = bin(n)  # transforme en binaire 
compteur = 0

for bit in binaire:
    if bit == '1':
        compteur += 1

print("Nombre de bits à 1 :", compteur)




############swap bits #############
n = int(input("Entrez un nombre : "))
i = int(input("Index i : "))
j = int(input("Index j : "))

binaire = list(bin(n)[2:])  # enlève '0b' et transforme en liste

# compléte avec des 0 si besoin
while len(binaire) <= max(i, j):
    binaire.insert(0, '0')

# inverse les positions 
binaire[-1 - i], binaire[-1 - j] = binaire[-1 - j], binaire[-1 - i]

# reconstruit le nombre
resultat = int("".join(binaire), 2)

print("Résultat :", resultat)