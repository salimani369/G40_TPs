# Gestion des threads dans le serveur

## 1. Création des threads
À chaque connexion d’un client, le serveur crée un nouveau thread :

start_new_thread(communication_client, (c,))

Chaque thread gère un client indépendamment, ce qui permet au serveur de traiter plusieurs connexions en parallèle.

## 2. Problèmes de concurrence
Comme plusieurs threads s’exécutent en même temps, ils peuvent accéder aux mêmes ressources :
- affichages (print)
- variables partagées
- structures de données communes

Sans synchronisation, les sorties peuvent se mélanger et les données peuvent être modifiées simultanément, ce qui rend le comportement du programme imprévisible.

## 3. Utilisation d’un verrou (Lock)
Pour éviter ces conflits, un verrou est utilisé :

print_lock = threading.Lock()

Avant d’accéder à une ressource partagée :
print_lock.acquire()

Après utilisation :
print_lock.release()

Le verrou garantit qu’un seul thread à la fois accède à la section protégée. Oublier release() peut bloquer tout le programme (deadlock).

## 4. Conclusion
- Le serveur utilise des threads pour gérer plusieurs clients simultanément.
- Cela améliore la réactivité.
- Les verrous sont indispensables pour éviter les conflits entre threads.
- Sans synchronisation, le programme peut produire des erreurs ou des comportements incohérents.

# Exercices d’algorithmie

## Somme nulle de deux éléments
Objectif : trouver tous les couples d’éléments dont la somme est égale à zéro.

Exemple :
Entrée : [1, 20, 15, 3, 5, -3, 41]
Sortie : [3, -3]

J'ai deux boucles imbriquées sur la liste t de taille n
Donc chaque élément a est comparé à tous les éléments b : n × n opérations

- Complexité : O(n²)

- Non il n’existe pas d’algorithme plus rapide que O(n²) pour ce problème dans le cas général

## Somme nulle de trois éléments
Objectif : trouver trois éléments dont la somme est nulle.

Exemple :
Entrée : [1, 20, 15, 3, 5, -4, 41]
Sortie : [1, 3, -4]

- On utilise trois boucles imbriquées, chacune parcourant n éléments.
donc on examine toutes les combinaisons de trois éléments : n × n × n opérations.

- Complexité : O(n³)

