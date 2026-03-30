import socket
import json 

"""hote = "127.0.0.1"
port = 10600

# création des données sous forme de dictionnaire Python
donnees = {
    "nom": "client1",
    "date_connexion": "19/04/2021",
    "lieu": "Paris"
}

# conversion du dictionnaire en chaîne JSON (string)
message_json = json.dumps(donnees)

# Connexion et envoi
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((hote, port))
    
    # Envoi du message encodé en octets
    s.send(message_json.encode('utf-8'))
    
    print("Message JSON envoyé !")
    """
"""
import json

# définition de la chaîne JSON 
client_str = """
{
    "nom": "client1",
    "date_connexion": "19/04/2021",
    "lieu": "Paris"
}
"""

# transformation de la chaîne JSON en dictionnaire Python json.loads (load string) permet de lire le texte
client = json.loads(client_str)

print(client['nom'])            # Affiche : client1
print(client['date_connexion']) # Affiche : 19/04/2021
print(client['lieu'])           # Affiche : Paris


# afficher le nom du client et son lieu de connexion
print("Nom du client : " + client['nom'])
print("Lieu de connexion : " + client['lieu'])"""

import socket
import json

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 18000))

# Identification
message1 = {
    "type": "identification",
    "nom": "client1",
    "date_connexion": "30/03/2026",
    "lieu": "Paris"
}
client.send(json.dumps(message1).encode())

# Notification (connexion)
message2 = {
    "type": "notification",
    "event": "connexion",
    "client": "client"
}
client.send(json.dumps(message2).encode())

# Etat
message3 = {
    "type": "etat",
    "client": "client",
    "etat": "LIBRE"
}
client.send(json.dumps(message3).encode())

client.close()
