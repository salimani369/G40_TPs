METHODES_VALIDES = ["GET", "POST", "PUT", "DELETE", "HEAD"]

def format_requete_http(methode, url, version, entetes, body):
    
    # vérification de la méthode
    if methode not in METHODES_VALIDES:
        print("Erreur : méthode invalide")
        return

    # vérification de la version
    if version == 1:
        version_str = "HTTP/1.1"
    elif version == 2:
        version_str = "HTTP/2.0"
    else:
        print("Erreur : version invalide")
        return

    # première ligne
    requete = methode + " " + url + " " + version_str + "\r\n"

    # ajout des en-têtes
    for nom, valeur in entetes.items():
        requete = requete + nom + ": " + valeur + "\r\n"

    # ligne vide + body
    requete = requete + "\r\n" + body

    return requete


# test
entetes = {
    "Host": "localhost:8000",
    "User-Agent": "Mozilla/5.0",
    "Accept": "text/html"
}

resultat = format_requete_http("GET", "/index.html", 1, entetes, "")
print(resultat)
