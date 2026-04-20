#pseudo code pour la fonction listen 
fonction listen():
    créer une socket TCP
    binder la socket sur (adresse, port)
    mettre la socket en écoute

    tant que nombre de clients < max_players:
        accepter une nouvelle connexion
        ajouter la socket du joueur dans la liste clients
        afficher "Nouveau joueur connecté"

-  On utilise des threads parce que chaque joueur doit pouvoir jouer en même temps, sans bloquer les autres.
Si un joueur met 10 secondes à répondre, le serveur ne doit pas être bloqué.
Donc :
==> Un thread par joueur
==> Chaque thread exécute communicate_with_client()
Où utiliser les threads ?
Dans listen() quand un joueur se connecte :
 - créer un thread pour communicate_with_client(client)
 - lancer le thread


#Si on utilise UDP au lieu de TCP ce qu’il faut changer dans le code
- Supprimer listen() et accept() car UDP n’a pas de connexion
- Utiliser recvfrom() au lieu de recv() ==> car il faut connaître l’adresse du client.
- Utiliser sendto() au lieu de send() ==> car UDP n’a pas de socket dédiée par client.
- Gérer les pertes de messages==> UDP n’est pas fiable.

Comparatif : 
TCP est un protocole orienté connexion : il utilise listen() et accept() pour établir une communication entre le client et le serveur. Chaque client possède sa propre socket. Les échanges se font avec send() et recv(). TCP est fiable : il garantit que les données arrivent sans perte et dans le bon ordre. Il est orienté flux, ce qui signifie que les données sont vues comme un flux continu.

UDP, au contraire, est sans connexion : il n’y a pas de listen() ni accept(). Une seule socket est utilisée pour tous les clients. Les échanges se font avec sendto() et recvfrom(). UDP n’est pas fiable : des pertes sont possibles et l’ordre des messages n’est pas garanti. Il est orienté message, donc chaque envoi est indépendant.