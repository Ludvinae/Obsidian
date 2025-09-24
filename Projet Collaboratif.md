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
*Cette liste est uniquement à titre indicatif pour pouvoir commencer le projet, n'hésitez pas à proposer vos idées au groupe*

---

## **Workflow Collaboratif**
1. **Discussion initiale** :
   - Le groupe se met d’accord sur les choix de design (ex : comment gérer les livres incomplets, quel format pour l’affichage).
   - Chacun choisit une feature à implémenter.

2. **Développement** :
   - Chaque membre travaille sur sa feature dans sa propre branche.
   - Les commits doivent être clairs et atomiques, en utilisant le format **`<Type> (<Format>) : <Message>`**

3. **Intégration** :
   - Les contributions sont fusionnées via des pull requests, n'hésitez pas à demander l'avis des autres en cas de doute.

4. **Gestion des conflits** :
   - Les conflits de fusion sont résolus en équipe.

---

## **Exemple de Données**
La collection est une liste de livres, chaque livre étant représenté par un ensemble d’informations (titre, éditeur, genre, nombre de pages, etc.).
Le fichier CSV initial contient ces informations, le code présent dans main.py permet de manipuler ce fichier et d'en extraire les données, le groupe devrait interagir avec la liste de livres qui en est extraite uniquement.
