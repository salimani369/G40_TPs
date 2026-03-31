import socket
from ipheader import create_ip_header
from tcpheader import create_tcp_header

def create_packet(ip_header, tcp_header, data):
    return ip_header + tcp_header + data.encode()

def main():
    message = 'Bonjour, je suis un nouveau client'

    while True:
        # reconstruction du paquet avec le nouveau message
        ip_header  = create_ip_header(ip_source, ip_dest)
        tcp_header = create_tcp_header(ip_source, ip_dest, message)
        packet     = create_packet(ip_header, tcp_header, message)

        # envoi du paquet
        s.sendto(packet, (ip_dest, 0))
        print('Message envoyé :', message)

        # demande à l'utilisateur s'il veut continuer
        ans = input('Voulez-vous continuer ? (y/n) ')
        if ans.lower() == 'y':
            message = input('Entrez le nouveau message : ')
            continue
        else:
            break

    s.close()

if __name__ == '__main__':
    # création d'une raw socket
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
    ip_source = '127.0.0.1'
    ip_dest   = '127.0.0.1'

    main()