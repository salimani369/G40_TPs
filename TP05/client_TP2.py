import socket
from ipheader import create_ip_header
from tcpheader import create_tcp_header

HOST = '127.0.0.1'
PORT = 1060

def create_packet(ip_header, tcp_header, data):
    return ip_header + tcp_header + data.encode()

def recv_all(sock, length):
    # lit exactement le nombre d'octets demandés
    data = b''
    while len(data) < length:
        more = sock.recv(length - len(data))
        if not more:
            raise EOFError('la socket a été fermée')
        data += more
    return data

def client():
    print('Connexion au serveur {}:{}'.format(ip_dest, PORT))

    text = 'Bonjour !'

    # construction du paquet
    ip_header  = create_ip_header(ip_source, ip_dest)
    tcp_header = create_tcp_header(ip_source, ip_dest, text)
    packet     = create_packet(ip_header, tcp_header, text)

    # envoi du paquet
    s.sendto(packet, (ip_dest, 0))
    print('Paquet envoyé !')

if __name__ == '__main__':
    # création d'une raw socket
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
    ip_source = '127.0.0.1'
    ip_dest   = '127.0.0.1'

    client()