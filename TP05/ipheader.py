from struct import pack
import socket


# création en tete IP
def create_ip_header(ip_source, ip_dest):
    ip_version = 4
    ip_ihl = 5
    ip_tos = 0
    ip_total_len = 0
    ip_id = 54321
    ip_frag_off = 0
    ip_ttl = 255
    ip_proto = socket.IPPROTO_TCP
    ip_check = 0

    ip_saddr = socket.inet_aton(ip_source)
    ip_daddr = socket.inet_aton(ip_dest)

    ip_ihl_ver = (ip_version << 4) + ip_ihl

    ip_header = pack('!BBHHHBBH4s4s',
        ip_ihl_ver, ip_tos, ip_total_len,
        ip_id, ip_frag_off,
        ip_ttl, ip_proto, ip_check,
        ip_saddr, ip_daddr)

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