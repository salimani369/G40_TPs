1. oui, on peut utiliser le polymorphisme à ce niveau du TP.
En regardant les deux classes Serveur et Client, on remarque que recv_all est identique dans les deux. On peut donc créer une classe mère SocketBase qui contient recv_all une seule fois, et faire hériter Serveur et Client de cette classe :
class SocketBase(ABC):
    def recv_all(self, sock, length):  
        ...
    @abstractmethod
    def demarrer(self):  

class Serveur(SocketBase):
    def demarrer(self):
        ...

class Client(SocketBase):
    def demarrer(self):
        ...
même ligne de code mais comportement différent selon l'objet :
pythonnode = Serveur(...)  # ou Client(...)
node.demarrer()      
Si node est un Serveur, il écoute. Si node est un client, il se connecte. 
C'est là qu'on voit le polymorphisme : même appel maiscomportement différent.



Application de chat TCP

Le serveur attend une connexion, puis les deux côtés
s'envoient des messages à tour de rôle jusqu'à ce que
l'un d'eux tape 'quit'.

tcp est lieux adapté car :
- TCP garantit que les messages arrivent dans l'ordre
- TCP garantit qu'aucun message ne se perd
- La connexion persistante est plus adaptée à une session de chat
