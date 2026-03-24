"""import socket
import threading
from _thread import *
import threading """

#########regroupement du code du serveur en classe ###########
"""class ServeurTCP:
    def __init__(self, host="", port=12345):
        self.host = host
        self.port = port
        self.print_lock = threading.Lock()
        self.socket_ecoute = None

    def communication_client(self, c):
        #Gère la communication avec un client connecté
        while True:
            data = c.recv(1024)
            if not data:
                with self.print_lock:
                    print("Client déconnecté")
                break

            # Réponse envoyée au client
            reponse = "Welcome"
            c.send(reponse.encode())

        c.close()

    def thread_ecoute(self):
        #Thread principal d'écoute et d'acceptation des connexions
        self.socket_ecoute = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_ecoute.bind((self.host, self.port))

        print(f"Socket bindée au port {self.port}")
        self.socket_ecoute.listen(5)
        print("Le serveur est en écoute...")

        while True:
            c, addr = self.socket_ecoute.accept()

            with self.print_lock:
                print(f"Connecté au client : {addr[0]} : {addr[1]}")

            start_new_thread(self.communication_client, (c,))

    def start(self):
        Démarre le serveur
        self.thread_ecoute()


if __name__ == "__main__":
    serveur = ServeurTCP(host="", port=1060)
    serveur.start()"""


#################code serveur modifié pour qu'il envoie la liste des clients"
# ##########
import socket
import threading

HOST, PORT = "127.0.0.1", 1080
clients = {}

def handle_client(conn, name):
    while True:
        try:
            data = conn.recv(1024).decode()
            if not data or "|" not in data:
                break
            
            dest, msg = data.split("|", 1)
            if dest in clients:
                clients[dest].send(f"{name}: {msg}".encode())
        except:
            break

    # Nettoyage en cas de déconnexion
    clients.pop(name, None)
    conn.close()
    
    # Notification aux autres
    for c in clients.values():
        try: c.send(f"{name} s'est déconnecté".encode())
        except: pass

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Évite l'erreur de port occupé
    server.bind((HOST, PORT))
    server.listen()
    print("Serveur prêt...")

    while True:
        conn, addr = server.accept()
        name = conn.recv(1024).decode()
        
        # 1. Enregistrer le client
        clients[name] = conn
        
        # 2. Envoyer la liste actuelle (incluant lui-même)
        list_msg = "Clients connectés: " + ", ".join(clients.keys())
        conn.send(list_msg.encode())

        # 3. Lancer l'écoute
        threading.Thread(target=handle_client, args=(conn, name), daemon=True).start()

if __name__ == "__main__":
    start_server()