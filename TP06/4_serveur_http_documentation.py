from http.server import HTTPServer, BaseHTTPRequestHandler
 
PAGE_INDEX = """<!DOCTYPE html>
<html>
<body>
<p>Bonjour</p>
<p style="font-size:50px;">C'est notre premier serveur</p>
</body>
</html>"""
 
PAGE_404 = """<html>
<body>
<h1>404 Not Found</h1>
</body>
</html>"""
 
 
class MonServeur(BaseHTTPRequestHandler):
 
    def do_GET(self):
        if self.path == "/index.html":
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write(PAGE_INDEX.encode("utf-8"))
        else:
            self.send_response(404)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write(PAGE_404.encode("utf-8"))
 
 
# Démarrer le serveur
serveur = HTTPServer(("", 8000), MonServeur)
print("Serveur démarré sur http://localhost:8000")
print("Testez : http://localhost:8000/index.html")
serveur.serve_forever()