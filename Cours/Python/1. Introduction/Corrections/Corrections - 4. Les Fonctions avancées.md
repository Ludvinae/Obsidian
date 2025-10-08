# <span style="color:red;">Les Fonctions Avancées : Corrections</span> 📘

---

## <span style="color:red;">Correction — Exercice 1 : `*args` et `**kwargs`</span> 🧺

```python
from copy import copy

def additionner(*nombres: float) -> float:
    """Retourne la somme de tous les nombres passés (0 si aucun)."""
    return sum(nombres)  # sum(()) == 0

def fusion_config(base: dict, **overrides) -> dict:
    """
    Retourne un nouveau dict fusionnant base et overrides, sans modifier base.
    Affiche un avertissement si une clé override est inconnue (absente de base).
    """
    inconnues = [k for k in overrides.keys() if k not in base]
    if inconnues:
        print(f"⚠️ Clés inconnues ignorées: {inconnues}")
    # on fusionne en priorisant overrides
    merged = {**base, **{k: v for k, v in overrides.items() if k in base}}
    return merged

# Démo
print("additionner(1,2,3) =", additionner(1, 2, 3))
print("additionner()      =", additionner())

config_defaut = {"theme": "light", "debug": False}
print("fusion_config:", fusion_config(config_defaut, debug=True))
print("fusion_config avec clé inconnue:", fusion_config(config_defaut, debug=True, mode="pro"))
print("Vérif base inchangée:", config_defaut)
```

---

## <span style="color:red;">Correction — Exercice 2 : Valeurs par défaut & mutables</span> ⚠️

```python
# ❌ Mauvaise version : la liste par défaut est partagée entre appels
def ajouter_item_mauvais(x, liste=[]):
    liste.append(x)
    return liste

print("Mauvais 1:", ajouter_item_mauvais(1))
print("Mauvais 2:", ajouter_item_mauvais(2))
print("Mauvais 3:", ajouter_item_mauvais(3))  # Surprise : [1, 2, 3] cumulés

# ✅ Bonne version : utiliser None comme sentinelle
def ajouter_item(x, liste=None):
    if liste is None:
        liste = []
    liste.append(x)
    return liste

print("Bon 1:", ajouter_item(1))
print("Bon 2:", ajouter_item(2))
print("Bon 3:", ajouter_item(3))
```

---

## <span style="color:red;">Correction — Exercice 3 : Fonctions comme objets (premier ordre)</span> 🧠

```python
def carre(x: float) -> float:
    return x * x

def appliquer(f, valeur):
    """Applique f à valeur et retourne le résultat."""
    return f(valeur)

def compose(f, g):
    """Retourne h(x) = f(g(x))."""
    def h(x):
        return f(g(x))
    return h

def map_f(f, seq):
    """Retourne une nouvelle liste : f appliqué à chaque élément de seq."""
    return [f(x) for x in seq]

# Démo
print("appliquer(carre, 5)  =", appliquer(carre, 5))
print("compose(carre, abs)(-3) =", compose(carre, abs)(-3))
print("map_f(carre, [1,2,3])   =", map_f(carre, [1, 2, 3]))
```

---

## <span style="color:red;">Correction — Exercice 4 : Lambdas & Closures</span> 🧷

```python
# 1) Tri avec lambda
notes = [("Alice", 14), ("Bob", 9), ("Chloé", 16)]
notes_triees = sorted(notes, key=lambda t: t[1], reverse=True)
print("Tri par note décroissante:", notes_triees)

# 2) Closure
def make_multiplier(n: int):
    """Retourne une fonction f(x) = x * n."""
    def f(x: int) -> int:
        return x * n
    return f

times3 = make_multiplier(3)
print("times3(4) =", times3(4))

# 3) Piège du late binding + correction
# Mauvais : toutes les lambdas capturent la même variable i (sa valeur finale)
lambdas_mauvaises = [lambda: i for i in range(3)]
print("Late binding mauvais:", [f() for f in lambdas_mauvaises])  # [2,2,2]

# Bon : "geler" i via un paramètre par défaut
lambdas_bonnes = [lambda i=i: i for i in range(3)]
print("Late binding corrigé:", [f() for f in lambdas_bonnes])     # [0,1,2]
```

---

## <span style="color:red;">Correction — Exercice 5 : Générateurs & `yield`</span> ⚙️

```python
def pairs_jusqua(limit: int):
    """Génère 0, 2, 4, ..., ≤ limit."""
    n = 0
    while n <= limit:
        if n % 2 == 0:
            yield n
        n += 1

print("pairs_jusqua(6) →", list(pairs_jusqua(6)))

def lire_lignes_chemin(chemin: str):
    """
    Itère sur les lignes d'un fichier sans tout charger en mémoire.
    Usage: for ligne in lire_lignes_chemin('fichier.txt'): ...
    """
    with open(chemin, encoding="utf-8") as f:
        for ligne in f:
            yield ligne.rstrip("\n")

def chunker(iterable, taille: int):
    """
    Génère des blocs (listes) de longueur 'taille' à partir d'un iterable.
    Le dernier bloc peut être plus court.
    """
    bloc = []
    for item in iterable:
        bloc.append(item)
        if len(bloc) == taille:
            yield bloc
            bloc = []
    if bloc:
        yield bloc

# Démo chunker
print("chunker(range(7), 3) →", list(chunker(range(7), 3)))
```

---

## <span style="color:red;">Correction — Exercice 6 : Décorateurs</span> 🎀

```python
import time
from functools import wraps

def logger(f):
    """Décorateur : log avant/après l'appel (nom, args, kwargs, résultat)."""
    @wraps(f)
    def wrapper(*args, **kwargs):
        print(f"→ appel {f.__name__}(args={args}, kwargs={kwargs})")
        result = f(*args, **kwargs)
        print(f"← {f.__name__} → résultat: {result}")
        return result
    return wrapper

def timer(f):
    """Décorateur : mesure le temps d'exécution en millisecondes."""
    @wraps(f)
    def wrapper(*args, **kwargs):
        t0 = time.perf_counter()
        try:
            return f(*args, **kwargs)
        finally:
            dt_ms = (time.perf_counter() - t0) * 1000
            print(f"⏱️ {f.__name__}: {dt_ms:.2f} ms")
    return wrapper

@logger
@timer
def calcul_lent(n: int = 2_000_00):
    """Somme 1..n (simple calcul coûteux)."""
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

# Démo
_ = calcul_lent(200_000)
```

---

## <span style="color:red;">Correction — Exercice 7 : Récursivité</span> 🔁

```python
def factorielle(n: int) -> int:
    """Retourne n! récursivement. Lève ValueError si n < 0."""
    if n < 0:
        raise ValueError("n doit être ≥ 0")
    if n < 2:   # cas de base: 0! = 1, 1! = 1
        return 1
    return n * factorielle(n - 1)

def somme_naturels(n: int) -> int:
    """Retourne 1 + 2 + ... + n récursivement (n ≥ 0)."""
    if n < 0:
        raise ValueError("n doit être ≥ 0")
    if n == 0:
        return 0
    return n + somme_naturels(n - 1)

def taille(nested) -> int:
    """
    Compte le nombre total d'éléments non-listes dans une structure potentiellement imbriquée.
    Ex: [1,[2,3],[4,[5]]] → 5
    """
    if isinstance(nested, list):
        return sum(taille(x) for x in nested)
    return 1  # élément atomique

# Démo
print("factorielle(5)   =", factorielle(5))
print("somme_naturels(4)=", somme_naturels(4))
print("taille([1,[2,3],[4,[5]]]) =", taille([1, [2, 3], [4, [5]]]))
```

---

## <span style="color:red;">Correction — Exercice 8 : Docstrings & Annotations de type</span> 📚

```python
def normaliser_texte(texte: str, *, strip: bool = True, lower: bool = True) -> str:
    """
    Normalise un texte simple.

    Args:
        texte (str): texte d'entrée.
        strip (bool, kw-only): si True, supprime les espaces en début/fin.
        lower (bool, kw-only): si True, convertit en minuscules.
    Returns:
        str: texte normalisé.
    Exemple:
        >>> normaliser_texte("  Bonjour  ")
        'bonjour'
    """
    s = texte
    if strip:
        s = s.strip()
    if lower:
        s = s.lower()
    return s

# Tests
print(normaliser_texte("  Bonjour  "))
print(normaliser_texte("  Bonjour  ", strip=False, lower=True))
print(normaliser_texte("  Bonjour  ", strip=True, lower=False))

# Bonus : docstring pour un générateur et aperçu via help()
def pairs(limit: int):
    """Génère les entiers pairs de 0 à 'limit' inclus (step=2)."""
    for n in range(0, limit + 1, 2):
        yield n

# help(pairs)  # décommentez pour voir la doc dans un interpréteur
```

---

## <span style="color:lime;">Bonus — Intégration</span> 🧪

```python
# B1 — Cache facile
from functools import lru_cache

@lru_cache(maxsize=128)
def fib(n: int) -> int:
    """Fibonacci avec mémoïsation (cache)."""
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

print("fib(35) avec cache =", fib(35))

# B2 — Pipeline de fonctions
def strip_text(s: str) -> str: return s.strip()
def to_lower(s: str) -> str: return s.lower()
def remplacer_accents(s: str) -> str:
    import unicodedata
    return "".join(
        c for c in unicodedata.normalize("NFD", s)
        if unicodedata.category(c) != "Mn"
    )

def pipeline(texte: str, *fonctions):
    for f in fonctions:
        texte = f(texte)
    return texte

textes = ["  Héllo  ", "  ÇA VA?  "]
print([pipeline(t, strip_text, to_lower, remplacer_accents) for t in textes])

# B3 — Générateur + décorateur
def count_yield(gen_func):
    """Décorateur qui compte combien d'éléments un générateur a produits."""
    @wraps(gen_func)
    def wrapper(*args, **kwargs):
        count = 0
        for item in gen_func(*args, **kwargs):
            count += 1
            yield item
        print(f"ℹ️ {gen_func.__name__} a produit {count} élément(s).")
    return wrapper

@count_yield
def gen_range(n: int):
    for i in range(n):
        yield i

print(list(gen_range(5)))
```

---
