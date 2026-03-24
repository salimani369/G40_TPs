import socket


MAX_BYTES = 65535

"""
def server(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('127.0.0.1', port))
    print('En ecoute sur {}'.format(sock.getsockname()))
    while True:
        data, address = sock.recvfrom(MAX_BYTES)
        text = data.decode('ascii')
        print('Le client {} dit {!r}'.format(address, text))
        text = 'les donnees ont une taille de {} octets'.format(len(data))
        data = text.encode('ascii')
        sock.sendto(data, address)

if __name__ == '__main__':
    server(1060)
"""

###########meme programme en class ##############

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
            
            response = f'Les données ont une taille de {len(data)} octets'
            self.sock.sendto(response.encode('ascii'), address)

if __name__ == '__main__':
    server = UDPServer()
    server.start()
"""

import socket
 
MAX_BYTES = 65535
clients = []
 
def server(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('127.0.0.1', port))
    print('En ecoute sur {}'.format(sock.getsockname()))
 
    while True:
        data, address = sock.recvfrom(MAX_BYTES)
 
        if address not in clients:
            clients.append(address)
 
        text = data.decode('ascii')
        print('Client {} dit : {}'.format(address, text))
 
        # Relayer le message a tous les autres clients
        for client in clients:
            if client != address:
                sock.sendto(data, client)
 
if __name__ == '__main__':
    server(1060)