[[Versioning]]

Logiciel de versioning, qui permet de gérer plusieurs déploiements de la même application.
Cela permet aussi de revenir en arrière lorsque l'on casse des choses dans le code, et de travailler de manière collaborative.

Git est **décentralisé**. Il permet un travail flexible, parallèle et indépendant, avec une gestion efficace des fusions et de l'historique.
Son ancêtre est SVN (Subversion), qui était quant à lui centralisé. Il est encore utilisé dans certaines entreprises mais pose plus de contraintes que Git.
Git a été crée par Linus Torvald. pour le développement du noyau de Linux.

Git est le protocole, alors que GitHub est la plateforme d'hébergement de dépôts Git. 

### Termes importants

- **Repository**: un dépôt où tout le code et l'historique des versions sont stockés.
- **Commit**: un enregistrement de changements apportés au code dans le dépôt.
- **Tag**: un marqueur utilisé pour identifier des points spécifiques de l'historique .
- **Branche**: une version parallèle du projet permettant de travailler sur des fonctionnalités ou des corrections sans affecter le code.
- **Merge**: action de fusionner les modifications de deux branches différentes dans une seule.
- **Rebase**: Change le point de départ d'une branche pour récupérer les commit qui ont été ajoutés entre temps pour éviter d'avoir trop de retard.


#### Initialiser un repository

Créer un repository en local
`git init`

#### Cloner un repository

Récupérer un repository de Github vers sa machine
`git clone git@github.com:user/repository.git`

### Etats d'un fichier dans Git

- **Untracked**: fichier existe mais pas encore suivi par Git
- **Modified**: fichier suivi mais modifié depuis le dernier commit
- **Staged**: prêt a être enregistré dans l'historique
- **Committed**: officiellement enregistré dans l'historique local
- **Pushed**: Commit envoyé vers Github

#### Ignorer des fichiers

On peut ignorer certains fichiers qui peuvent comprendre des informations sensibles, des dépendances, des fichiers de configuration, etc...
-> Générateur de .gitignore: www.gitignore.io

### Workflow

- **gitflow**: une branche par environnement. Une version pour un environnement de production (Main), un environnement de développement, un environnement pour travailler sur des nouvelles features, etc...
- **Githubflow**: on a que deux environnement, un Main et une branche Feature. Des releases plus petites, plus fréquentes. La distance entre développement et production est réduite.
- **Trunk based**: moins utilisé, tout le monde travaille sur la branche Main, et quand une version est prête pour la production on crée une branche Release.

### Convention de commit

```ad-info
**`git commit -m "message"`**
```

Comment formaliser les messages de commit:
- Un commit = une idée
- Jamais de commit "fourre-tout"
- Limiter la taille du commit a 10-15 fichiers maximum
- Privilégier les commits dits "atomiques" (peu de modifications)
- Commits fréquents = historique lisible 

##### Conventional Commits
Standardise la manière d'écrire le messages de commit

```ad-important
`<type>(<scope>): <message>`
```

**Types**:
- feat: nouvelle fonctionnalité
- fix
- refactor
- docs
- test
- chore
- style

**Scope**:
Précisé le scope dans le message de commit est *optionnel*
- auth
- users
- payment

**Message**:
Le message doit être en anglais, clair, concis mais compréhensible.

