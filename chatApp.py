"""
Application de chat TCP
-----------------------
Lance le serveur :  python chat_tcp.py server
Lance un client :   python chat_tcp.py client

Le serveur attend une connexion, puis les deux côtés
s'envoient des messages à tour de rôle jusqu'à ce que
l'un d'eux tape 'quit'.

Pourquoi TCP plutôt qu'UDP pour un chat ?
- TCP garantit que les messages arrivent dans l'ordre
- TCP garantit qu'aucun message ne se perd
- La connexion persistante est plus adaptée à une session de chat
"""

import socket
import argparse
import sys

HOST = '127.0.0.1'
PORT = 1060


def send_msg(sock, message):
    """Envoie un message précédé de sa longueur sur 4 octets."""
    encoded = message.encode()
    sock.sendall(len(encoded).to_bytes(4, 'big') + encoded)


def recv_msg(sock):
    """Reçoit un message précédé de sa longueur."""
    raw_len = sock.recv(4)
    if not raw_len:
        return None
    msg_len = int.from_bytes(raw_len, 'big')
    data = b''
    while len(data) < msg_len:
        chunk = sock.recv(msg_len - len(data))
        if not chunk:
            return None
        data += chunk
    return data.decode()


def chat_loop(sock, my_name, first_to_speak):
    """Boucle de chat : on parle en alternance."""
    if first_to_speak:
        while True:
            msg = input(f'[{my_name}] > ').strip()
            if not msg:
                continue
            send_msg(sock, msg)
            if msg.lower() == 'quit':
                print('Fin de la conversation.')
                break
            received = recv_msg(sock)
            if received is None or received.lower() == 'quit':
                print("L'autre cote a ferme la connexion.")
                break
            print(f'[Interlocuteur] > {received}')
    else:
        while True:
            received = recv_msg(sock)
            if received is None or received.lower() == 'quit':
                print("L'autre cote a ferme la connexion.")
                break
            print(f'[Interlocuteur] > {received}')
            msg = input(f'[{my_name}] > ').strip()
            if not msg:
                continue
            send_msg(sock, msg)
            if msg.lower() == 'quit':
                print('Fin de la conversation.')
                break


def run_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(1)
    print(f'Serveur en attente sur {HOST}:{PORT}...')
    print("(tapez 'quit' pour terminer)\n")

    sc, addr = s.accept()
    print(f'Client connecte depuis {addr}\n')

    chat_loop(sc, my_name='Serveur', first_to_speak=False)

    sc.close()
    s.close()


def run_client():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    print(f'Connecte au serveur {HOST}:{PORT}')
    print("(tapez 'quit' pour terminer)\n")

    chat_loop(s, my_name='Client', first_to_speak=True)

    s.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Chat TCP')
    parser.add_argument('mode', choices=['server', 'client'])
    args = parser.parse_args()

    if args.mode == 'server':
        run_server()
    else:
        run_client()