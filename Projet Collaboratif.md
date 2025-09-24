# Gestionnaire de Bibliothèque Fantastique/SF

## **Objectif**
Développer ensemble un outil pour gérer une collection de livres (Fantasy/SF) lue depuis un fichier CSV.
L’objectif principal est de **s’entraîner à collaborer avec Git** (branches, commits, pull requests, résolution de conflits) tout en implémentant des fonctionnalités utiles.

**Approche** :
- Chaque membre choisit une ou plusieurs features à implémenter.
- Le groupe discute des choix de design (ex : comment gérer les livres incomplets, quel format d’affichage).
- Les solutions techniques sont laissées libres, mais il faut essayer de ne pas modifier directement la liste "livres".

---

## **Features à Développer**

| Feature                           | Objectif                                                                                   | Difficulté estimée |
| --------------------------------- | ------------------------------------------------------------------------------------------ | ------------------ |
| **Réferencement**                 | Permettre un accès rapide à un livre.                                                      | Facile             |
| **Filtrer les livres incomplets** | Identifier et filtrer les livres qui n’ont pas d’information sur leur nombre de pages.     | Facile             |
| **Ajouter un livre**              | Ajouter une nouvelle entrée à la collection.                                               | Facile             |
| **Supprimer un livre**            | Retirer une entrée de la collection et mettre à jour les références.                       | Moyenne            |
| **Trier les livres**              | Organiser la collection selon différents critères (titre, ISBN, etc.).                     | Moyenne            |
| **Rechercher un livre**           | Trouver un ou plusieurs livres selon des critères (titre, éditeur, genre, etc.).           | Moyenne            |
| **Formater l’affichage**          | Présenter les informations d’un livre ou de la collection de manière claire et lisible.    | Facile             |
| **Statistiques**                  | Calculer et afficher des informations sur la collection (ex : nombre de livres par genre). | Difficile          |
| **Recommandations**               | Proposer des livres similaires à un livre donné (même genre, même éditeur, etc.).          | Difficile          |

---

## **Workflow Collaboratif**
1. **Discussion initiale** :
   - Le groupe se met d’accord sur les choix de design (ex : comment gérer les livres incomplets, quel format pour l’affichage).
   - Chacun choisit une feature à implémenter.

2. **Développement** :
   - Chaque membre travaille sur sa feature dans sa propre branche.
   - Les commits doivent être clairs et atomiques, en utilisant le format **`<Type> (<Format>) : <Message>`**

3. **Intégration** :
   - Les contributions sont fusionnées via des pull requests, avec une relecture par un autre membre du groupe.

4. **Gestion des conflits** :
   - Les conflits de fusion sont résolus en équipe.

---

## **Exemple de Données**
La collection est une liste de livres, chaque livre étant représenté par un ensemble d’informations (titre, éditeur, genre, nombre de pages, etc.).
Le fichier CSV initial contient ces informations, et chaque feature doit permettre de les manipuler ou les afficher de manière utile.

---

## **Pour les Autres Groupes**
- **Fork du dépôt** : Les autres groupes peuvent fork le dépôt et travailler sur leur propre version.
- **Collaboration** : Les groupes peuvent s’inspirer mutuellement, ou même contribuer au dépôt original via des pull requests.

---

## **Questions pour le Groupe**
- Comment gérer les livres qui n’ont pas de nombre de pages ?
- Quel format d’affichage serait le plus utile pour visualiser un livre ou la collection ?
- Faut-il ajouter d’autres informations aux livres (ex : note, résumé) ?

---
**Prochaine étape** :
Ce document est une base de discussion. Le groupe peut l’adapter, ajouter ou supprimer des features, et définir ensemble les règles de design.

Lire un fichier CSV (livres fantasy)
Chaque livre est rentré dans un dictionnaire, qu'on ajoute a une liste de livres

- Créer un dictionnaire de référence, associant chaque index de la liste a un id de livre
- filtrer les doublons
- ajouter un livre a la liste
- enlever un livre de la liste (et donc update du dictionnaire de référence)
- trier les livres par nom, auteur, etc...
- rechercher un morceau
- Formater l'affichage d'un livre