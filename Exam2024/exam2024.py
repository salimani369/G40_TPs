class Game:
    def __init__(self, initial_sticks, max_players):
        # Nombre de bâtonnets au début (on ne le change jamais)
        self.initial_sticks = initial_sticks

        # Nombre de bâtonnets qui vont diminuer pendant la partie
        self.remaining_sticks = initial_sticks

        # Nombre maximum de joueurs autorisés
        self.max_players = max_players

        # Liste des sockets des joueurs connectés
        self.clients = []



def communicate_with_client(self, client_id):
    # 1 Envoyer la consigne
    self.send(client_id, "Choisissez 1, 2 ou 3 bâtonnets à retirer")

    # 2 Lire la réponse
    reponse = self.read(client_id)

    # 3 Vérifier que c'est un nombre valide
    if not reponse.isdigit():
        self.send(client_id, "Erreur : vous devez entrer un chiffre")
        return

    choix = int(reponse)

    if choix < 1 or choix > 3:
        self.send(client_id, "Erreur : choisissez 1, 2 ou 3")
        return

    # 4 Mettre à jour le nombre de bâtonnets
    self.remaining_sticks -= choix

    # 5 Vérifier si le joueur perd
    if self.remaining_sticks <= 0:
        self.send(client_id, "perdu")

        # Tous les autres gagnent
        for other in self.clients:
            if other != client_id:
                self.send(other, "gagné")
    else:
        self.send(client_id, "vous restez dans le jeu")


#Fonction principale de Game 
def start(self):
    self.listen()  # accepter les connexions

    # Lancer un thread par joueur
    for client_id in self.clients:
        t = Thread(target=self.communicate_with_client, args=(client_id,))
        t.start()



#Si on utilise UDP au lieu de TCP 
#Serveur UDP 
# créer socket UDP
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# bind
server.bind(("localhost", 1234))

print("Serveur UDP en attente...")

while True:
    # recevoir message + adresse client
    message, addr = server.recvfrom(1024)

    print("Reçu :", message.decode())

    # répondre au client
    server.sendto(b"message reçu", addr)


#cient UDP 
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# envoyer message au serveur
client.sendto(b"hello", ("localhost", 1234))

# recevoir réponse
data, addr = client.recvfrom(1024)

print("Réponse :", data.decode())
