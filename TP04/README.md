1. Format XML (Extensible Markup Language)Structure : Inspiré du HTML, le XML repose sur des balises ouvrantes et fermantes (<tag>...</tag>) entourant une valeur.
- Analyse en Python : L'utilisation de la bibliothèque xml.etree.ElementTree permet de transformer une chaîne de caractères (string) en un objet "arbre" (ElementTree).
- Manipulation du code :La fonction ET.fromstring(client_str) convertit le texte brut en données structurées.L'accès aux données s'effectue par l'indexation des éléments enfants de la racine (ex: root[0] pour le premier élément).
2. Le Format JSON (JavaScript Object Notation) Ce format est privilégié pour sa légèreté par rapport au XML, car il réduit la quantité de métadonnées descriptives au profit de la donnée utile.
- Structure : Il organise les informations sous forme de paires Clé / Valeur.
- Analyse en Python : Le module json permet une intégration directe avec les types de données natifs de Python.
- Manipulation du code :La méthode json.loads(client_str) transforme la chaîne JSON en un dictionnaire Python.L'accès aux valeurs est plus explicite que le XML, utilisant le nom de la clé (ex: client['nom']).

L'implémentation logicielle définit un protocole de communication pour une application de chat basé sur plusieurs types de messages:
-Identification : Message envoyé lors de la connexion contenant le nom, la date_connexion et le lieu. 
-Notification : Utilisé pour signaler des événements comme le nombre de clients connectés, les arrivées/départs ou l'état d'écriture d'un utilisateur.
-État : Permet de diffuser le statut actuel du client (LIBRE, OCCUPÉ, INACTIF).


3. Algorithmes :
L'algorithme de conversion vers les nombres romains repose sur une approche qui décompose un entier en une chaîne de caractères structurée. En utilisant une liste de correspondances triée par ordre décroissant, le programme soustrait successivement la plus grande valeur possible du nombre initial tout en concaténant le symbole associé au résultat final. Pour garantir le respect de la notation moderne et éviter les répétitions excessives (comme "IIII"), des formes soustractives spécifiques telles que 900 (CM), 40 (XL) ou 4 (IV) sont intégrées directement dans le référentiel de données. À l'inverse, l'algorithme de décodage analyse la position relative des symboles pour déterminer s'il doit additionner ou soustraire leur valeur au total selon que le chiffre actuel est supérieur ou inférieur au suivant.