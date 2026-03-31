
import socket
from struct import pack

# Fonction checksum pour vérifier l'intégrité du paquet
def checksum(data):
    s = 0
    for i in range(0, len(data) - 1, 2):
        w = (data[i] << 8) + data[i + 1]
        s = s + w
    # si le nombre d'octets est impair on ajoute le dernier tout seul
    if len(data) % 2 != 0:
        s += data[-1] << 8
    # on replie les retenues sur 16 bits
    while s >> 16:
        s = (s & 0xFFFF) + (s >> 16)
    # complément à 1
    s = ~s & 0xFFFF
    return s

# Création de l'entête TCP
def create_tcp_header(ip_source, ip_dest, message):
    tcp_source = 1234  # port source du client
    tcp_dest = 80      # port destination du serveur
    tcp_seq = 454      # numéro de séquence
    tcp_ack_seq = 0    # numéro d'acquittement
    tcp_doff = 5       # taille de l'entête TCP (5 x 32 bits = 20 octets)

    tcp_flags = 2      # flag SYN/FIN selon usage
    tcp_window = socket.htons(5840)
    tcp_check = 0      # checksum, calculé après
    tcp_urg_ptr = 0    # pointeur urgent, non utilisé

    # regroupe offset et flags
    offset_res = (tcp_doff << 4)

    tcp_header = pack('!HHLLBBHHH',
                      tcp_source, tcp_dest,
                      tcp_seq, tcp_ack_seq,
                      offset_res, tcp_flags,
                      tcp_window, tcp_check, tcp_urg_ptr)

    # pseudo header pour le checksum
    source_address = socket.inet_aton(ip_source)
    dest_address = socket.inet_aton(ip_dest)
    placeholder = 0
    protocol = socket.IPPROTO_TCP
    tcp_length = len(tcp_header) + len(message)

    psh = pack('!4s4sBBH',
               source_address, dest_address,
               placeholder, protocol, tcp_length)
    psh = psh + tcp_header + message.encode()

    tcp_check = checksum(psh)

    tcp_header = pack('!HHLLBBH',
                      tcp_source, tcp_dest,
                      tcp_seq, tcp_ack_seq,
                      offset_res, tcp_flags,
                      tcp_window) + pack('H', tcp_check) + pack('!H', tcp_urg_ptr)

    return tcp_header

