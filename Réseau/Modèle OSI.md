[[Réseau]]

Le **modèle OSI** ( Open Systems Interconnection ) est une [norme](https://fr.wikipedia.org/wiki/Norme_et_standard_techniques "Norme et standard techniques") de communication de tous les systèmes informatiques en réseau. L'objectif de cette norme est de spécifier un cadre général pour la création de normes ultérieures cohérentes. Le modèle lui-même ne définit pas de service particulier ni de protocole.

### Concept

Le modèle est essentiellement une architecture en couches définies et délimitées avec les notions de service, de [protocole](https://fr.wikipedia.org/wiki/Protocole_de_communication "Protocole de communication") et d'[interface](https://fr.wikipedia.org/wiki/Interface_\(informatique\) "Interface (informatique)").

- Un service est une description abstraite de fonctionnalités à l'aide de primitives (commandes ou événements) telles que demande de connexion ou réception de données.
- Un protocole est un ensemble de messages et de règles d'échange réalisant un service.
- Une interface (« point d'accès au service » dans la norme) est le moyen concret d'utiliser le service. Dans un programme, c'est typiquement un ensemble de fonctions de [bibliothèque](https://fr.wikipedia.org/wiki/Biblioth%C3%A8que_logicielle "Bibliothèque logicielle") ou d'[appels systèmes](https://fr.wikipedia.org/wiki/Appel_syst%C3%A8me "Appel système"). Dans une réalisation matérielle, c'est par exemple un [jeu de registres](https://fr.wikipedia.org/wiki/Registre_de_processeur "Registre de processeur") à l'entrée d'un circuit.


### Couches


![[OSI_Model_.png]]

Les trois couches inférieures sont plutôt orientées communication et sont souvent fournies par un [système d'exploitation](https://fr.wikipedia.org/wiki/Syst%C3%A8me_d%27exploitation "Système d'exploitation") et par le matériel. C'est le domaine des techniciens réseau.

Les quatre couches supérieures sont plutôt orientées [application](https://fr.wikipedia.org/wiki/Application_\(informatique\) "Application (informatique)") et plutôt réalisées par des bibliothèques ou un programme spécifique. C'est le domaine des développeurs.

On  transmet les informations dans la **couche physique** grâce a trois supports: 
- Cable (électricité)
- Fibre optique (lumière)
- Sans-fil (ondes électromagnétique)

## Modèle TCP/IP

Les trois couches supérieurs sont regroupées dans une couche Application. Transport et Réseau ont leur propres couches, et Liaison et Physique sont regroupées. Toutefois, plus récemment, on a tendance a séparer les couches Liaisons et Physiques, car elles dépendent de différents corps de métier.
