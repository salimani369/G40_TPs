
Le TP5 vise à voir ce qui se passe sous la couche Transport en construisant soi‑même les en‑têtes IP et TCP. Contrairement aux TPs précédents, l’OS ne gère plus les en‑têtes, la fiabilité ou la connexion : on fabrique et envoie un paquet complet (IP + TCP + données) à la main

##Principales différences avec les TPs précédents

- UDP (TP1) utilise SOCK_DGRAM et laisse l’OS gérer l’en‑tête IP.
- TCP (TP2–TP4) utilise SOCK_STREAM, nécessite connect() et bénéficie de la fiabilité intégrée
- Raw socket (TP5) utilise SOCK_RAW + IPPROTO_RAW, sans connect(), et demande les droits root
Dans ce TP on crée l’en‑tête IP, l’en‑tête TCP (avec checksum), puis on assemble et envoie le paquet avec sendto()
Comparatif:

##UDP

-Type : SOCK_DGRAM
-Couche OSI : 4 (Transport)
-Connexion : aucune (non connecté)
-En‑têtes : gérés automatiquement par l’OS
-Checksum : calculé par l’OS
-Fiabilité : aucune garantie
-Droits : utilisateur normal

##TCP

-Type : SOCK_STREAM
-Couche OSI : 4 (Transport)
- Connexion : obligatoire (connect())
- En‑têtes IP/TCP : générés par l’OS
- Checksum : calculé par l’OS
- Fiabilité : assurée par TCP (retransmissions, ordre, intégrité)
- Droits : utilisateur normal

##Raw Socket
- Type : SOCK_RAW + IPPROTO_RAW
- Couche OSI : 3 (Réseau)
- Connexion : aucune (pas de handshake TCP)
- En‑têtes IP/TCP : construits manuellement
- Checksum : calculé manuellement
- Fiabilité : aucune, tout est à gérer soi‑même
- Droits : root obligatoire (il a fallu utiliser powershell avec droits d'adminstrateurs pour exécuter)

###Limites des raw sockets
-Exécution avec droits d'admininstrateur  obligatoire
- Réception brute : on reçoit l’intégralité du paquet (IP + TCP + données)
- Pas de handshake TCP 
- Pas de retransmission automatique en cas de perte
- Checksum TCP à calculer manuellement via un pseudo‑header
- Code plus long et plus complexe qu’une socket classique


