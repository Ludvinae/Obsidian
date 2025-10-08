# <span style="color:red;">📚 Algorithmes en PHP — Exercices par Niveaux (+ Bonus Sudoku)</span>

> Tout est prêt à copier-coller. Chaque niveau contient **les énoncés**, des **exemples**, des **contraintes**, et un **starter code PHP** avec des `TODO` à compléter.  
> Version : PHP 8+ — utilisez `declare(strict_types=1);` si vous le souhaitez.

---

## 🔹 Niveau 1 — Bases simples  
🎯 **Objectif :** boucles, conditions, arithmétique élémentaire.

### 1) Pairs consécutifs  
**But :** vérifier si deux nombres **pairs** apparaissent côte à côte.  
**Ex. :** `[1,4,6,3] → true`, `[2,1,4] → false`.

**Contraintes :** tableau d’entiers (≥ 0 ou négatifs autorisés).

---

### 2) Somme des carrés  
**But :** calculer `1² + 2² + … + n²`.  
**Ex. :** `n=3 → 14`.  
**Contraintes :** `n ≥ 0`.

---

### 3) Renverser un nombre  
**But :** `1234 → 4321` (gérer le **signe négatif** : `-120 → -21`).  
**Contraintes :** 32/64 bits selon votre environnement (ignorez l’overflow pour l’exercice).

---

### 4) Tableau miroir  
**But :** `[1,2,3] → [1,2,3,2,1]`.  
**Contraintes :** ne pas modifier l’original (retourner un **nouveau** tableau).

---

### 5) Compter “a” dans une chaîne  
**But :** `"JavaScript" → 2` (compter **a/A**).  
**Contraintes :** sensible à la casse ? -> **Non** (comptez a/A).

---

### 6) Factorielle (récursive & itérative)  
**But :** `5! = 120`.  
**Contraintes :** `0! = 1`, `n ≥ 0`.

---

### 7) Égalité somme gauche/droite (pivot)  
**But :** existe-t-il un index `i` tel que `sum(left) == sum(right)` ?  
**Ex. :** `[10,20,30,10,20] → true` (30 est pivot : 10+20 = 10+20).

---

#### 🧪 Starter code (Niveau 1)
```php
<?php
// TODO: ajoutez declare(strict_types=1); si souhaité.

/** 1) Pairs consécutifs */
function hasConsecutiveEvens(array $arr): bool {
    // TODO: retournez true s'il existe i tel que arr[i] et arr[i+1] sont pairs.
    return false;
}

/** 2) Somme des carrés 1^2 + ... + n^2 */
function sumSquares(int $n): int {
    // TODO
    return 0;
}

/** 3) Renverser un nombre (gérer négatif) */
function reverseInt(int $x): int {
    // TODO
    return 0;
}

/** 4) Tableau miroir */
function mirrorArray(array $arr): array {
    // TODO: [1,2,3] -> [1,2,3,2,1]
    return [];
}

/** 5) Compter 'a' (non sensible à la casse) */
function countLetterA(string $s): int {
    // TODO
    return 0;
}

/** 6a) Factorielle itérative */
function factorialIter(int $n): int {
    // TODO
    return 1;
}

/** 6b) Factorielle récursive */
function factorialRec(int $n): int {
    // TODO
    return 1;
}

/** 7) Égalité somme gauche/droite (pivot) */
function hasEquilibriumIndex(array $arr): bool {
    // TODO
    return false;
}

// — Optionnel : quelques tests rapides
// var_dump(hasConsecutiveEvens([1,4,6,3])); // true
```

---

## 🔹 Niveau 2 — Chaînes & conditions  
🎯 **Objectif :** manipuler chaînes, sous-chaînes, logique conditionnelle.

### 1) Mot en escalier  
**But :** `"CODE"` →  
```
C
CO
COD
CODE
```
**Retour attendu :** une **chaîne** multi-ligne (séparée par "\n") ou un **tableau** de lignes.

---

### 2) Rotation de voyelles  
**But :** déplacer chaque **voyelle** d’un cran : `a→e→i→o→u→a` (conserver la casse).  
**Ex. :** `"hello" → "hillu"` (e→i, o→u).  
**Voyelles :** `a e i o u` / `A E I O U`.

---

### 3) Mot répété k fois  
**But :** `"js", k=3 → "jsjsjs"`.

---

### 4) Mots croisés (simple)  
**But :** deux mots partagent-ils **au moins une lettre** (case-insensible) ?  
**Ex. :** `"chat","tigre" → true` (lettre **t**).

---

### 5) Index des majuscules  
**But :** `"HeLLo" → [0,2,3]`.

---

### 6) Palindrome numérique  
**But :** `121 → true`, `123 → false` (sans convertir en chaîne si possible).

---

### 7) Césure d’un mot (chunks)  
**But :** `"algorithme", n=3 → ["alg","ori","thm","e"]`.

---

#### 🧪 Starter code (Niveau 2)
```php
<?php
/** 1) Mot en escalier */
function staircaseWord(string $word): string {
    // TODO: construire lignes "C\nCO\n..." ou retourner un tableau de lignes
    return "";
}

/** 2) Rotation de voyelles a->e->i->o->u->a (respect casse) */
function rotateVowels(string $s): string {
    // TODO
    return $s;
}

/** 3) Répéter mot k fois */
function repeatWord(string $word, int $k): string {
    // TODO
    return "";
}

/** 4) Partage au moins une lettre (case-insensible) */
function shareLetter(string $a, string $b): bool {
    // TODO
    return false;
}

/** 5) Indices des majuscules */
function uppercaseIndices(string $s): array {
    // TODO
    return [];
}

/** 6) Palindrome numérique */
function isNumericPalindrome(int $x): bool {
    // TODO (évitez la conversion en string pour le challenge)
    return false;
}

/** 7) Césure d'un mot par blocs de n caractères */
function chunkWord(string $word, int $n): array {
    // TODO
    return [];
}
```

---

## 🔹 Niveau 3 — Tableaux & logique intermédiaire  
🎯 **Objectif :** parcours fins, tri simple, regroupements.

### 1) Somme diagonale secondaire (matrice)  
**But :** somme de `m[i][n-1-i]` pour une matrice carrée `n×n`.

---

### 2) Compter les inversions  
**But :** paires `(i,j)` avec `i<j` et `arr[i] > arr[j]`.  
**Ex. :** `[2,4,1,3] → 3`.

---

### 3) Détecter progression arithmétique  
**But :** `[2,4,6,8] → true`, `[1,2,4] → false`.

---

### 4) Fusion alternée de deux tableaux  
**But :** `[a,b,c] + [1,2,3] → [a,1,b,2,c,3]` (gérer tailles différentes).

---

### 5) Tri par insertion  
**But :** coder l’**insertion sort**.  
**Ex. :** `[5,2,9] → [2,5,9]`.

---

### 6) Sous-tableau avec somme donnée (positifs)  
**But :** `[1,2,3,7,5], somme=12 → [2,3,7]`.  
**Indice :** **fenêtre glissante** si tous les éléments sont **≥ 0**.

---

### 7) Équilibre des hauteurs (déplacements min.)  
**But :** nombre d’éléments **à déplacer** pour que le tableau devienne trié (croissant).  
**Idée simple :** comparer au **tableau trié** et compter les **mauvais placements**.

---

#### 🧪 Starter code (Niveau 3)
```php
<?php
/** 1) Somme diagonale secondaire */
function secondaryDiagonalSum(array $m): int {
    // TODO: suppose matrice carrée
    return 0;
}

/** 2) Compter les inversions (O(n^2) accepté ici) */
function countInversions(array $arr): int {
    // TODO
    return 0;
}

/** 3) Progression arithmétique ? */
function isArithmeticProgression(array $arr): bool {
    // TODO
    return false;
}

/** 4) Fusion alternée */
function alternateMerge(array $a, array $b): array {
    // TODO
    return [];
}

/** 5) Tri par insertion */
function insertionSort(array $arr): array {
    // TODO
    return $arr;
}

/** 6) Sous-tableau avec somme (éléments >= 0) */
function subarrayWithSum(array $arr, int $target): array {
    // TODO: renvoyer le sous-tableau trouvé ou []
    return [];
}

/** 7) Équilibre des hauteurs (nb de déplacements) */
function minMovesToSort(array $heights): int {
    // TODO: comparez avec une copie triée
    return 0;
}
```

---

## 🔹 Niveau 4 — Algo avancé (réflexion)  
🎯 **Objectif :** optimisation, récursivité, graphes légers.

### 1) Nombres amicaux  
**But :** `sumDivPropres(220)=284` et réciproquement ⇒ **amicaux**.

---

### 2) Syracuse / Collatz max ≤ N  
**But :** pour `1..N`, renvoyer le nombre qui a la **suite la plus longue** (et sa longueur).  
**Indice :** mémoïsation possible.

---

### 3) Tournoi round-robin  
**But :** toutes les paires entre joueurs `[A,B,C] → [[A,B],[A,C],[B,C]]`.

---

### 4) Sous-mot commun le plus long  
**But :** **plus longue sous-séquence commune** (LCS).  
**Ex. :** `"abcde","ace" → "ace"`.

---

### 5) Tableau “spirale”  
**But :** générer matrice `n×n` remplie en **spirale croissante** (1..n²).

---

### 6) Chemins grille (haut/droite)  
**But :** nombre de chemins de `(0,0)` à `(m,n)` (mouvements **droite**/**bas**).  
**Indice :** DP combinatoire (`C(m+n, m)`) ou **programmation dynamique**.

---

### 7) Tri fusion (merge sort)  
**But :** implémenter **merge sort** (récursif + fusion).

---

#### 🧪 Starter code (Niveau 4)
```php
<?php
/** 1) Amicaux ? */
function sumProperDivisors(int $n): int {
    // TODO: somme des diviseurs stricts de n (exclure n)
    return 1;
}
function areAmicable(int $a, int $b): bool {
    // TODO
    return false;
}

/** 2) Collatz: plus longue suite pour 1..N */
function collatzLength(int $x): int {
    // TODO (mémoïsation possible)
    return 0;
}
function longestCollatzUpTo(int $N): array {
    // TODO: return ['number' => ?, 'length' => ?]
    return ['number' => 1, 'length' => 1];
}

/** 3) Round-robin pairs */
function roundRobinPairs(array $players): array {
    // TODO
    return [];
}

/** 4) LCS (plus longue sous-séquence commune) */
function lcs(string $s1, string $s2): string {
    // TODO: DP classique
    return "";
}

/** 5) Matrice spirale n×n (1..n^2) */
function spiralMatrix(int $n): array {
    // TODO
    return [];
}

/** 6) Chemins grille (DP) */
function gridPaths(int $m, int $n): int {
    // TODO
    return 0;
}

/** 7) Tri fusion */
function mergeSort(array $arr): array {
    // TODO: cas base + fusion
    return $arr;
}
```

---

## 🎯 Bonus / Mini-projet — Sudoku Simplifié (Validation)

**But :** vérifier qu’une **grille 9×9 partielle** est **valide** :  
- Pas de doublons dans **chaque ligne** (hors cases vides)  
- Pas de doublons dans **chaque colonne**  
- Pas de doublons dans chaque **sous-carré 3×3**  
**Entrée :** chiffres `1..9` et **cases vides** représentées par `"."` (ou `0`).  
**Sortie :** `true/false`.  
**⚠️** Ne **pas** résoudre la grille, seulement **valider**.

**Exemple (texte) :**
```
5 3 . | . 7 . | . . .
6 . . | 1 9 5 | . . .
. 9 8 | . . . | . 6 .
------+-------+------
8 . . | . 6 . | . . 3
4 . . | 8 . 3 | . . 1
7 . . | . 2 . | . . 6
------+-------+------
. 6 . | . . . | 2 8 .
. . . | 4 1 9 | . . 5
. . . | . 8 . | . 7 9
```

#### 🧪 Starter code (Bonus)
```php
<?php
/** Vérifie qu'une unité (ligne/colonne/boîte) n'a pas de doublons (hors '.' ou 0) */
function unitIsValid(array $unit): bool {
    // TODO: filtrer '.', '0', vérifier doublons
    return true;
}

/** Récupère la 3x3 box (r,c) => indices 0..2 pour groupe ligne/col */
function getBox(array $grid, int $boxRow, int $boxCol): array {
    // TODO: extraire 9 cases de la boîte (3x3)
    return [];
}

/** Est-ce qu'une grille 9x9 partielle est valide ? */
function estSudokuValide(array $grid): bool {
    // TODO:
    // 1) lignes
    // 2) colonnes
    // 3) 9 boîtes 3x3
    return false;
}

/** Exemple d'utilisation ('.' pour vide) */
$grid = [
    ['5','3','.','.','7','.','.','.','.'],
    ['6','.','.','1','9','5','.','.','.'],
    ['.','9','8','.','.','.','.','6','.'],
    ['8','.','.','.','6','.','.','.','3'],
    ['4','.','.','8','.','3','.','.','1'],
    ['7','.','.','.','2','.','.','.','6'],
    ['.','6','.','.','.','.','2','8','.'],
    ['.','.','.','4','1','9','.','.','5'],
    ['.','.','.','.','8','.','.','7','9'],
];
// var_dump(estSudokuValide($grid)); // attendu: true pour cet exemple classique
```

---

## 💡 Tips généraux (pour réussir plus vite)

- **Boucles & conditions :** commencez par les **cas simples** (tableau vide, taille 1, `n=0`).  
- **Chaînes :** précisez si l’exercice doit être **sensible à la casse**.  
- **Tableaux :** évitez de **muter** l’original sauf mention contraire (travaillez sur une **copie**).  
- **Complexité :** annoncez vos choix (ex. `O(n^2)` acceptable ici, `O(n log n)` utile pour de grands tableaux).  
- **Tests :** ajoutez **des cas limites** (vide, singleton, tous identiques, valeurs négatives, etc.).
