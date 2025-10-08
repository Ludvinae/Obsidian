# ✅ Corrections détaillées — Kata

> Version PHP 8+. J’inclus pour chaque fonction : **solution**, **explications**, parfois **complexité** et **cas limites**.  
> Tout est prêt à copier-coller. Vous pouvez activer le typage strict si souhaité.

---

## 🔹 Niveau 1 — Bases simples

```php
<?php
// 1) Pairs consécutifs
// Idée : balayer le tableau et tester arr[i] % 2 == 0 && arr[i+1] % 2 == 0.
// Complexité : O(n)
function hasConsecutiveEvens(array $arr): bool {
    for ($i = 0, $n = count($arr) - 1; $i < $n; $i++) {
        if (($arr[$i] & 1) === 0 && ($arr[$i+1] & 1) === 0) return true;
    }
    return false;
}

// 2) Somme des carrés 1^2 + ... + n^2
// Deux options : boucle O(n) ou formule n(n+1)(2n+1)/6 en O(1).
function sumSquares(int $n): int {
    if ($n <= 0) return 0;
    return intdiv($n * ($n + 1) * (2 * $n + 1), 6);
}

// 3) Renverser un nombre (gérer négatif)
// Technique : travailler en valeur absolue puis réappliquer le signe.
// 120 -> 21 ; -120 -> -21
function reverseInt(int $x): int {
    $sign = $x < 0 ? -1 : 1;
    $x = abs($x);
    $rev = 0;
    while ($x > 0) {
        $rev = $rev * 10 + ($x % 10);
        $x = intdiv($x, 10);
    }
    return $sign * $rev;
}

// 4) Tableau miroir
// Exemple : [1,2,3] -> [1,2,3,2,1]
// On n'ajoute pas l'élément central en double, on concatène le reverse du tableau SANS son dernier élément.
function mirrorArray(array $arr): array {
    $n = count($arr);
    if ($n <= 1) return $arr;
    $tail = array_slice($arr, 0, -1);
    $tail = array_reverse($tail);
    return array_merge($arr, $tail);
}

// 5) Compter 'a' (non sensible à la casse)
function countLetterA(string $s): int {
    return substr_count(strtolower($s), 'a');
}

// 6) Factorielle (itérative & récursive)
function factorialIter(int $n): int {
    if ($n < 0) throw new InvalidArgumentException("n doit être >= 0");
    $res = 1;
    for ($i = 2; $i <= $n; $i++) $res *= $i;
    return $res;
}
function factorialRec(int $n): int {
    if ($n < 0) throw new InvalidArgumentException("n doit être >= 0");
    if ($n <= 1) return 1;
    return $n * factorialRec($n - 1);
}

// 7) Égalité somme gauche/droite (pivot index)
// On cherche i tel que sum(arr[0..i-1]) == sum(arr[i+1..end])
// Complexité : O(n) avec somme totale puis parcours.
function hasEquilibriumIndex(array $arr): bool {
    $total = array_sum($arr);
    $left = 0;
    foreach ($arr as $i => $val) {
        $right = $total - $left - $val;
        if ($left === $right) return true;
        $left += $val;
    }
    return false;
}

// // TESTS RAPIDES
// var_dump(hasConsecutiveEvens([1,4,6,3])); // true
// var_dump(sumSquares(3)); // 14
// var_dump(reverseInt(-120)); // -21
// var_dump(mirrorArray([1,2,3])); // [1,2,3,2,1]
// var_dump(countLetterA("JavaScript")); // 2
// var_dump(factorialIter(5)); // 120
// var_dump(factorialRec(5)); // 120
// var_dump(hasEquilibriumIndex([10,20,30,10,20])); // true
```

---

## 🔹 Niveau 2 — Chaînes & conditions

```php
<?php
// 1) Mot en escalier : "CODE" -> "C\nCO\nCOD\nCODE"
function staircaseWord(string $word): string {
    $out = [];
    for ($i = 1, $n = strlen($word); $i <= $n; $i++) {
        $out[] = substr($word, 0, $i);
    }
    return implode("\n", $out);
}

// 2) Rotation de voyelles (a->e->i->o->u->a), respect de la casse
function rotateVowels(string $s): string {
    $map = [
        'a' => 'e','e' => 'i','i' => 'o','o' => 'u','u' => 'a',
        'A' => 'E','E' => 'I','I' => 'O','O' => 'U','U' => 'A'
    ];
    $chars = preg_split('//u', $s, -1, PREG_SPLIT_NO_EMPTY);
    foreach ($chars as $i => $ch) {
        if (isset($map[$ch])) $chars[$i] = $map[$ch];
    }
    return implode('', $chars);
}

// 3) Mot répété k fois
function repeatWord(string $word, int $k): string {
    if ($k <= 0) return "";
    return str_repeat($word, $k);
}

// 4) Mots croisés (partagent au moins une lettre, case-insensible)
function shareLetter(string $a, string $b): bool {
    $setA = array_unique(str_split(strtolower($a)));
    $seen = array_fill_keys($setA, true);
    foreach (array_unique(str_split(strtolower($b))) as $ch) {
        if (isset($seen[$ch]) && ctype_alpha($ch)) return true;
    }
    // On pourrait accepter tout caractère, ici on limite aux lettres
    return false;
}

// 5) Indices des majuscules
function uppercaseIndices(string $s): array {
    $idx = [];
    for ($i = 0, $n = strlen($s); $i < $n; $i++) {
        if (ctype_upper($s[$i])) $idx[] = $i;
    }
    return $idx;
}

// 6) Palindrome numérique (sans string)
// Règle: négatif -> false ; compare x avec sa version renversée.
function isNumericPalindrome(int $x): bool {
    if ($x < 0) return false;
    $orig = $x;
    $rev = 0;
    while ($x > 0) {
        $rev = $rev * 10 + ($x % 10);
        $x = intdiv($x, 10);
    }
    return $rev === $orig;
}

// 7) Césure d’un mot par blocs de n caractères
function chunkWord(string $word, int $n): array {
    if ($n <= 0) return [$word];
    $out = [];
    for ($i = 0, $len = strlen($word); $i < $len; $i += $n) {
        $out[] = substr($word, $i, $n);
    }
    return $out;
}

// // TESTS RAPIDES
// echo staircaseWord("CODE"), "\n";
// echo rotateVowels("hello"), "\n"; // hillu
// echo repeatWord("js",3), "\n"; // jsjsjs
// var_dump(shareLetter("chat","tigre")); // true
// var_dump(uppercaseIndices("HeLLo")); // [0,2,3]
// var_dump(isNumericPalindrome(121)); // true
// var_dump(chunkWord("algorithme",3)); // ["alg","ori","thm","e"]
```

---

## 🔹 Niveau 3 — Tableaux & logique intermédiaire

```php
<?php
// 1) Somme diagonale secondaire : m[i][n-1-i]
function secondaryDiagonalSum(array $m): int {
    $n = count($m);
    $sum = 0;
    for ($i = 0; $i < $n; $i++) {
        $sum += $m[$i][$n - 1 - $i] ?? 0;
    }
    return $sum;
}

// 2) Compter les inversions (O(n^2) ici)
function countInversions(array $arr): int {
    $n = count($arr);
    $cnt = 0;
    for ($i = 0; $i < $n; $i++) {
        for ($j = $i + 1; $j < $n; $j++) {
            if ($arr[$i] > $arr[$j]) $cnt++;
        }
    }
    return $cnt;
}

// 3) Progression arithmétique ?
function isArithmeticProgression(array $arr): bool {
    $n = count($arr);
    if ($n < 2) return true;
    $d = $arr[1] - $arr[0];
    for ($i = 2; $i < $n; $i++) {
        if ($arr[$i] - $arr[$i-1] !== $d) return false;
    }
    return true;
}

// 4) Fusion alternée (gérer tailles différentes)
function alternateMerge(array $a, array $b): array {
    $out = [];
    $i = $j = 0;
    $na = count($a); $nb = count($b);
    while ($i < $na || $j < $nb) {
        if ($i < $na) $out[] = $a[$i++];
        if ($j < $nb) $out[] = $b[$j++];
    }
    return $out;
}

// 5) Tri par insertion
function insertionSort(array $arr): array {
    for ($i = 1, $n = count($arr); $i < $n; $i++) {
        $key = $arr[$i];
        $j = $i - 1;
        while ($j >= 0 && $arr[$j] > $key) {
            $arr[$j+1] = $arr[$j];
            $j--;
        }
        $arr[$j+1] = $key;
    }
    return $arr;
}

// 6) Sous-tableau avec somme donnée (tous éléments >= 0) — fenêtre glissante
function subarrayWithSum(array $arr, int $target): array {
    $start = 0; $sum = 0;
    for ($end = 0, $n = count($arr); $end < $n; $end++) {
        $sum += $arr[$end];
        while ($sum > $target && $start <= $end) {
            $sum -= $arr[$start++];
        }
        if ($sum === $target) {
            return array_slice($arr, $start, $end - $start + 1);
        }
    }
    return [];
}

// 7) Équilibre des hauteurs — nb d’éléments à déplacer (approche simple)
// Idée (simple) : comparer au tableau trié et compter les positions différentes.
function minMovesToSort(array $heights): int {
    $sorted = $heights;
    sort($sorted);
    $moves = 0;
    for ($i = 0, $n = count($heights); $i < $n; $i++) {
        if ($heights[$i] !== $sorted[$i]) $moves++;
    }
    return $moves;
}

// // TESTS RAPIDES
// $m = [[1,2,3],[4,5,6],[7,8,9]];
// var_dump(secondaryDiagonalSum($m)); // 15 (3 + 5 + 7)
// var_dump(countInversions([2,4,1,3])); // 3
// var_dump(isArithmeticProgression([2,4,6,8])); // true
// var_dump(alternateMerge(['a','b','c'], [1,2,3])); // [a,1,b,2,c,3]
// var_dump(insertionSort([5,2,9])); // [2,5,9]
// var_dump(subarrayWithSum([1,2,3,7,5], 12)); // [2,3,7]
// var_dump(minMovesToSort([1,1,4,2,1,3])); // nombre d'écarts
```

---

## 🔹 Niveau 4 — Algo avancé (réflexion)

```php
<?php
// 1) Nombres amicaux
// Somme des diviseurs propres (exclut n). Optimisation sqrt(n).
function sumProperDivisors(int $n): int {
    if ($n <= 1) return 0;
    $sum = 1; // 1 est toujours un diviseur propre (pour n>1)
    $limit = (int)floor(sqrt($n));
    for ($d = 2; $d <= $limit; $d++) {
        if ($n % $d === 0) {
            $sum += $d;
            $pair = intdiv($n, $d);
            if ($pair !== $d) $sum += $pair;
        }
    }
    return $sum;
}
function areAmicable(int $a, int $b): bool {
    if ($a === $b) return false;
    return sumProperDivisors($a) === $b && sumProperDivisors($b) === $a;
}

// 2) Syracuse / Collatz : plus longue suite pour 1..N
function collatzLength(int $x, array &$memo = []): int {
    if ($x === 1) return 1;
    if (isset($memo[$x])) return $memo[$x];
    $next = ($x % 2 === 0) ? intdiv($x, 2) : 3*$x + 1;
    return $memo[$x] = 1 + collatzLength($next, $memo);
}
function longestCollatzUpTo(int $N): array {
    $memo = [1 => 1];
    $bestNum = 1; $bestLen = 1;
    for ($i = 2; $i <= $N; $i++) {
        $len = collatzLength($i, $memo);
        if ($len > $bestLen) { $bestLen = $len; $bestNum = $i; }
    }
    return ['number' => $bestNum, 'length' => $bestLen];
}

// 3) Tournoi round-robin (toutes les paires i<j)
function roundRobinPairs(array $players): array {
    $pairs = [];
    for ($i = 0, $n = count($players); $i < $n; $i++) {
        for ($j = $i + 1; $j < $n; $j++) {
            $pairs[] = [$players[$i], $players[$j]];
        }
    }
    return $pairs;
}

// 4) LCS (plus longue sous-séquence commune) — DP + reconstruction
function lcs(string $s1, string $s2): string {
    $n = strlen($s1); $m = strlen($s2);
    $dp = array_fill(0, $n + 1, array_fill(0, $m + 1, 0));
    for ($i = 1; $i <= $n; $i++) {
        for ($j = 1; $j <= $m; $j++) {
            if ($s1[$i-1] === $s2[$j-1]) {
                $dp[$i][$j] = 1 + $dp[$i-1][$j-1];
            } else {
                $dp[$i][$j] = max($dp[$i-1][$j], $dp[$i][$j-1]);
            }
        }
    }
    // Reconstruction
    $i = $n; $j = $m; $chars = [];
    while ($i > 0 && $j > 0) {
        if ($s1[$i-1] === $s2[$j-1]) {
            $chars[] = $s1[$i-1];
            $i--; $j--;
        } elseif ($dp[$i-1][$j] >= $dp[$i][$j-1]) {
            $i--;
        } else {
            $j--;
        }
    }
    return implode('', array_reverse($chars));
}

// 5) Matrice spirale n×n (1..n^2)
function spiralMatrix(int $n): array {
    if ($n <= 0) return [];
    $mat = array_fill(0, $n, array_fill(0, $n, 0));
    $top = 0; $bottom = $n - 1; $left = 0; $right = $n - 1;
    $val = 1;
    while ($top <= $bottom && $left <= $right) {
        for ($c = $left; $c <= $right; $c++) $mat[$top][$c] = $val++;
        $top++;
        for ($r = $top; $r <= $bottom; $r++) $mat[$r][$right] = $val++;
        $right--;
        if ($top <= $bottom) {
            for ($c = $right; $c >= $left; $c--) $mat[$bottom][$c] = $val++;
            $bottom--;
        }
        if ($left <= $right) {
            for ($r = $bottom; $r >= $top; $r--) $mat[$r][$left] = $val++;
            $left++;
        }
    }
    return $mat;
}

// 6) Chemins grille (droite/bas) — DP
// Nombre de chemins de (0,0) à (m,n) avec mouvements droite/bas seulement.
function gridPaths(int $m, int $n): int {
    $dp = array_fill(0, $m + 1, array_fill(0, $n + 1, 0));
    for ($i = 0; $i <= $m; $i++) $dp[$i][0] = 1;
    for ($j = 0; $j <= $n; $j++) $dp[0][j] = 1;
    for ($i = 1; $i <= $m; $i++) {
        for ($j = 1; $j <= $n; $j++) {
            $dp[$i][j] = $dp[$i-1][j] + $dp[$i][j-1];
        }
    }
    return $dp[$m][ $n];
}

// 7) Tri fusion (merge sort)
function mergeSort(array $arr): array {
    $n = count($arr);
    if ($n <= 1) return $arr;
    $mid = intdiv($n, 2);
    $left = mergeSort(array_slice($arr, 0, $mid));
    $right = mergeSort(array_slice($arr, $mid));
    return mergeArrays($left, $right);
}
function mergeArrays(array $a, array $b): array {
    $i = $j = 0; $out = [];
    $na = count($a); $nb = count($b);
    while ($i < $na && $j < $nb) {
        if ($a[$i] <= $b[$j]) $out[] = $a[$i++]; else $out[] = $b[$j++];
    }
    while ($i < $na) $out[] = $a[$i++];
    while ($j < $nb) $out[] = $b[$j++];
    return $out;
}

// // TESTS RAPIDES
// var_dump(areAmicable(220, 284)); // true
// var_dump(longestCollatzUpTo(100000));
// var_dump(roundRobinPairs(['A','B','C'])); // [[A,B],[A,C],[B,C]]
// var_dump(lcs("abcde","ace")); // "ace"
// print_r(spiralMatrix(3));
// var_dump(gridPaths(2,2)); // 6
// var_dump(mergeSort([5,2,9,1])); // [1,2,5,9]
```

---

## 🎯 Bonus / Mini-projet — Sudoku Simplifié (Validation)

```php
<?php
// Règles :
// - Grille 9x9, char '1'..'9' ou '.' (vide) (vous pouvez aussi accepter 0).
// - Valide si aucune ligne/colonne/boîte 3x3 ne contient de doublon (hors vides).

function unitIsValid(array $unit): bool {
    $seen = [];
    foreach ($unit as $cell) {
        if ($cell === '.' || $cell === '0' || $cell === 0) continue;
        if (!ctype_digit((string)$cell)) return false; // sécurité
        if ($cell < 1 || $cell > 9) return false;
        if (isset($seen[$cell])) return false;
        $seen[$cell] = true;
    }
    return true;
}

function getBox(array $grid, int $boxRow, int $boxCol): array {
    $out = [];
    $startR = $boxRow * 3;
    $startC = $boxCol * 3;
    for ($r = 0; $r < 3; $r++) {
        for ($c = 0; $c < 3; $c++) {
            $out[] = $grid[$startR + $r][$startC + $c];
        }
    }
    return $out;
}

function estSudokuValide(array $grid): bool {
    // Vérifier dimension 9x9
    if (count($grid) !== 9) return false;
    for ($r = 0; $r < 9; $r++) if (count($grid[$r]) !== 9) return false;

    // Lignes
    for ($r = 0; $r < 9; $r++) {
        if (!unitIsValid($grid[$r])) return false;
    }
    // Colonnes
    for ($c = 0; $c < 9; $c++) {
        $col = [];
        for ($r = 0; $r < 9; $r++) $col[] = $grid[$r][$c];
        if (!unitIsValid($col)) return false;
    }
    // Boîtes 3x3
    for ($br = 0; $br < 3; $br++) {
        for ($bc = 0; $bc < 3; $bc++) {
            if (!unitIsValid(getBox($grid, $br, $bc))) return false;
        }
    }
    return true;
}

// // EXEMPLE
// $grid = [
//     ['5','3','.','.','7','.','.','.','.'],
//     ['6','.','.','1','9','5','.','.','.'],
//     ['.','9','8','.','.','.','.','6','.'],
//     ['8','.','.','.','6','.','.','.','3'],
//     ['4','.','.','8','.','3','.','.','1'],
//     ['7','.','.','.','2','.','.','.','6'],
//     ['.','6','.','.','.','.','2','8','.'],
//     ['.','.','.','4','1','9','.','.','5'],
///     ['.','.','.','.','8','.','.','7','9'],
// ];
// var_dump(estSudokuValide($grid)); // true
```

---

## 🧠 Notes & bonnes pratiques

- **Clarté d’abord** : privilégiez des solutions lisibles, puis optimisez si nécessaire.  
- **Cas limites** : tableaux vides, singleton, valeurs négatives, `n=0`.  
- **Complexité** : annoncez votre ordre de grandeur (`O(n)`, `O(n log n)`, …).  
- **Tests** : ajoutez des `var_dump`/`assert` pour sécuriser vos fonctions.
