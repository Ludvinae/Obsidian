# <span style="color:red;">Introduction aux Collections en PHP : Correction Exercices</span> 📘

---

## <span style="color:red;">Exercice n°1 : Correction (QCM – Panorama des collections SPL)</span> ✅

1) **B — `SplStack`**  
*Raison :* une pile suit le modèle **LIFO** (*Last In, First Out*).

2) **A — `SplQueue`**  
*Raison :* une file suit le modèle **FIFO** (*First In, First Out*).

3) **B — `SplObjectStorage`**  
*Raison :* agit comme un **set d’objets** (unicité par identité) et permet d’associer des **métadonnées**.

4) **A — Les éléments peuvent être consommés par l’itération**  
*Raison :* selon les **extract flags** et le mode d’itération, `SplPriorityQueue` peut être **vidée** au fil du parcours.

5) **B — Moins de surcoût mémoire pour une taille connue**  
*Raison :* `SplFixedArray` optimise la mémoire lorsqu’on connaît **à l’avance** la taille.

---

## <span style="color:red;">Exercice n°2 : Correction (Implémenter une pile – Historique)</span> 📚

```php
<?php
$history = new SplStack();

// 1) Empiler les pages
$history->push("Accueil");
$history->push("Produits");
$history->push("Produit #42");
$history->push("Panier");

// 2) Page courante (sommet)
echo "Courant : " . $history->top() . PHP_EOL; // Panier

// 3) Retour en arrière (pop 2x)
$history->pop(); // quitte "Panier"
$history->pop(); // quitte "Produit #42"
echo "Après retour : " . $history->top() . PHP_EOL; // Produits

// 4) Afficher toutes les pages restantes (du sommet vers la base)
echo "Pile restante (du sommet vers la base) :" . PHP_EOL;
foreach ($history as $page) {
    echo "- " . $page . PHP_EOL; // Produits, Accueil
}
```

> 🧠 **Note :** `top()` lit sans retirer ; `pop()` retire l’élément au sommet. L’itération d’une `SplStack` **n’est pas destructrice** (contrairement à `SplPriorityQueue`).

---

## <span style="color:red;">Exercice n°3 : Correction (File d’attente – Support technique)</span> 🚶

```php
<?php
$queue = new SplQueue();

// 1) Enqueue de 3 tickets
$queue->enqueue("#101");
$queue->enqueue("#102");
$queue->enqueue("#103");

// 2) Traiter jusqu'à ce que la file soit vide
while (!$queue->isEmpty()) {
    $ticket = $queue->dequeue();
    echo "Traitement du ticket $ticket" . PHP_EOL;
}

// 3) Nombre de tickets restants
echo "Reste : " . count($queue) . PHP_EOL; // 0
```

> 💡 **Astuce :** `SplQueue` implémente `Countable` → `count($queue)` fonctionne directement.

---

## <span style="color:red;">Exercice n°4 : Correction (Ordonner par priorité – Planificateur)</span> 🥇

```php
<?php
$pq = new SplPriorityQueue();

// 1-2) Insertion avec priorités (plus grand = plus prioritaire)
$pq->insert("Sauvegarde", 10);
$pq->insert("Indexation", 50);
$pq->insert("Alerte critique", 100);

// 3) Extraire uniquement la donnée
$pq->setExtractFlags(SplPriorityQueue::EXTR_DATA);

// 4) Extraire dans l'ordre des priorités
while (!$pq->isEmpty()) {
    echo $pq->extract() . PHP_EOL;
}
// Sortie attendue :
// Alerte critique
// Indexation
// Sauvegarde
```

> ⚠️ **Attention :** `extract()` **retire** les éléments ; après la boucle la file est **vide**.

---

## <span style="color:red;">Exercice n°5 : Correction (Collection typée – IteratorAggregate + Countable)</span> 🧱

```php
<?php
// 1) Classe immuable Book
final class Book {
    public function __construct(
        public string $title,
        public string $author,
        public int $pages
    ) {}
}

// 2) BookCollection typée
final class BookCollection implements IteratorAggregate, Countable {
    /** @var Book[] */
    private array $items = [];

    public function __construct(Book ...$books) {
        foreach ($books as $b) {
            $this->add($b);
        }
    }

    public function add(Book $b): void {
        $this->items[] = $b;
    }

    /** @return Traversable<Book> */
    public function getIterator(): Traversable {
        return new ArrayIterator($this->items);
    }

    public function count(): int {
        return count($this->items);
    }

    /** Renvoie une NOUVELLE collection filtrée */
    public function filter(callable $p): self {
        $out = new self();
        foreach ($this->items as $b) {
            if ($p($b)) {
                $out->add($b);
            }
        }
        return $out;
    }

    /** Mappe les livres vers un tableau (scalaires/objets) */
    public function map(callable $m): array {
        $result = [];
        foreach ($this->items as $b) {
            $result[] = $m($b);
        }
        return $result;
    }

    /** Somme totale des pages via réduction */
    public function totalPages(): int {
        $total = 0;
        foreach ($this->items as $b) {
            $total += $b->pages;
        }
        return $total;
    }
}

// 3) Démonstration d'utilisation
$bc = new BookCollection(
    new Book("Clean Code", "Robert C. Martin", 464),
    new Book("The Pragmatic Programmer", "Andrew Hunt", 352),
    new Book("Refactoring", "Martin Fowler", 448)
);

// Filtrer > 200 pages
$longs = $bc->filter(fn(Book $b) => $b->pages > 200);

// Récupérer uniquement les titres
$titres = $longs->map(fn(Book $b) => $b->title);

// Somme totale des pages (de toute la collection)
$total = $bc->totalPages();

// Affichage
echo "Titres (>200 pages) : " . implode(", ", $titres) . PHP_EOL;
echo "Total pages (tous livres) : $total" . PHP_EOL;
```

> ✅ **Points clés :**  
> - `filter()` retourne **une nouvelle collection** (pas d’effet de bord).  
> - `getIterator()` expose un `ArrayIterator` → compatible `foreach`.  
> - `Countable` permet `count($collection)`.

