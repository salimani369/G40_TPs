import socket
from datetime import datetime
from ipheader import create_ip_header
from tcpheader import create_tcp_header

MAX_BYTES = 65535

def create_packet(ip_header, tcp_header, data):
    # simple concaténation des headers et des données
    return ip_header + tcp_header + data.encode()

def client(port):
    text = 'Le temps est {}'.format(datetime.now())

    ip_header  = create_ip_header(ip_source, ip_dest)
    tcp_header = create_tcp_header(ip_source, ip_dest, text)
    packet     = create_packet(ip_header, tcp_header, text)

    s.sendto(packet, (ip_dest, 0))
    print('mon adresse est {}'.format(s.getsockname()))

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
    ip_source = '127.0.0.1'
    ip_dest   = '127.0.0.1'

    client(1060)