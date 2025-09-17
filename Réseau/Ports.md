[[IP]]
[[Serveurs]]

### Configuration d'un serveur dans un réseau local

HTTP utilise le port ==80==, HTTPS utilise le port ==443==.
Lorsqu'un routeur reçoit des requêtes non demandées de l'extérieur, il peut rediriger la requête vers le serveur dans le réseau local si les ports correspondants sont ouverts.
Cela représente néanmoins un danger pour le réseau local; on crée donc une **DMZ** (zone démilitarisée) en isolant le serveur du reste du réseau, afin de pouvoir couper cette partie du réseau en cas d'attaque.