import socket
from datetime import datetime


""""
MAX_BYTES = 65535   #taille maximum du paquet UDP que le client accepte de recevoir du serveur 

def client(port):  #fonction de création d'un socket UDP 
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #une socket UDP est définie par le type de protocole ip (AF_INET=IPv4) et le type de protocole de transport (SOCK_DGRAM=UDP) 
    text = 'Le temps est {}'.format(datetime.now())
    data = text.encode('ascii')  # conversion str vers bytes car socket utilise bytes
    sock.sendto(data, ('127.0.0.1', port))  # envoi le datagramme au serveur local sur le port donné
    print('mon adresse est {}'.format(sock.getsockname())) # affiche l'adresse locale du client (IP=0.0.0.0 + port choisi aléatoire)
    data, address = sock.recvfrom(MAX_BYTES)  # réception de la réponse du serveur (bloquant jusqu'à réception)
    text = data.decode('ascii')  #decodage des données réçues de bytes vers str 
    #sock.sendto(data, address) #renvoi de l'adresse au serveur, et ici c'est erruer qui mit fin à la connexion  
    # la socket de renvoi(communication) n'a pas été créé correctement   

if __name__ == '__main__':
    client(1060)      """


#Le serveur ecoute sur l'adresse locale sur le port 1060
#le client local (parce qu'il est sur la meme machine/localhost malgré que son adresse annoncée est 0.0.0.0) et son port choisi aléatoirement 58055 dit au serveur le temps/date 


########## meme programme en class #####

"""
class UDPServer:
    def __init__(self, host='127.0.0.1', port=1060):
        self.address = (host, port)
        self.MAX_BYTES = 65535
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def start(self):
        self.sock.bind(self.address)
        print(f'En écoute sur {self.sock.getsockname()}')
        
        while True:
            data, address = self.sock.recvfrom(self.MAX_BYTES)
            text = data.decode('ascii')
            print(f'Le client {address} dit {text!r}')
            
            # Préparation de la réponse
            response = f'Les données ont une taille de {len(data)} octets'
            self.sock.sendto(response.encode('ascii'), address)

if __name__ == '__main__':
    server = UDPServer()
    server.start()
"""

 
import threading
 
MAX_BYTES = 65535
 
def recevoir(sock):
    while True:
        data, address = sock.recvfrom(MAX_BYTES)
        print('Message recu : {}'.format(data.decode('ascii')))
 
def client(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('127.0.0.1', 0))
 
    t = threading.Thread(target=recevoir, args=(sock,))
    t.daemon = True
    t.start()
 
    while True:
        message = input('Message : ')
        sock.sendto(message.encode('ascii'), ('127.0.0.1', port))
 
if __name__ == '__main__':
    client(1060)