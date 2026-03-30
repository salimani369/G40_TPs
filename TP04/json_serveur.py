import socket
import json

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Option pour relancer le serveur sans attendre
server.bind(("0.0.0.0", 18000))
server.listen(5)

print("Serveur en attente sur le port 18000...")

while True: # Boucle pour accepter plusieurs clients successivement
    conn, addr = server.accept()
    print(f"Connexion de {addr}")

    try:
        data = conn.recv(1024)
        if data:
            # On décode et on enlève les espaces vides autour
            raw_data = data.decode().strip()
            
            # Si jamais il y a plusieurs messages collés, on prend le premier
            # (Solution de secours pour l'exercice)
            if "}{" in raw_data:
                raw_data = raw_data.split("}{")[0] + "}"

            message = json.loads(raw_data)

            if message.get("type") == "identification":
                print("Identification :")
                # Utilise .get() pour éviter de planter si une clé manque
                print(f"Nom: {message.get('nom')}, Date: {message.get('date_connexion')}, Lieu: {message.get('lieu')}")

            elif message.get("type") == "notification":
                print("Notification :")
                print(message.get("event"), message.get("client"), message.get("nombre"))

            elif message.get("type") == "etat":
                print("Etat :")
                print(message.get("client"), message.get("etat"))
                
    except json.JSONDecodeError as e:
        print(f"Erreur de lecture JSON : {e}")
    except Exception as e:
        print(f"Erreur : {e}")
    finally:
        conn.close() # On ferme la connexion après avoir traité le message