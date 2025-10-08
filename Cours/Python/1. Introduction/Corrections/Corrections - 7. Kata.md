# <span style="color:red;">Corrections — Exercices “Kata”</span> 📘

> Python 3.x — Fonctions pures, robustes et testables.  
> Chaque bloc inclut des exemples d’usage + **Idée clé**, **Complexité**, **Bords de cas**.

---

## 🧩 Niveau 1 — Mise en route (bases propres)

### 1) Pairs / Impairs (compteur)
```python
from typing import Iterable, Dict, List, Tuple, Any, Callable, Union

def compter_pairs_impairs(arr: Iterable[int]) -> Dict[str, object]:
    """
    Compte pairs/impairs et renvoie aussi les listes correspondantes.
    Contraintes: entiers (bool exclus).
    Return: {"pairs": int, "impairs": int, "list_pairs": List[int], "list_impairs": List[int]}
    """
    pairs_list: List[int] = []
    impairs_list: List[int] = []
    for x in arr:
        if not isinstance(x, int) or isinstance(x, bool):
            raise ValueError(f"Valeur non entière: {x!r}")
        (pairs_list if x % 2 == 0 else impairs_list).append(x)
    return {
        "pairs": len(pairs_list),
        "impairs": len(impairs_list),
        "list_pairs": pairs_list,
        "list_impairs": impairs_list,
    }

# Démo
print(compter_pairs_impairs([1,2,3,4]))  # {'pairs': 2, 'impairs': 2, ...}
```
- **Idée clé :** partitionner la séquence une seule fois en deux listes (pair/impair).
- **Complexité :** temps O(n) ; espace O(n) pour stocker les deux listes.
- **Bords de cas :** liste vide → compte 0/0 ; valeurs non entières → `ValueError` ; très grands entiers OK.

---

### 2) Première valeur > seuil (et dernier)
```python
def premier_sup(arr: Iterable[int], seuil: int) -> int:
    """Index de la 1re valeur strictement > seuil, sinon -1."""
    for i, v in enumerate(arr):
        if v > seuil:
            return i
    return -1

def dernier_sup(arr: Iterable[int], seuil: int) -> int:
    """Index de la dernière valeur strictement > seuil, sinon -1."""
    idx = -1
    for i, v in enumerate(arr):
        if v > seuil:
            idx = i
    return idx

# Démo
print(premier_sup([1,3,7,4], 5))  # 2
print(dernier_sup([1,3,7,4], 5))  # 2
```
- **Idée clé :** scan linéaire ; pour le dernier, garder le dernier index valable.
- **Complexité :** O(n) temps ; O(1) espace.
- **Bords de cas :** liste vide → -1 ; tous ≤ seuil → -1 ; seuil négatif/positif gérés pareil.

---

### 3) Remplacement conditionnel
```python
def remplacer_negatifs_par_zero(arr: Iterable[int]) -> List[int]:
    """Remplace chaque nombre négatif par 0 (retourne une nouvelle liste)."""
    return [0 if x < 0 else x for x in arr]

Replacement = Union[Any, Callable[[Any], Any]]

def remplacer_si(arr: Iterable[Any],
                 predicate: Callable[[Any], bool],
                 replacement: Replacement) -> List[Any]:
    """
    Règle paramétrable.
    - predicate(x): bool
    - replacement: valeur OU fonction f(x)->valeur
    """
    out: List[Any] = []
    for x in arr:
        if predicate(x):
            out.append(replacement(x) if callable(replacement) else replacement)
        else:
            out.append(x)
    return out

# Démo
print(remplacer_negatifs_par_zero([3,-1,4,-5]))         # [3,0,4,0]
print(remplacer_si([3,-1,4,-5], lambda x: x<0, 0))      # [3,0,4,0]
print(remplacer_si([1,2,3], lambda x: x%2==0, lambda x: x*100))  # [1,200,3]
```
- **Idée clé :** appliquer une règle de substitution via prédicat (fonction pure).
- **Complexité :** O(n) temps ; O(n) espace (nouvelle liste).
- **Bords de cas :** liste vide ; `replacement` fonction/valeur ; types hétérogènes autorisés par la version générique.

---

### 4) Intercaler un séparateur entre caractères
```python
def intercaler(sep: str, s: str) -> str:
    """
    'code','-' -> 'c-o-d-e'
    Ne met ni au début ni à la fin. Gère la chaîne vide.
    """
    return sep.join(list(s))

# Démo
print(intercaler("-", "code"))  # c-o-d-e
print(intercaler("-", ""))      # ""
```
- **Idée clé :** `sep.join` sur l’itérable de caractères.
- **Complexité :** O(n) temps/espace.
- **Bords de cas :** chaîne vide → `""` ; séparateur vide → identique à l’entrée.

---

### 5) Différences absolues voisines (+ somme)
```python
def diff_voisins(arr: Iterable[int]) -> List[int]:
    """Renvoie |a[i]-a[i-1]| pour i=1..n-1"""
    arr = list(arr)
    return [abs(arr[i] - arr[i-1]) for i in range(1, len(arr))]

def diff_voisins_avec_somme(arr: Iterable[int]) -> Tuple[List[int], int]:
    diffs = diff_voisins(arr)
    return diffs, sum(diffs)

# Démo
print(diff_voisins([5,2,9]))              # [3,7]
print(diff_voisins_avec_somme([5,2,9]))   # ([3,7], 10)
```
- **Idée clé :** dérivée discrète absolue entre voisins.
- **Complexité :** O(n) temps ; O(n) espace pour la liste des différences.
- **Bords de cas :** longueur 0/1 → `[]` et somme `0`.

---

### 6) Compter chiffres d’un entier (sans str)
```python
def nb_chiffres(n: int) -> int:
    """
    Nombre de chiffres en base 10. 0 → 1. Supporte négatifs. Sans conversion str.
    """
    n = abs(n)
    if n == 0:
        return 1
    c = 0
    while n > 0:
        n //= 10
        c += 1
    return c

# Démo
print(nb_chiffres(12034))  # 5
print(nb_chiffres(-7))     # 1
print(nb_chiffres(0))      # 1
```
- **Idée clé :** divisions entières successives (logarithme en base 10 implicite).
- **Complexité :** O(log₁₀|n|) temps ; O(1) espace.
- **Bords de cas :** n=0 ; n<0 ; très grands entiers Python OK.

---

### 7) Table de multiplication simple (bornes 1..k)
```python
def table_multiplication(n: int, k: int = 10) -> List[str]:
    """Retourne ['n x 1 = ...', ..., 'n x k = ...']"""
    return [f"{n} x {i} = {n*i}" for i in range(1, k+1)]

# Démo
print(table_multiplication(3)[:3])   # ['3 x 1 = 3', '3 x 2 = 6', '3 x 3 = 9']
print(table_multiplication(5, k=5))
```
- **Idée clé :** compréhension de liste sur la plage 1..k.
- **Complexité :** O(k) temps/espace.
- **Bords de cas :** k<1 → renvoie `[]` (si on l’autorise en changeant la plage) ; n négatif/0 autorisés.

---

## 🔤 Niveau 2 — Chaînes & parcours

### 1) Isogramme (+ premier doublon)
```python
from typing import Optional

def est_isogramme(s: str) -> Dict[str, Optional[object]]:
    """
    Ignore casse/espaces. Renvoie {"isogramme": bool, "doublon": Optional[str]}
    """
    seen = set()
    for ch in s.lower():
        if ch == " ":
            continue
        if ch in seen:
            return {"isogramme": False, "doublon": ch}
        seen.add(ch)
    return {"isogramme": True, "doublon": None}

# Démo
print(est_isogramme("lumberjacks"))
print(est_isogramme("Hello"))  # doublon 'l'
```
- **Idée clé :** détection de doublon via ensemble (hashset).
- **Complexité :** O(n) temps ; O(min(n, alphabet)) espace.
- **Bords de cas :** chaîne vide → isogramme True ; caractères spéciaux ignorés ici seulement pour espace (adapter au besoin).

---

### 2) Pangramme (FR/EN) + lettres manquantes
```python
import unicodedata
import string

def _normalize_letters(text: str) -> str:
    # retire accents, garde lettres a-z
    t = unicodedata.normalize("NFD", text)
    t = "".join(c for c in t if unicodedata.category(c) != "Mn")
    t = t.lower()
    return "".join(c for c in t if "a" <= c <= "z")

def est_pangramme(s: str, alphabet: str = "en") -> Dict[str, object]:
    """
    alphabet: 'en' ou 'fr' (26 lettres a-z après normalisation).
    Renvoie {"pangramme": bool, "manquantes": set[str]}
    """
    letters = set(_normalize_letters(s))
    ref = set(string.ascii_lowercase)  # 26 lettres
    manquantes = ref - letters
    return {"pangramme": len(manquantes) == 0, "manquantes": manquantes}

# Démo
print(est_pangramme("Portez ce vieux whisky au juge blond qui fume"))
```
- **Idée clé :** normaliser (accents → base), comparer à l’alphabet.
- **Complexité :** O(n) temps ; O(1) espace (alphabet taille fixe).
- **Bords de cas :** accents/ponctuation ; chiffres ignorés ; texte court → manquantes=alphabet.

---

### 3) Miroir de mots (reverse chaque mot, normaliser espaces)
```python
def miroir_mots(s: str) -> str:
    """
    Inverse chaque mot, conserve l'ordre des mots. Espaces multiples normalisés (split/join).
    """
    mots = s.split()  # normalise espaces
    return " ".join(m[::-1] for m in mots)

# Démo
print(miroir_mots("Bonjour   tout   le  monde"))  # 'ruojnoB tuot el ednom'
```
- **Idée clé :** `split()` puis inversion caractère par caractère, `join` pour recomposer.
- **Complexité :** O(n) temps/espace.
- **Bords de cas :** chaînes avec espaces multiples/leading/trailing ; chaîne vide → "".

---

### 4) Subsequence (inclusion ordonnée) + indices
```python
def est_sous_sequence(a: str, b: str) -> Dict[str, object]:
    """
    a est-il sous-séquence de b ? Renvoie {"ok": bool, "indices": List[int]}
    indices = positions dans b où les caractères de a ont été trouvés (si ok).
    """
    indices = []
    j = 0
    for i, ch in enumerate(b):
        if j < len(a) and ch == a[j]:
            indices.append(i)
            j += 1
            if j == len(a):
                return {"ok": True, "indices": indices}
    return {"ok": False, "indices": []}

# Démo
print(est_sous_sequence("abc", "ahbgdc"))  # ok True
print(est_sous_sequence("axc", "ahbgdc"))  # False
```
- **Idée clé :** deux pointeurs (sur a et b).
- **Complexité :** O(|b|) temps ; O(|a|) espace pour indices.
- **Bords de cas :** a vide → True (indices `[]`) ; a plus long que b → False.

---

### 5) Bigrammes (fréquences) + top-k
```python
from collections import Counter
from typing import Mapping, Tuple, List

def bigrammes_freq(s: str) -> Mapping[str, int]:
    """
    Compte les paires adjacentes (ignorer espaces), case-insensible.
    Ex: 'abba' -> {'ab':1,'bb':1,'ba':1}
    """
    s = s.replace(" ", "").lower()
    return Counter(s[i:i+2] for i in range(len(s)-1)) if len(s) >= 2 else Counter()

def top_k_bigrammes(s: str, k: int) -> List[Tuple[str, int]]:
    c = bigrammes_freq(s)
    return c.most_common(k)

# Démo
print(bigrammes_freq("abba"))
print(top_k_bigrammes("abbaabbab", 2))
```
- **Idée clé :** glissement de fenêtre de taille 2, `Counter` pour fréquences.
- **Complexité :** comptage O(n) ; top-k via `most_common` O(n log n) (implémentation dépendante).
- **Bords de cas :** n<2 → Counter vide ; ponctuation → ici conservée (adapter si besoin).

---

### 6) ROT13 (préserve casse, ponctuation)
```python
def rot13(s: str) -> str:
    out = []
    for ch in s:
        if "a" <= ch <= "z":
            out.append(chr((ord(ch) - 97 + 13) % 26 + 97))
        elif "A" <= ch <= "Z":
            out.append(chr((ord(ch) - 65 + 13) % 26 + 65))
        else:
            out.append(ch)
    return "".join(out)

# Démo
print(rot13("Hello, World!"))  # Uryyb, Jbeyq!
```
- **Idée clé :** décalage circulaire de 13 positions pour lettres A-Z/a-z.
- **Complexité :** O(n) temps/espace.
- **Bords de cas :** caractères non alphabétiques laissés tels quels ; lettres accentuées non gérées.

---

### 7) Suppression doublons consécutifs + total supprimé
```python
def dedupe_consecutifs(s: str) -> Dict[str, object]:
    """
    Conserve 1 char par run. Renvoie {"result": str, "suppr": int}
    """
    if not s:
        return {"result": "", "suppr": 0}
    res = [s[0]]
    suppr = 0
    for ch in s[1:]:
        if ch == res[-1]:
            suppr += 1
        else:
            res.append(ch)
    return {"result": "".join(res), "suppr": suppr}

# Démo
print(dedupe_consecutifs("aaabccddd"))  # {'result': 'abcd', 'suppr': 4}
```
- **Idée clé :** compresser les runs de caractères identiques adjacents.
- **Complexité :** O(n) temps ; O(n) espace (résultat).
- **Bords de cas :** chaîne vide ; chaîne d’un seul caractère ; toute la chaîne identique.

---

## 🧮 Niveau 3 — Tableaux & logique

### 1) Regroupement stable pairs/impairs (+ prédicat générique)
```python
def stable_pairs_impairs(arr: Iterable[int]) -> List[int]:
    """Pairs puis impairs, en conservant l'ordre relatif initial (stable)."""
    arr = list(arr)
    pairs  = [x for x in arr if x % 2 == 0]
    impairs= [x for x in arr if x % 2 != 0]
    return pairs + impairs

from typing import Callable, Iterable, List

def stable_partition(arr: Iterable, predicate: Callable[[object], bool]) -> List:
    """Générique: éléments satisfaisant predicate d'abord, puis les autres, ordre stable."""
    arr = list(arr)
    t = [x for x in arr if predicate(x)]
    f = [x for x in arr if not predicate(x)]
    return t + f

# Démo
print(stable_pairs_impairs([3,2,4,1]))  # [2,4,3,1]
print(stable_partition(["Alice","Bob","Chloé"], lambda s: s.startswith("B")))
```
- **Idée clé :** partition stable par filtrage double.
- **Complexité :** O(n) temps ; O(n) espace.
- **Bords de cas :** tous satisfont / aucun ne satisfait → liste inchangée à l’ordre près ; éléments non hashables OK (pas de set).

---

### 2) Compresser runs + décompresser
```python
def rle_compresser(arr: Iterable) -> List[Tuple[object, int]]:
    """Run-Length Encoding: [1,1,1,2,2,3] -> [(1,3),(2,2),(3,1)]"""
    arr = list(arr)
    if not arr:
        return []
    out: List[Tuple[object, int]] = []
    cur, cnt = arr[0], 1
    for x in arr[1:]:
        if x == cur:
            cnt += 1
        else:
            out.append((cur, cnt))
            cur, cnt = x, 1
    out.append((cur, cnt))
    return out

def rle_decompresser(paires: Iterable[Tuple[object, int]]) -> List:
    out: List = []
    for val, cnt in paires:
        out.extend([val]*cnt)
    return out

# Démo
enc = rle_compresser([1,1,1,2,2,3])
print(enc)
print(rle_decompresser(enc))
```
- **Idée clé :** RLE (Run-Length Encoding) ; inverse par réplication.
- **Complexité :** compression O(n), décompression O(∑counts) ; espace O(n).
- **Bords de cas :** liste vide ; alternance totale (pas de gain) ; valeurs non comparables → nécessite `==` défini.

---

### 3) Rotation en place (droite/gauche)
```python
def _reverse(a: List, i: int, j: int) -> None:
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1; j -= 1

def rotate_right_in_place(a: List, k: int) -> None:
    """Rotation à droite de k, en place. k modulo n."""
    n = len(a)
    if n == 0: return
    k %= n
    if k == 0: return
    _reverse(a, 0, n-1)
    _reverse(a, 0, k-1)
    _reverse(a, k, n-1)

def rotate_left_in_place(a: List, k: int) -> None:
    """Rotation à gauche de k, en place."""
    n = len(a)
    rotate_right_in_place(a, n - (k % n) if n else 0)

# Démo
arr = [1,2,3,4,5]
rotate_right_in_place(arr, 2)
print(arr)  # [4,5,1,2,3]
rotate_left_in_place(arr, 2)
print(arr)  # back to [1,2,3,4,5]
```
- **Idée clé :** triple inversion pour rotation O(1) espace.
- **Complexité :** O(n) temps ; O(1) espace.
- **Bords de cas :** k multiple de n ; n=0/1 ; k négatif (normaliser au besoin).

---

### 4) Intersection avec multiplicité + différence multiset
```python
from collections import Counter

def multiset_intersection(a: Iterable, b: Iterable) -> List:
    ca, cb = Counter(a), Counter(b)
    inter = ca & cb
    out: List = []
    for val, cnt in inter.items():
        out.extend([val]*cnt)
    return out

def multiset_difference(a: Iterable, b: Iterable) -> List:
    """
    A \ B avec multiplicité (retire jusqu'à min(occA,occB) pour chaque valeur)
    """
    ca, cb = Counter(a), Counter(b)
    diff = ca - cb
    out: List = []
    for val, cnt in diff.items():
        out.extend([val]*cnt)
    return out

# Démo
print(multiset_intersection([1,2,2,3],[2,2,2]))  # [2,2]
print(multiset_difference([1,2,2,3],[2,2,2]))    # [1,3]
```
- **Idée clé :** utiliser `Counter` et opérations & / -.
- **Complexité :** O(n+m) temps ; O(u) espace avec u=valeurs uniques.
- **Bords de cas :** listes vides ; types non hashables → non supportés par Counter.

---

### 5) Produit sauf soi-même (sans division)
```python
def produit_sauf_soi(a: List[int]) -> List[int]:
    """
    Pour chaque i, produit de tous les éléments sauf a[i].
    Gère 0 multiples naturellement.
    """
    n = len(a)
    if n == 0: return []
    out = [1]*n
    # préfixes
    p = 1
    for i in range(n):
        out[i] = p
        p *= a[i]
    # suffixes
    s = 1
    for i in range(n-1, -1, -1):
        out[i] *= s
        s *= a[i]
    return out

# Démo
print(produit_sauf_soi([1,2,3,4]))    # [24,12,8,6]
print(produit_sauf_soi([0,2,3,4]))    # [24,0,0,0]
print(produit_sauf_soi([0,2,0,4]))    # [0,0,0,0]
```
- **Idée clé :** préfixes × suffixes pour éviter la division.
- **Complexité :** O(n) temps ; O(1) extra (hors sortie).
- **Bords de cas :** zéro(s) dans le tableau ; tableau vide.

---

### 6) Somme diagonales (matrice carrée) + |diff|
```python
def diag_sum(m: List[List[int]]) -> Dict[str, int]:
    n = len(m)
    princ = sum(m[i][i] for i in range(n))
    sec   = sum(m[i][n-1-i] for i in range(n))
    return {"principale": princ, "secondaire": sec, "abs_diff": abs(princ-sec)}

# Démo
mat = [[1,2,3],[4,5,6],[7,8,9]]
print(diag_sum(mat))  # {'principale':15,'secondaire':15,'abs_diff':0}
```
- **Idée clé :** indices (i,i) et (i,n-1-i).
- **Complexité :** O(n) temps ; O(1) espace (n = dimension).
- **Bords de cas :** matrice vide / non carrée → à valider en amont ; n=1.

---

### 7) Sous-tableau le plus long sans répétition (longueur + indices)
```python
def plus_long_sans_repetition(a: List) -> Dict[str, object]:
    """
    Sliding window. Renvoie {"longueur": L, "indices": [l,r]} avec r inclus.
    Si plusieurs max, renvoie le 1er.
    """
    seen = {}
    l = 0
    best_len = 0
    best_lr = [0, -1]
    for r, val in enumerate(a):
        if val in seen and seen[val] >= l:
            l = seen[val] + 1
        seen[val] = r
        if r - l + 1 > best_len:
            best_len = r - l + 1
            best_lr = [l, r]
    return {"longueur": best_len, "indices": best_lr}

# Démo
print(plus_long_sans_repetition([1,2,1,3,2,3]))  # longueur 3, indices ex: [1,3]
```
- **Idée clé :** fenêtre glissante + dernière position vue.
- **Complexité :** O(n) temps ; O(min(n, alphabet)) espace.
- **Bords de cas :** liste vide ; tous uniques → toute la liste ; tous identiques → 1.

---

## 🧠 Niveau 4 — Algo intermédiaire

### 1) Trois nombres = cible (3-Sum) + version bool
```python
def trois_sum(nums: List[int], cible: int = 0) -> List[List[int]]:
    """
    Tous les triplets triés sans doublons qui somment à cible.
    """
    nums.sort()
    n = len(nums)
    res: List[List[int]] = []
    for i in range(n-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        a = nums[i]
        l, r = i+1, n-1
        while l < r:
            s = a + nums[l] + nums[r]
            if s == cible:
                res.append([a, nums[l], nums[r]])
                l += 1; r -= 1
                while l < r and nums[l] == nums[l-1]: l += 1
                while l < r and nums[r] == nums[r+1]: r -= 1
            elif s < cible:
                l += 1
            else:
                r -= 1
    return res

def existe_trois_sum(nums: List[int], cible: int = 0) -> bool:
    return len(trois_sum(nums, cible)) > 0

# Démo
print(trois_sum([-1,0,1,2,-1,-4], 0))
print(existe_trois_sum([-1,0,1,2,-1,-4], 0))
```
- **Idée clé :** tri + deux pointeurs ; sauter doublons.
- **Complexité :** O(n²) temps ; O(1) espace (hors sorties).
- **Bords de cas :** <3 éléments → `[]` ; multiples doublons → gestion stricte des sauts.

---

### 2) Fusion d’intervalles + trous
```python
def fusion_intervalles(intervals: List[List[int]]) -> List[List[int]]:
    if not intervals: return []
    intervals = sorted(intervals)
    merged = [intervals[0][:]]
    for s, e in intervals[1:]:
        if s <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], e)
        else:
            merged.append([s, e])
    return merged

def trous_intervalles(intervals: List[List[int]]) -> List[List[int]]:
    """
    Renvoie les "trous" entre intervalles après fusion.
    """
    m = fusion_intervalles(intervals)
    gaps: List[List[int]] = []
    for i in range(len(m)-1):
        a, b = m[i][1], m[i+1][0]
        if a < b:
            gaps.append([a, b])
    return gaps

# Démo
print(fusion_intervalles([[1,3],[2,6],[8,10],[15,18]]))   # [[1,6],[8,10],[15,18]]
print(trous_intervalles([[1,3],[2,6],[8,10],[15,18]]))    # [[6,8],[10,15]]
```
- **Idée clé :** trier, fusionner en balayant ; trous = espaces entre blocs fusionnés.
- **Complexité :** O(n log n) temps (tri) ; O(n) espace.
- **Bords de cas :** intervalles déjà triés/sans chevauchement ; intervalles invalides (s>e) → valider en amont.

---

### 3) k-ième plus petit (Quickselect) + plus grand
```python
import random

def quickselect_kth_smallest(a: List[int], k: int) -> int:
    """
    k est 1-based: k=1 -> plus petit.
    Modifie potentiellement l'ordre (partition in-place style).
    """
    if not 1 <= k <= len(a):
        raise ValueError("k hors bornes")
    l, r = 0, len(a)-1
    while True:
        pivot = a[random.randint(l, r)]
        i, j = l, r
        while i <= j:
            while a[i] < pivot: i += 1
            while a[j] > pivot: j -= 1
            if i <= j:
                a[i], a[j] = a[j], a[i]
                i += 1; j -= 1
        if k-1 <= j:
            r = j
        elif k-1 >= i:
            l = i
        else:
            return a[k-1]

def quickselect_kth_largest(a: List[int], k: int) -> int:
    """k-ème plus grand (1-based)."""
    return quickselect_kth_smallest(a, len(a) - k + 1)

# Démo
print(quickselect_kth_smallest([7,10,4,3,20,15], 3))  # 7
print(quickselect_kth_largest([7,10,4,3,20,15], 2))   # 15
```
- **Idée clé :** partition aléatoire façon Quicksort mais sur cible unique.
- **Complexité :** temps attendu O(n), pire cas O(n²) ; espace O(1).
- **Bords de cas :** k hors bornes → `ValueError` ; doublons gérés ; liste vide.

---

### 4) Puissance rapide (exponentiation binaire) + exposants négatifs
```python
def pow_fast(base: float, exp: int) -> float:
    if exp == 0:
        return 1.0
    if exp < 0:
        if base == 0:
            raise ZeroDivisionError("0**neg")
        return 1.0 / pow_fast(base, -exp)
    res = 1.0
    b = base
    e = exp
    while e > 0:
        if e & 1:
            res *= b
        b *= b
        e >>= 1
    return res

# Démo
print(pow_fast(2, 10))   # 1024.0
print(pow_fast(2, -3))   # 0.125
```
- **Idée clé :** décomposition binaire de l’exposant (exponentiation rapide).
- **Complexité :** O(log |exp|) temps ; O(1) espace.
- **Bords de cas :** base=0 et exp<0 → erreur ; exp=0 → 1 ; exp négatifs → inverser.

---

### 5) Collatz — nombre d’étapes (+ mémo plage)
```python
def collatz_steps(n: int) -> int:
    """Nombre d'étapes pour atteindre 1 (n>=1)."""
    if n < 1:
        raise ValueError("n doit être >= 1")
    steps = 0
    x = n
    while x != 1:
        x = (x // 2) if (x % 2 == 0) else (3*x + 1)
        steps += 1
    return steps

def collatz_steps_memo(N: int) -> Dict[int, int]:
    """
    Mémo pour 1..N. Retourne un dict {n: steps}.
    """
    memo = {1: 0}
    for n in range(2, N+1):
        x = n
        path = []
        while x not in memo:
            path.append(x)
            x = (x // 2) if (x % 2 == 0) else (3*x + 1)
        base = memo[x]
        for i, val in enumerate(reversed(path), start=1):
            memo[val] = base + i
    return memo

# Démo
print(collatz_steps(12))       # 9
print(collatz_steps_memo(20)[12])
```
- **Idée clé :** itérer la suite ; mémo pour réutiliser des sous-résultats.
- **Complexité :** par n, empirique O(log n) en moyenne ; mémo 1..N ~ O(N log N) approx.; espace O(N).
- **Bords de cas :** n<1 → erreur ; grands n → attention à l’explosion temporaire.

---

### 6) Sous-tableau somme max (Kadane + indices)
```python
def kadane_indices(a: List[int]) -> Dict[str, object]:
    """
    Renvoie {"somme": best, "indices": [l, r]} (r inclus).
    Gère le cas tout négatif (prend le max élément).
    """
    if not a:
        return {"somme": 0, "indices": [-1, -1]}
    best = a[0]
    cur = a[0]
    cur_l = 0
    best_l = best_r = 0
    for i in range(1, len(a)):
        if cur + a[i] < a[i]:
            cur = a[i]
            cur_l = i
        else:
            cur += a[i]
        if cur > best:
            best = cur
            best_l, best_r = cur_l, i
    return {"somme": best, "indices": [best_l, best_r]}

# Démo
print(kadane_indices([-2,1,-3,4,-1,2,1,-5,4]))  # somme 6, indices [3,6]
print(kadane_indices([-5,-2,-7]))               # somme -2, indices [1,1]
```
- **Idée clé :** DP en ligne (garder suffixe optimal + meilleur global).
- **Complexité :** O(n) temps ; O(1) espace.
- **Bords de cas :** tableau vide ; tout négatif → max élément ; multiples sous-tableaux équivalents.

---

### 7) Majorité relative (> n/3) — Boyer-Moore étendu + vérif
```python
def majorite_n_sur_3(nums: List[int]) -> List[int]:
    """
    Éléments apparaissant strictement plus que n/3 fois (0,1, ou 2).
    """
    if not nums:
        return []
    c1 = c2 = None
    n1 = n2 = 0
    for x in nums:
        if c1 == x:
            n1 += 1
        elif c2 == x:
            n2 += 1
        elif n1 == 0:
            c1, n1 = x, 1
        elif n2 == 0:
            c2, n2 = x, 1
        else:
            n1 -= 1; n2 -= 1
    # vérification
    res = []
    for c in (c1, c2):
        if c is not None and nums.count(c) > len(nums)//3:
            if c not in res:
                res.append(c)
    return res

# Démo
print(majorite_n_sur_3([1,2,3,1,2,1,1]))      # [1]
print(majorite_n_sur_3([1,2,3,1,2,1,2,2]))    # [1,2] ou [2,1]
```
- **Idée clé :** au plus 2 candidats > n/3 ; sélectionner puis vérifier.
- **Complexité :** O(n) + O(n) (vérif) = O(n) ; espace O(1).
- **Bords de cas :** liste vide ; aucun élément majoritaire ; doublons massifs.

---

## 🎯 Bonus — Mini-projet Mastermind (chiffres)

### Logique pure (génération, évaluation, filtrage)
```python
import random
from typing import Callable, List, Dict

def generer_secret(longueur: int = 4, digits: str = "0123456789", unique: bool = False) -> str:
    """
    Génère un code secret numérique (chaîne).
    - unique=False: doublons autorisés
    - unique=True : chiffres tous distincts
    """
    if unique:
        if longueur > len(digits):
            raise ValueError("longueur > nb de chiffres disponibles pour unique=True")
        return "".join(random.sample(digits, longueur))
    return "".join(random.choice(digits) for _ in range(longueur))

def evaluer(secret: str, proposition: str) -> Dict[str, int]:
    """
    Retourne {bienPlace, malPlace} (type Bulls/Cows).
    malPlace = bons chiffres aux mauvaises positions (sans compter les bien placés).
    """
    if len(secret) != len(proposition):
        raise ValueError("Longueurs différentes")
    bien = sum(1 for a,b in zip(secret, proposition) if a == b)
    from collections import Counter
    cs, cg = Counter(secret), Counter(proposition)
    total_bons = sum(min(cs[d], cg[d]) for d in cs.keys() | cg.keys())
    mal = total_bons - bien
    return {"bienPlace": bien, "malPlace": mal}

def filtrer_candidats(candidats: List[str],
                      guess: str,
                      feedback: Dict[str, int]) -> List[str]:
    """Élimine les codes incompatibles avec le feedback fourni."""
    bp, mp = feedback["bienPlace"], feedback["malPlace"]
    out = []
    for cand in candidats:
        if evaluer(cand, guess) == {"bienPlace": bp, "malPlace": mp}:
            out.append(cand)
    return out

def generer_tous_codes(longueur: int = 4, digits: str = "0123456789", unique: bool = False) -> List[str]:
    """Espace de recherche (10**longueur si unique=False)."""
    if unique:
        from itertools import permutations
        return ["".join(p) for p in permutations(digits, longueur)]
    else:
        from itertools import product
        return ["".join(p) for p in product(digits, repeat=longueur)]
```
- **Idée clé :** séparer logique pure (génération, évaluation, filtrage) de l’I/O.
- **Complexité :**
  - `evaluer` O(L) temps, O(1) espace (alphabet 10).
  - `filtrer_candidats` O(C·L) pour C candidats.
  - `generer_tous_codes` : taille 10^L (ou P(10,L) en unique).
- **Bords de cas :** longueurs différentes → erreur ; doublons autorisés/non selon mode ; alphabet restreint.

### Boucle de jeu (console optionnelle) & mode assistant
```python
def partie_console(secret: str | None = None, essais_max: int = 8) -> None:
    """
    Partie console minimaliste (peut être commentée si I/O non souhaitée).
    """
    secret = secret or generer_secret()
    print("Mastermind chiffres — devine le code de 4 chiffres. 'quit' pour sortir.")
    for essai in range(1, essais_max+1):
        guess = input(f"[{essai}/{essais_max}] Proposition: ").strip()
        if guess.lower() == "quit":
            print("Fin.")
            return
        if not (guess.isdigit() and len(guess) == len(secret)):
            print("Entrée invalide.")
            continue
        fb = evaluer(secret, guess)
        print(f"→ bienPlace={fb['bienPlace']}, malPlace={fb['malPlace']}")
        if fb["bienPlace"] == len(secret):
            print(f"🎉 Gagné en {essai} essai(s) ! Secret: {secret}")
            return
    print(f"Perdu. Secret: {secret}")

def assistant_naif(longueur: int = 4, essais_max: int = 8, unique: bool = False) -> None:
    """
    Démo: l'assistant tente de déduire un secret inconnu en filtrant l'espace des candidats
    via les feedbacks obtenus (naïf: premier candidat restant).
    """
    secret = generer_secret(longueur, unique=unique)
    candidats = generer_tous_codes(longueur, unique=unique)
    historique = []

    for essai in range(1, essais_max+1):
        guess = candidats[0]  # stratégie naïve: premier restant
        fb = evaluer(secret, guess)
        historique.append((guess, fb))
        print(f"[{essai}] guess={guess} -> bp={fb['bienPlace']}, mp={fb['malPlace']} (restants={len(candidats)})")
        if fb["bienPlace"] == longueur:
            print(f"✅ Trouvé en {essai} essai(s): {secret}")
            break
        candidats = filtrer_candidats(candidats, guess, fb)
    else:
        print(f"❌ Non trouvé en {essais_max} essais. Secret: {secret}")
    for g, f in historique:
        print(f"{g} -> {f}")

# Démo non interactive (commentée par défaut)
# partie_console()               # ← décommentez pour jouer
# assistant_naif(longueur=4)     # exploration naïve
```
- **Idée clé :** boucle (proposer → évaluer → filtrer) ; historique des essais.
- **Complexité :** assistant naïf ~ itérations × coût de filtrage O(C·L) décroissant ; génération exhaustive coûteuse (10^L).
- **Bords de cas :** essais_max insuffisant ; espace de recherche énorme ; entrées invalides côté console.

---
