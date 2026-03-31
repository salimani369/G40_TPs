
import socket 
import sys 
import time 
from struct import *

def create_tcp_header(ip_source, ip_dest, message):
    tcp_source = 1234
    tcp_dest = 80
    tcp_seq = 454
    tcp_ack_seq = 0
    tcp_doff = 5

    tcp_flags = 2  
    tcp_window = socket.htons(5840)
    tcp_check = 0
    tcp_urg_ptr = 0

    offset_res = (tcp_doff << 4)

    tcp_header = pack('!HHLLBBHHH',
        tcp_source, tcp_dest,
        tcp_seq, tcp_ack_seq,
        offset_res, tcp_flags,
        tcp_window, tcp_check, tcp_urg_ptr)

    # pseudo header
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

