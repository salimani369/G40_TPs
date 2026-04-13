1.
- HTTP = protocole qui définit comment un navigateur demande des pages web
- Quand on ouvre une page web :
    1. Requête DNS pour avoir l'IP du serveur
    2. Connexion TCP ouverte
    3. Le navigateur demande la page
    4. Le serveur répond avec la page HTML
    5. Le navigateur demande les ressources (css, images, js)
    6. Affichage de la page
 
- Une requête HTTP ressemble à :
    GET /index.html HTTP/1.1
    Host: localhost:8000
    User-Agent: Mozilla/5.0
    (ligne vide)
    (body)
 
- Une réponse HTTP ressemble à :
    HTTP/1.1 200 OK
    Server: MonServeur
    (ligne vide)
    (body HTML)
 
- Méthodes HTTP : GET, POST, PUT, DELETE, HEAD
- Codes importants : 200 = OK, 404 = page non trouvée
 
 
2. Formatage d'une requête HTTP

- On crée une fonction format_requete_http()
- Paramètres : méthode, url, version, entetes (dict), body
- On vérifie que la méthode est dans [GET, POST, PUT, DELETE, HEAD]
- La version 1 → "HTTP/1.1", version 2 → "HTTP/2.0"
- On assemble : premiere_ligne + en-têtes + ligne vide + body
 
 
3. Formatage d'une réponse HTTP

- Même principe que l'exercice 1 mais pour une réponse
- Paramètres différents : version_str, status_code, status_info, entetes, body
- Exemple : HTTP/1.1 404 Not Found
 
4.Serveur avec sockets
- On utilise le module socket de Python (bas niveau)
- Le serveur écoute sur le port 8080
- Il lit la 1ère ligne de la requête pour savoir ce que veut le client
- Si GET /index.html → réponse 200 avec la page HTML
- Sinon → réponse 404
  
5. Serveur avec http.server

- Même chose mais avec la librairie http.server (plus simple)
- On crée une classe qui hérite de BaseHTTPRequestHandler
- On redéfinit do_GET() pour gérer les requêtes GET
- Le serveur tourne sur le port 8000
 
6. DJANGO - Application de chat

INSTALLATION :
    pip install django
    python -m django startproject chatServer
    cd chatServer
    python manage.py startapp g40aChat
    python manage.py migrate
    python manage.py runserver
 
STRUCTURE :
    chatServer/
        chatServer/
            urls.py     ← routing principal modifié
        g40aChat/
            views.py    ← les pages HTML modifiée
            urls.py     ← routing de l'app crée
        manage.py
 
FICHIERS IMPORTANTS :
- views.py : contient les fonctions qui retournent les pages HTML
- urls.py (g40aChat) : lie une URL à une fonction de views.py
- urls.py (chatServer) : relie l'URL "chat/" à l'application g40aChat
 
il y a deux dossiers "chatServer"
    - le grand (contient manage.py)
    - le petit (contient urls.py et settings.py)
 

7.Exercices de coding

ESCALIERS :
- Compter le nombre de façons de monter N marches (1 ou 2 marches à la fois)
- C'est la suite de Fibonacci : f(1)=1, f(2)=2, f(n) = f(n-1) + f(n-2)
- Exemple : 4 marches → 5 façons
 
NOMBRE DE MOTS :
- Compter les mots dans une chaîne de caractères
- On utilise texte.split() qui coupe aux espaces
- Puis len() pour compter
- Exemple : "Bonjour tout le monde" → 4 mots
