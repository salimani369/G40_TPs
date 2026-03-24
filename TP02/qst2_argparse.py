import socket
import argparse
 
DEFAULT_HOST = '127.0.0.1'
DEFAULT_PORT = 1060
 
 
def recv_all(sock, length):
    data = ''
    while len(data) < length:
        more = sock.recv(length - len(data))
        if not more:
            raise EOFError('la socket a ete fermee')
        data += more.decode()
    return data
 
 
def run_server(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host, port))
    s.listen(1)
 
    print(f'Serveur en ecoute sur {host}:{port}')
    while True:
        sc, sockname = s.accept()
        print(f'Connexion acceptee de : {sockname}')
 
        message = recv_all(sc, 9)
        print(f'Message recu : {repr(message)}')
 
        sc.sendall('Au revoir !'.encode())
        sc.close()
        print('Reponse envoyee.\n')
 
 
def run_client(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    print(f'Connecte a {host}:{port} depuis {s.getsockname()}')
 
    s.sendall('Bonjour !'.encode())
 
    reply = recv_all(s, 11)
    print(f'Reponse du serveur : {repr(reply)}')
 
    s.close()
 
 
if __name__ == '__main__':
    # Définition des arguments en ligne de commande
    parser = argparse.ArgumentParser(description='Client/Serveur TCP')
 
    parser.add_argument(
        'mode',
        choices=['server', 'client'],
        help='Mode de lancement : server ou client'
    )
    parser.add_argument(
        '--host',
        default=DEFAULT_HOST,
        help=f'Adresse IP (defaut: {DEFAULT_HOST})'
    )
    parser.add_argument(
        '--port',
        type=int,
        default=DEFAULT_PORT,
        help=f'Port (defaut: {DEFAULT_PORT})'
    )
 
    args = parser.parse_args()
 
    if args.mode == 'server':
        run_server(args.host, args.port)
    else:
        run_client(args.host, args.port)