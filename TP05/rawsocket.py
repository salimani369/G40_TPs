
import socket
from ipheader import create_ip_header 
from tcpheader import create_tcp_header

def create_packet(ip_header, tcp_header, message):
    return ip_header + tcp_header + message.encode()

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)

    ip_source = '127.0.0.1'
    ip_dest = '127.0.0.1'
    message = "Hello"

    ip_header = create_ip_header(ip_source, ip_dest)
    tcp_header = create_tcp_header(ip_source, ip_dest, message)

    packet = create_packet(ip_header, tcp_header, message)

    s.sendto(packet, (ip_dest, 0))
    print("Message envoyé")

    s.close()

if __name__ == "__main__":
    main()