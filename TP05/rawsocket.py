import socket
import tcpheader


if __name__ == '__main__':
    # creation d'une raw socket
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
    ip_source = '127.0.0.1'
    ip_dest = '127.0.0.1'
    message = 'Hello, how are you'

    ip_header = create_ip_header(ip_source, ip_dest)
    tcp_header = create_tcp_header(message, ip_source, ip_dest)

    packet = create_packet(ip_header, tcp_header, message)

    s.sendto(packet, (ip_dest , 0 ))