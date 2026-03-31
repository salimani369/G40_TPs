import socket
import json
import xml.etree.ElementTree as ET
from ipheader import create_ip_header
from tcpheader import create_tcp_header

def create_packet(ip_header, tcp_header, data):
    return ip_header + tcp_header + data.encode()

def envoyer(message):
    # construction du paquet et envoi
    ip_header  = create_ip_header(ip_source, ip_dest)
    tcp_header = create_tcp_header(ip_source, ip_dest, message)
    packet     = create_packet(ip_header, tcp_header, message)
    s.sendto(packet, (ip_dest, 0))

def main():

    # ---- message d'identification en XML ----
    message_xml = """
<client>
    <nom>client1</nom>
    <date_connexion>31/03/2026</date_connexion>
    <lieu>Paris</lieu>
</client>"""

    envoyer(message_xml)
    print('message XML envoyé')

    # lecture et vérification du XML
    root = ET.fromstring(message_xml)
    print(root.tag)
    for child in root:
        print(child.tag, child.text)

    # ---- message d'identification en JSON ----
    client_str = """
{
    "nom": "client1",
    "date_connexion": "31/03/2026",
    "lieu": "Paris"
}"""

    envoyer(client_str)
    print('message JSON envoyé')

    # lecture et vérification du JSON
    client = json.loads(client_str)
    print(client['nom'])
    print(client['date_connexion'])
    print(client['lieu'])

    # ---- boucle de chat TP3 ----
    message = 'Bonjour, je suis un nouveau client'
    while True:
        envoyer(message)
        print('message envoyé :', message)

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