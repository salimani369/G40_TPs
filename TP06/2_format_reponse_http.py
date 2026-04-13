def format_reponse_http(version_str, status_code, status_info, entetes, body):
 
    # Première ligne
    reponse = version_str + " " + str(status_code) + " " + status_info + "\r\n"
 
    # Ajout des en-têtes
    for nom, valeur in entetes.items():
        reponse = reponse + nom + ": " + valeur + "\r\n"
 
    # Ligne vide + body
    reponse = reponse + "\r\n" + body
 
    return reponse
 
 
# --- Test ---
entetes = {
    "Server": "PythonTPServer",
    "Connection": "Closed"
}
 
body = "<html><body><h1>404 Not Found</h1></body></html>"
 
resultat = format_reponse_http("HTTP/1.1", 404, "Not Found", entetes, body)
print(resultat)