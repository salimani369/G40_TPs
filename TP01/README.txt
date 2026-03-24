Application de chat :

Ces scripts mettent en place une communication UDP simple entre un client et un serveur sur la même machine (127.0.0.1).
Le serveur (server.py) après exécution reste en attente de messages. Lorsqu'il reçoit un texte, il l'affiche dans la console, calcule la taille du message reçu en octets et renvoie cette information au client.
Le client (client.py) crée un message contenant l'heure actuelle et l'envoie au serveur, affiche sa propre adresse réseau et port dans la console (0.0.0.0, 58160), puis attend la réponse du serveur pour l'afficher.
socket.socket() : crée un nouveau point de terminaison de communication/le socket
sock.bind() : attache le socket à une adresse IP et un port précis
sock.recvfrom() : reçoit des données et récupère l'adresse de l'expéditeur
sock.sendto() : envoie des données vers une adresse spécifique
sock.getsockname() : retourne l'adresse IP et le port que le socket utilise actuellement
decode('ascii') : transforme les bytes reçus en texte lisible
encode('ascii') : transforme le texte en bytes pour l'envoi sur le réseau
format() : permet d'insérer des variables dynamiquement dans une chaîne de caractères

Les inconvénients de l'architecture client-serveur-client :

Si le serveur plante, tout s'arrête car tous les clients dépendent de lui.
-Si on a 100 clients qui parlent en même temps, le serveur doit gérer tous les messages à la fois. Il peut vite être dépassé.
UDP perd des messages, un message peut ne jamais arriver et personne ne le saura.
Pas d'historique, si on est déconnecté au moment où quelqu'un nous on envoie un message, on ne le recevras jamais. Les messages ne sont pas sauvegardés.
Le serveur ne sait pas si un client est encore là, si un client ferme son programme sans prévenir, le serveur continue à essayer de lui envoyer des messages pour rien