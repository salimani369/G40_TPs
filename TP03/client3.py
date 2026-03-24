import socket
import socket
import threading
from _thread import *
import threading 


"""
def main():
    host = '127.0.0.1'
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    message = 'Bonjour, je suis un nouveau client'
    while True:
        s.send(message.encode('ascii'))
        data = s.recv(1024)
        print('message recu du serveur : ', str(data))
        ans = input('voulez vous continuer ?')
        if ans == 'y':
            continue
        else:
            break

    s.close()

if __name__ == '__main__':
    main()"""

##########code modifié pour ###################


import socket
import threading

HOST, PORT = "127.0.0.1", 1080

def receive_messages(conn):
    while True:
        try:
            # Affiche le message reçu et réaffiche l'invite de commande
            print(f"\n{conn.recv(1024).decode()}\nMessage (dest|texte) : ", end="")
        except:
            print("\n[DECONNEXION] Serveur perdu.")
            break

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((HOST, PORT))
    except:
        return print("Impossible de se connecter au serveur.")

    name = input("Votre nom : ")
    client.send(name.encode())

    # Lancement du thread de réception
    threading.Thread(target=receive_messages, args=(client,), daemon=True).start()

    print("Format d'envoi : destinataire|message (ou 'exit' pour quitter)")
    
    while True:
        # On demande une seule chaîne pour ne pas bloquer le terminal deux fois
        msg_send = input("Message (dest|texte) : ")
        
        if msg_send.lower() == "exit":
            break
            
        if "|" in msg_send:
            client.send(msg_send.encode())
        else:
            print("Erreur format : utilise 'Nom|Message'")

    client.close()

if __name__ == "__main__":
    start_client()