import socket

HOST = '127.0.0.1'   # Configuration de l'adresse (localhost) et du port du socket serveur 
PORT = 1060

"""
def recv_all(sock, length):  # définit le nombre d'octets attendus (length)
    data = b''   #initialisation en bytes directement au lieu de str 
    while len(data) < length:  #on compare la taille de données recues avec ce que l'on attend 
        more = sock.recv(length - len(data))
        if not more:
            raise EOFError('la socket a ete fermee')  #si le serveur ne recoit rien ca veut dire qu ele client  a fermé la connexion
        data += more

    return data

def server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #creation de la socket TCP 
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  #réutiliser le port immédiatement après un arrêt
    s.bind((HOST, PORT))  #binding de la socket à la l'adresse IP et port 
    s.listen(1)  #écoute pour une durée indéfinie 
    while True:
        print('le serveur ecoute a cette adresse ', s.getsockname())
        sc, sockname = s.accept()
        print('Le serveur a accepte une connexion de ', sockname)
        print('Une connexion : ', sc.getsockname(), ' et ', sc.getpeername())
        message = recv_all(sc, 9)
        print('Les 16 octets recu : ', repr(message))
        sc.sendall(b'Au revoir !')
        sc.close()
        print("Une reponse a ete envoye, la socket est fermee")

if __name__ == '__main__': 
    server()
"""

"""
1. utilisation de SOCK_STREAM (TCP) établit une connexion
   entre le client et le serveur avant tout échange de données.
   
2. La fonction recv_all  garantit que le 
   serveur attend de recevoir la totalité des octets prévus avant de continuer

3. - La socket 's' sert uniquement à écouter (listen) les nouveaux arrivants
   - La socket 'sc' est créée par 'accept' pour communiquer avec le client actuel.
"""


#########regroupement class ##################################################


# On regroupe toutes les fonctions du serveur dans une classe
class Serveur:

    def __init__(self):
        # On crée la socket TCP
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # On permet de relancer le serveur sans attendre
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # On attache la socket à l'adresse et au port
        self.sock.bind((HOST, PORT))
        # On se met en écoute
        self.sock.listen(1)

    def recv_all(self, sock, length):
        # Reçoit exactement "length" octets
        data = ''
        while len(data) < length:
            more = sock.recv(length - len(data))
            if not more:
                raise EOFError('la socket a ete fermee')
            data += more.decode()
        return data

    def demarrer(self):
        # Démarre le serveur et attend les connexions
        while True:
            print('le serveur ecoute a cette adresse :', self.sock.getsockname())
            sc, sockname = self.sock.accept()
            print('Le serveur a accepte une connection de :', sockname)
            print('Une connexion :', sc.getsockname(), 'et', sc.getpeername())

            message = self.recv_all(sc, 9)
            print('Les 9 octets recu :', repr(message))

            sc.sendall('Au revoir !'.encode())
            sc.close()
            print("Une reponse a ete envoye, la socket est fermee")


if __name__ == '__main__':
    # On crée un objet Serveur et on le démarre
    serveur = Serveur()
    serveur.demarrer()

