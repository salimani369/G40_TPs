import socket

class LeChat:

    def __init__(self, max_client=3, max_message_len=1500,
                 ip_address="127.0.0.1", port=1600):

        self.max_client = max_client
        self.max_message_len = max_message_len
        self.ip_address = ip_address
        self.port = port

        # Création du socket serveur
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Liste des clients connectés
        self.clients = []

        # Pour calculer la moyenne des notes
        self.total_notes = 0
        self.nb_notes = 0


    # Lancer le serveur
    def serveur(self):
        self.sock.bind((self.ip_address, self.port))
        self.sock.listen(self.max_client)
        print("Serveur lancé sur", self.ip_address, "port", self.port)


    # Gérer les connexions entrantes
    def manage_connexions(self):
        print("En attente de clients...")

        while True:
            conn, addr = self.sock.accept()
            print("Nouveau client:", addr)

            self.clients.append(conn)

            # On gère le client dans cette même boucle
            self.handle_client(conn)


    # Tokenizer : transforme un message en liste d'entiers
    def tokenizer(self, message, vocab):
        mots = message.split()
        resultat = []

        for mot in mots:
            if mot in vocab:
                resultat.append(vocab[mot])
            else:
                resultat.append(0)   # mot inconnu : 0

        return resultat


    # Simulation d’un LLM

    def handle_llm(self, liste_entiers):
        # On renvoie juste une phrase simple
        return "Réponse du LLM basée sur " + str(liste_entiers)


    # Communication avec un client

    def handle_client(self, client_socket):

        while True:
            data = client_socket.recv(2048)

            if not data:
                print("Client déconnecté")
                break

            message = data.decode()

            print("Message reçu:", message)

          
            # Vérification du message
            if (not message.endswith("?")
                or len(message) > self.max_message_len
                or "merci" in message.lower()):

                client_socket.send("Texte invalide".encode())
                continue


            # Tokenization

            vocab = {
                "bonjour": 1,
                "comment": 2,
                "ça": 3,
                "va": 4,
                "?": 5
            }

            tokens = self.tokenizer(message, vocab)

            # Appel du LLM
            reponse = self.handle_llm(tokens)

            # Envoi au client
            client_socket.send(reponse.encode())

            # Réception de la note
            note_data = client_socket.recv(1024)
            note = int(note_data.decode())

            print("Note reçue:", note)

            # Mise à jour de la moyenne
            self.total_notes += note
            self.nb_notes += 1


    # Renvoyer la moyenne des notes
    def get_evaluation(self):
        if self.nb_notes == 0:
            return 0
        return self.total_notes / self.nb_notes