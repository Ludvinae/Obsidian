[[IP]]

**Domain Name System**
On peut aussi parler de DNS (server) qui fait tourner un DNS (service) pour fournir des adresses IP grâce au DNS (system).
C'est le système le plus sécurisé du monde, qui fourni les adresses IP en fonction du nom de domaine.

Lorsqu'on tape une adresse web dans notre navigateur, notre ordinateur va émettre une requête au *DNS local* si il connait l'adresse IP du domaine recherché. Si il ne la connait pas, l'ordinateur va demander au *DNS du FAI*, puis en dernier recours il interrogera le *DNS mondial*.

La requête DNS va se faire avec le protocole UDP (pas de failsafe) sur le port 53. Elle va être envoyée sur les serveurs **DNS racines**, qui enregistrent toutes les adresses des serveurs **DNS d'autorité**. Puis le DNS racine nous redirige vers le DNS qui a autorité sur le domaine demandé, selon que ce soit une adresse en *.com*, en *.fr* ou autre. C'est ce serveur d'autorité qui va ensuite transmettre l'adresse IP du site que l'on essaye d'afficher.

Les DNS gèrent aussi les adresses des serveur mails.

On peut aussi demander le nom de domaine en fonction de l'adresse IP. Dans ce cas, on parle de **résolution inverse**.

Les extensions de noms de domaines sont généralement un de ces types:
- Extension géographique (.fr, .eu, .alsace, etc...)
- Extension thématique (.org, .net, .gov, etc...)