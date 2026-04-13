####Lien météo (requests)

requests.get() permet d’envoyer une requête HTTP, un peu comme on le ferais avec Postman ou HTTPie, mais directement depuis Python.

Ensuite, response.json() transforme automatiquement la réponse en dictionnaire Python, ce qui évite de manipuler du texte brut et c’est pratique.

Quand on utilise params={}, python se charge tout seul de construire l’URL avec les paramètr, donc pas besoin de le faire à la main.

Par contre, le code ne gère pas encore les erreurs réseau (par exemple y’as pas internet). il faudrait ajouter un try/except.

#######Django REST Framework

ModelViewSet est très pratique car avec une seule classe, on obtient automatiquement toutes les routes classiques (GET, POST, PUT, DELETE, LIST), sans avoir à tout coder.

Le router.register() simplifie aussi beaucoup les choses, car il fait automatiquement le lien entre les URLs et les méthodes HTTP.

Le sérialiseur est très important : il convertit les données dans les deux sens (Python → JSON et JSON → Python) et s’occupe aussi de valider les données reçues.

-par défaut, l’API est ouverte. N’importe qui peut accéder, créer ou supprimer des données. En production, il faut absolument ajouter de la sécurité (authentification, permissions…).

#####Algo fusion de tableaux

La version simple avec sorted(nums1 + nums2) est facile à écrire, mais elle crée un nouveau tableau en mémoire → donc consommation en O(n).

La version optimisée modifie le tableau directement (in-place) en partant de la fin. Ça évite d’écraser des valeurs encore utiles et ça ne consomme pas de mémoire supplémentaire → O(1), donc beaucoup plus efficace.

Si on commence par le début, on risque d’écraser des données importantes et c’est le piège de l'exercice.