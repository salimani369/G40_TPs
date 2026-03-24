# 2 nombres qui font 0
def somme_nulle_deux(t):
    result = []

    for a in t:
        for b in t:
            if a != b:
                if a + b == 0:
                    result.append([a, b])

    return result


# 3 nombres qui font 0
def somme_nulle_trois(t):
    result = []

    for a in t:
        for b in t:
            for c in t:
                if a != b and a != c and b != c:
                    if a + b + c == 0:
                        result.append([a, b, c])

    return result


t = [1, 20, 15, 3, 5, -3, 41]

print(somme_nulle_deux(t))
print(somme_nulle_trois(t))