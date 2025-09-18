[[Réseau]]

Il n'y a qu'**une seule arborescence** pour tous les lecteurs / disques / fichier systèmes.
Contrairement a Windows, Linux fait la **différenciation de la casse** sur les noms de fichiers et d'extension.
La **notion d'extension n'existe pas** sous Linux. Il ne sait ouvrir que les fichiers textes.

Il y'a trois grands types de fichiers sous Linux:
- *Répertoire*
- *Périphérique*
- *Normal*

Lorsque l'in fait un ls -l, cela afficher une liste longue des fichiers dans le dossier.
La première ligne contiens des informations:
- d'abord l ou d: **Link** (un raccourci) ou **Directory** (qui contient des fichiers)

Les fichiers cachés commencent par un point. On peut les afficher quand on liste avec l'option *-al*.

Les deux premiers fichiers quand on liste dans un répertoire sont:
- **.** : pointe vers les chemin absolu du dossier
- **..** : identifie le chemin absolu du dossier parent


