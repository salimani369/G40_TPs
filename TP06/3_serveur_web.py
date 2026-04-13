import socket
 
PAGE_INDEX = """<!DOCTYPE html>
<html>
<body>
<p>Bonjour</p>
<p style="font-size:50px;">Moi c'est Sarah et c'est notre premier serveur</p>
</body>
</html>"""
 
PAGE_404 = """<html>
<body>
<h1>404 Not Found</h1>
</body>
</html>"""
 
 
# Création du socket
serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serveur.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serveur.bind(("", 8080))
serveur.listen(5)
print("Serveur démarré sur le port 8080...")
 
while True:
    # Attendre une connexion
    client, adresse = serveur.accept()
    print("Connexion de", adresse)
 
    # Lire la requête
    donnees = client.recv(4096).decode("utf-8")
 
    # Récupérer la première ligne (ex: "GET /index.html HTTP/1.1")
    premiere_ligne = donnees.split("\r\n")[0]
    parties = premiere_ligne.split(" ")
    methode = parties[0]
    url = parties[1]
 
    # Choisir la bonne réponse
    if methode == "GET" and url == "/index.html":
        reponse = "HTTP/1.1 200 OK\r\n"
        reponse = reponse + "Content-Type: text/html\r\n"
        reponse = reponse + "\r\n"
        reponse = reponse + PAGE_INDEX
    else:
        reponse = "HTTP/1.1 404 Not Found\r\n"
        reponse = reponse + "Content-Type: text/html\r\n"
        reponse = reponse + "\r\n"
        reponse = reponse + PAGE_404
 
    # Envoyer la réponse
    client.send(reponse.encode("utf-8"))
    client.close()