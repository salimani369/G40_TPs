TP5 — Raw Sockets & Modèle OSI

Le TP5 vise à comprendre ce qui se passe sous la couche Transport en construisant soi‑même les en‑têtes IP et TCP. Contrairement aux TPs précédents, l’OS ne gère plus les en‑têtes, la fiabilité ou la connexion : on fabrique et envoie un paquet complet (IP + TCP + données) à la main.
Principales différences avec les TPs précédents
- UDP (TP1) utilise SOCK_DGRAM et laisse l’OS gérer l’en‑tête IP.
- TCP (TP2–TP4) utilise SOCK_STREAM, nécessite connect() et bénéficie de la fiabilité intégrée.
- Raw socket (TP5) utilise SOCK_RAW + IPPROTO_RAW, sans connect(), et demande les droits root.
Dans ce TP, on crée l’en‑tête IP, l’en‑tête TCP (avec checksum), puis on assemble et envoie le paquet avec sendto().
Comparatif rapide
- UDP (TP1)
- Type : SOCK_DGRAM
- Couche OSI : 4 (Transport)
- Connexion : aucune (non connecté)
- En‑têtes : gérés automatiquement par l’OS
- Checksum : calculé par l’OS
- Fiabilité : aucune garantie
- Droits : utilisateur normal
TCP (TP2–TP4)
- Type : SOCK_STREAM
- Couche OSI : 4 (Transport)
- Connexion : obligatoire (connect())
- En‑têtes IP/TCP : générés par l’OS
- Checksum : calculé par l’OS
- Fiabilité : assurée par TCP (retransmissions, ordre, intégrité)
- Droits : utilisateur normal
Raw Socket (TP5)
- Type : SOCK_RAW + IPPROTO_RAW
- Couche OSI : 3 (Réseau)
- Connexion : aucune (pas de handshake TCP)
- En‑têtes IP/TCP : construits manuellement
- Checksum : calculé manuellement
- Fiabilité : aucune, tout est à gérer soi‑même
- Droits : root obligatoire

Limites des raw sockets
- Exécution en root obligatoire
- Réception brute : on reçoit l’intégralité du paquet (IP + TCP + données)
- Pas de handshake TCP (pas de SYN/SYN‑ACK/ACK)
- Pas de retransmission automatique en cas de perte
- Checksum TCP à calculer manuellement via un pseudo‑header
- Code plus long et plus complexe qu’une socket classique

Organisation du TP
ip_header.py : génération de l’en‑tête IP et checksum
tcp_header.py : checksum, en‑tête TCP, création du paquet
clients TP1 → TP5 : versions adaptées en raw socket pour chaque exercice précédent

TP1–TP3 : couche 4 (Transport)
TP4 : couche 6 (Présentation)
TP5 : couche 3 (Réseau)
