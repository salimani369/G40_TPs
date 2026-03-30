import socket


"""hote = "127.0.0.1" # Adresse IP du serveur
port = 10600      # Port du serveur

#message XML (format string)
message_xml = <client>
    <nom>client1</nom>
    <date_connexion>19/04/2021</date_connexion>
    <lieu>Paris</lieu>
</client>

#connexion et envoi
try:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((hote, port))
    
    #envoi message encodé en UTF-8
    client_socket.send(message_xml.encode('utf-8'))
    
    print("Message XML envoyé avec succès !")
    client_socket.close()""" 


"""
import xml.etree.ElementTree as ET

# définition de la chaîne XML avec les triples guillemets pour éviter les erreurs de syntaxe
client_str = 
<client>
    <nom>client1</nom>
    <date_connexion>19/04/2021</date_connexion>
    <lieu>Paris</lieu>
</client>


# transformation de la chaîne en arbre XML
root = ET.fromstring(client_str)

print(root.tag)         # devrait afficher client
print(len(root))        # devrait afficher 3
print(root[0].tag)      # devrait afficher nom
print(root[0].text)     # devrait afficher client1
print(root[1].tag)      # devriat afficher date_connexion
print(root[1].text)     # devrait afficher: 19/04/2021

print("Nom du client : " + root[0].text)
print("Lieu de connexion : " + root[2].text)"""

###changez dans le code du client et du serveur afin de supporter ces différents type de messages

"""<identification>
    <nom>client</nom>
    <date_connexion>date</date_connexion>
    <lieu>lieu</lieu>
</identification>

<notification>
    <type>connexion</type>
    <client>nom_client</client>
</notification>


<notification>
    <type>nb_clients</type>
    <nombre>0</nombre>
</notification>

<notification>
    <type>ecriture</type>
    <client>nom_client</client>
</notification>

<etat>
    <client>nom_client</client>
    <statut>LIBRE</statut>
</etat>"""

#######message d’identification : le client, au moment de sa connexion, envoie un message au serveur afin de s’identifier en lui présentant#####
##son nom, sa date de connexion ainsi que son lieu de connexion
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 12345))

message1 = """
<identification>
    <nom>client1</nom>
    <date_connexion>03/30/2026</date_connexion>
    <lieu>Paris</lieu>
</identification>
"""

# notification
message2 = """
<notification>
    <type>connexion</type>
    <client>client</client>
</notification>
"""

# etat
message3 = """
<etat>
    <client>client</client>
    <statut>LIBRE</statut>
</etat>
"""

client.send(message1.encode())
client.close()


