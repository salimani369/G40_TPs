"""def ecrire_message(message):
    print(message)


if __name__ == '__main__':
    ecrire_message('mon premier script')"""


import http.client
import socket 

"""
def connect_to_google():
   path = ('/maps/geo?g=207+N.+Defiance+St%2C+Archbold%2C+OHoutput=json&oe=utf8')
   connection = http.client.HTTPConnection('maps.google.com')
   connection.request('GET', path)
   rawreply = connection.getresponse().read()
   print(rawreply)

if __name__ == '__main__':
    connect_to_google() 
"""

"""
def connect_to_google():  #fonction qui établit une connexion au serveur google pour récupérer une page web
    sock = socket.socket()   #création d'un socket TCP 
    sock.connect(('maps.google.com', 80))   #connexion au serveur maps.google.com sur le port TCP 80 
    sock.sendall(                   #Erreur détéctée à ce niveau là: a bytes-like object is required not 'str' ==> besoin d'un encodage utf-8
        'GET /maps/geo?q=207+N.+Defiance+St%2C+Archbold%2C+OH'  #HTTP get request pour récupérer la page google maps spécifié ici
        '&output=json&oe=utf8&sensor=false HTTP/1.1\r\n'      #ici on voit la version du protocole http
        'Host: maps.google.com:80\r\n'  #indique le serveur cible
        'User-Agent: search4.py\r\n'     #identifie mon programme auprès du serveur google maps
        'Connection: close\r\n'       #demande à ce que cette connexion soit fermée après réponse 
        '\r\n'
    )

    rawreply = sock.recv(4096)  #la socket reçoit les données et recv permet de lire le buffer de réception qui a pour capaxité max 4096 
    print(rawreply) #affiche ce qu'a lu recv sur le biffer 

if __name__ == '__main__':  #point d'entrée du programme. 
    connect_to_google()  #exécution de la fct qui permet d'établir une connexion 
"""

"""
def connect_to_google():  
    sock = socket.socket()
    sock.connect(('maps.google.com', 80))
    
    requete = (      #je crée une nouvelle variable dans laquelle je mets l'URL afin de faciliter l'encodage(que tous les caractères soient dedans)
        'GET /maps/geo?q=207+N.+Defiance+St%2C+Archbold%2C+OH'
        '&output=json&oe=utf8&sensor=false HTTP/1.1\r\n'
        'Host: maps.google.com:80\r\n'
        'User-Agent: search4.py\r\n'
        'Connection: close\r\n'
        '\r\n'
    )

    sock.sendall(requete.encode("utf-8"))

    rawreply = sock.recv(4096)
    print(rawreply)

if __name__ == '__main__':
    connect_to_google()

"""