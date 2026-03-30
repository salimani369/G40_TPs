def romain_to_int(s):
    valeurs = {'I':1, 'V':5, 'X':10, 'L':50,
               'C':100, 'D':500, 'M':1000}
    
    total = 0
    prev = 0
    
    for c in reversed(s):
        val = valeurs[c]
        if val < prev:
            total -= val
        else:
            total += val
        prev = val
        
    return total

print(romain_to_int("III")) 
print(romain_to_int("MCMXCIV"))  

####algorithme dans le cas contraire 

def int_to_romain(num):
    val = [
        (1000,'M'), (500,'D'),
        (100,'C'), (50,'L'),
        (10,'X'), (5,'V'), (1,'I')
    ]
    
    res = ""
    
    for v, sym in val:
        while num >= v:
            res += sym
            num -= v
            
    return res

print(int_to_romain(3))    
print(int_to_romain(1994)) 

# On ajoute les formes soustractives (comme IV pour 4) à la liste pour respecter la notation romaine moderne et éviter d'écrire IIII

def int_to_romain(num):
    val = [
        (1000,'M'), (900,'CM'), (500,'D'), (400,'CD'),
        (100,'C'), (90,'XC'), (50,'L'), (40,'XL'),
        (10,'X'), (9,'IX'), (5,'V'), (4,'IV'), (1,'I')
    ]
    
    res = ""
    
    for v, sym in val:
        while num >= v:
            res += sym
            num -= v
            
    return res

print(int_to_romain(1994))  