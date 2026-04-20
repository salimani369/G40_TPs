from struct import pack
import socket


# ce fichier contient juste la fonction qui construit l'entete IP
# on l'a mis a part pour pouvoir l'importer dans tous les clients


def create_ip_header(ip_source, ip_dest):
 
    ip_version   = 4        # on est en IPv4
    ip_ihl       = 5        # taille standard de l'entete IP (5 x 32 bits = 20 octets)
    ip_tos       = 0        # type of service on met 0 c'est la valeur normale
    ip_total_len = 0        # on laisse a 0 l'OS calcule tout seul
    ip_id        = 54321    # un identifiant pour le paquet, on met ce qu'on veut
    ip_frag_off  = 0        # pas de fragmentation
    ip_ttl       = 255      # time to live : combien de routeurs le paquet peut traverser
    ip_proto     = socket.IPPROTO_TCP   # on utilise TCP
    ip_check     = 0       
    ip_saddr     = socket.inet_aton(ip_source)  # adresse source en bytes
    ip_daddr     = socket.inet_aton(ip_dest)    # adresse destination en bytes
 
    # on combine la version et la taille de l'entete sur un seul octet
    ip_ihl_ver = (ip_version << 4) + ip_ihl
 
    # pack met tous les champs dans le bon format binaire
    # le ! veut dire big-endian (ordre reseau)
    ip_header = pack('!BBHHHBBH4s4s',
        ip_ihl_ver,
        ip_tos,
        ip_total_len,
        ip_id,
        ip_frag_off,
        ip_ttl,
        ip_proto,
        ip_check,
        ip_saddr,
        ip_daddr)
 
    return ip_header

# checksum IP
def checksum(data):
    s = 0
    for i in range(0, len(data), 2):
        if i + 1 < len(data):
            w = (data[i] << 8) + data[i + 1]
        else:
            w = (data[i] << 8)
        s += w

    while s >> 16:
        s = (s & 0xFFFF) + (s >> 16)

    return ~s & 0xFFFF