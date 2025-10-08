# <span style="color:red;">Introduction aux Collections en PHP : Exercices</span> 📘

---

## <span style="color:red;">Exercice n°1 : QCM – Panorama des collections (SPL)</span> 🧩
**Objectif :** Vérifier les acquis sur les structures les plus courantes de la SPL.

1) Quelle structure correspond à une **pile (LIFO)** ?  
   - A) `SplQueue`  
   - B) `SplStack`  
   - C) `SplDoublyLinkedList`  

2) Quelle structure garantit l’ordre **FIFO** ?  
   - A) `SplQueue`  
   - B) `SplStack`  
   - C) `SplMaxHeap`  

3) Laquelle est la plus adaptée pour conserver un **ensemble d’objets uniques** (avec métadonnées facultatives) ?  
   - A) `ArrayObject`  
   - B) `SplObjectStorage`  
   - C) `SplFixedArray`  

4) Quel **piège** courant avec `SplPriorityQueue` lors d’un `foreach` ?  
   - A) Les éléments sont **consommés** par l’itération selon le mode  
   - B) Les éléments sont automatiquement triés par insertion  
   - C) Les clés sont toujours préservées  

5) Quel avantage de `SplFixedArray` par rapport à un tableau classique ?  
   - A) Taille dynamique illimitée  
   - B) Moins de surcoût **mémoire** pour une taille connue  
   - C) Itération plus rapide que `ArrayIterator` dans tous les cas  

💡 **Tips pour apprenants :**  
- LIFO = **Stack**, FIFO = **Queue**.  
- `SplObjectStorage` agit comme un **set** d’objets (unicité par identité).  
- Avec `SplPriorityQueue`, attention au **mode d’extraction** (`setExtractFlags`) et à l’itération qui peut **vider** la file.

---

## <span style="color:red;">Exercice n°2 : Implémenter une pile (Historique de navigation)</span> 📚
**Objectif :** Manipuler `SplStack` (push/pop, lecture de l’élément courant).

**Consignes :**  
1. Crée une pile `SplStack` et empile (`push`) les pages : `"Accueil"`, `"Produits"`, `"Produit #42"`, `"Panier"`.  
2. Affiche la page courante (sommet de pile).  
3. Simule un **retour en arrière** : dépile (`pop`) deux fois et affiche la page courante.  
4. Affiche toutes les pages restantes (du sommet vers la base).

```php
<?php
$history = new SplStack();

// TODO 1) push pages

// TODO 2) echo "Courant: ..."

// TODO 3) pop deux fois, echo "Retour: ..."

// TODO 4) Parcourir la pile et afficher chaque page
```

💡 **Tips pour apprenants :**  
- `push()` ajoute au **sommet**, `pop()` **retire** le sommet.  
- On peut regarder le sommet avec `top()` sans le retirer.

---

## <span style="color:red;">Exercice n°3 : Gérer une file d’attente (Support technique)</span> 🚶
**Objectif :** Utiliser `SplQueue` (enqueue/dequeue), vérifier la taille via `Countable`.

**Consignes :**  
1. Crée une `SplQueue` et ajoute (`enqueue`) trois tickets : `#101`, `#102`, `#103`.  
2. Traite (`dequeue`) les tickets **jusqu’à ce que la file soit vide** : affiche `"Traitement du ticket ..."` à chaque itération.  
3. Après traitement, affiche le nombre de tickets restants.

```php
<?php
$queue = new SplQueue();

// TODO 1) enqueue 3 tickets

// TODO 2) while (!$queue->isEmpty()) { ... dequeue ... }

// TODO 3) echo "Reste: " . count($queue);
```

💡 **Tips pour apprenants :**  
- `SplQueue` implémente `Countable` → `count($queue)` fonctionne.  
- `isEmpty()` est pratique pour contrôler la boucle.

---

## <span style="color:red;">Exercice n°4 : Ordonner par priorité (Planificateur de tâches)</span> 🥇
**Objectif :** Découvrir `SplPriorityQueue` et ses modes d’extraction.

**Consignes :**  
1. Crée une `SplPriorityQueue` pour des tâches sous forme de chaînes : `"Sauvegarde"`, `"Indexation"`, `"Alerte critique"`.  
2. Assigne des priorités (plus grand = plus prioritaire), par ex. : Alerte=100, Indexation=50, Sauvegarde=10.  
3. Configure les **extract flags** pour **extraire seulement la donnée**.  
4. Extrait et affiche **dans l’ordre de priorité** toutes les tâches.

```php
<?php
$pq = new SplPriorityQueue();

// TODO 1-2) insert(task, priority)

// TODO 3) $pq->setExtractFlags( ... );

// TODO 4) while (!$pq->isEmpty()) { echo $pq->extract() . PHP_EOL; }
```

💡 **Tips pour apprenants :**  
- `setExtractFlags(SplPriorityQueue::EXTR_DATA)` pour ne récupérer **que** la donnée.  
- L’itération/`extract()` **vide** la structure : si vous devez réutiliser, copiez-la d’abord.

---

## <span style="color:red;">Exercice n°5 : Créer une collection typée (IteratorAggregate + Countable)</span> 🧱
**Objectif :** Construire une petite **collection métier** réutilisable.

**Consignes :**  
1. Définis une classe immuable `Book` avec propriétés publiques `string $title`, `string $author`, `int $pages`.  
2. Crée une classe `BookCollection` qui :  
   - implémente `IteratorAggregate` et `Countable`,  
   - expose une méthode `add(Book $b): void`,  
   - expose `filter(callable $p): self` (renvoie une **nouvelle** collection),  
   - expose `map(callable $m): array` (retourne un tableau),  
   - expose `totalPages(): int` (somme des pages via une réduction).  
3. Démonstration :  
   - Ajoute 3 livres,  
   - Filtre ceux de plus de **200 pages**,  
   - Mappe vers les **titres**,  
   - Affiche la **somme totale** des pages.

```php
<?php
// TODO 1) class Book { ... }

// TODO 2) class BookCollection implements IteratorAggregate, Countable { ... }

// TODO 3) Démo d'utilisation
$bc = new BookCollection(
    // Optionnel : démarrage via constructeur variadique
);
```

💡 **Tips pour apprenants :**  
- Retourne une **nouvelle** collection dans `filter()` pour éviter les effets de bord.  
- Dans `getIterator()`, renvoie `new ArrayIterator($this->items)`.  
- Typage strict = code plus **prévisible** et **testable**.

---
