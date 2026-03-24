import socket

HOST = '127.0.0.1'   #identifiants de la socket du serveur auquelon souhaite se connecter 
PORT = 1060
"""
def recv_all(sock, length): #fonction pour boucler jusqu'à avoir toutes les données attendues
    data = b''
    while len(data) < length:
        more = sock.recv(length - len(data))
        if not more:
            raise EOFError('la socket a ete fermee')
        data += more

    return data

def client():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #creation de la socket client TCP 
    s.connect((HOST, PORT)) #etablissment de la connexion avec le serveur (handshake)
    print('Le serveur a assigne {} comme socket pour le client'.format(s.getsockname()))
    s.sendall(b'Bonjour !')
    reply = recv_all(s, 11)
    print('Le serveur a repondu : ', repr(reply))
    s.close()

if __name__ == '__main__':  #point d'entree du programme
    client()

"""
Le serveur utilise une socket d'écoute pour accueillir 
   les clients et crée une socket de service dédiée pour chaque conversation.
"""
"""

#############regroupement class ###########################################
# On regroupe toutes les fonctions du client dans une classe
class Client:
 
    def __init__(self):
  
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    # création la socket TCP
        self.sock.connect((HOST, PORT))  # On se connecte au serveur
 
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

        print('Le serveur a assigne {} comme socket pour le client'.format(self.sock.getsockname()))    # Envoie un message et attend la réponse
 
        self.sock.sendall('Bonjour !'.encode())    # On envoie le message
 
        reply = self.recv_all(self.sock, 11)    # On attend la réponse
        print('Le serveur a repondu :', repr(reply))
 
        self.sock.close() # On ferme la connexion
 
 
if __name__ == '__main__':
    # On crée un objet Client et on le démarre
    client = Client()
    client.demarrer()