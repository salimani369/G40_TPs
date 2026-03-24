import socket
import argparse
import sys

DEFAULT_HOST = '127.0.0.1'
DEFAULT_PORT = 1060


def recv_all(sock, length):
    data = b''
    while len(data) < length:
        more = sock.recv(length - len(data))
        if not more:
            raise EOFError('la socket a ete fermee')
        data += more
    return data.decode()


def run_server(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host, port))
    s.listen(1)

    print(f'Serveur en ecoute sur {host}:{port}')
    while True:
        sc, sockname = s.accept()
        print(f'Connexion de : {sockname}')

        # Lecture de la longueur du message d'abord (4 octets)
        raw_len = sc.recv(4)
        if not raw_len:
            sc.close()
            continue
        msg_len = int.from_bytes(raw_len, 'big')

        # Puis lecture du message
        message = recv_all(sc, msg_len)
        print(f'Message recu : {repr(message)}')

        # Réponse saisie par l'utilisateur côté serveur
        print('Tapez votre reponse (ou appuyez sur Entree pour "Au revoir !") :')
        response = sys.stdin.readline().strip()
        if not response:
            response = 'Au revoir !'

        sc.sendall(len(response).to_bytes(4, 'big') + response.encode())
        sc.close()
        print('Reponse envoyee.\n')


def run_client(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    print(f'Connecte a {host}:{port}')

    # Message saisi par l'utilisateur
    print('Tapez votre message :')
    message = sys.stdin.readline().strip()
    if not message:
        message = 'Bonjour !'

    # Envoi de la longueur puis du message
    encoded = message.encode()
    s.sendall(len(encoded).to_bytes(4, 'big') + encoded)

    # Réception de la réponse (même protocole)
    raw_len = s.recv(4)
    reply_len = int.from_bytes(raw_len, 'big')
    reply = recv_all(s, reply_len)
    print(f'Reponse du serveur : {repr(reply)}')

    s.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Client/Serveur TCP avec input utilisateur')
    parser.add_argument('mode', choices=['server', 'client'])
    parser.add_argument('--host', default=DEFAULT_HOST)
    parser.add_argument('--port', type=int, default=DEFAULT_PORT)

    args = parser.parse_args()

    if args.mode == 'server':
        run_server(args.host, args.port)
    else:
        run_client(args.host, args.port)