import socket
import xml.etree.ElementTree as ET

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 12345))
server.listen(5)

conn, addr = server.accept()

while True:
    data = conn.recv(1024)
    if not data:
        break

    root = ET.fromstring(data.decode())

    # 🔹 Détection du type de message
    if root.tag == "identification":
        nom = root.find("nom").text
        date = root.find("date_connexion").text
        lieu = root.find("lieu").text

        print("Identification :", nom, date, lieu)

    elif root.tag == "notification":
        type_notif = root.find("type").text
        client_nom = root.find("client").text if root.find("client") is not None else None

        print("Notification :", type_notif, client_nom)

    elif root.tag == "etat":
        client_nom = root.find("client").text
        statut = root.find("statut").text

        print("Etat :", client_nom, statut)

conn.close()