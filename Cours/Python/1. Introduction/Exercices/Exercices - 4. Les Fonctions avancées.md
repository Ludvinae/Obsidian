# <span style="color:red;">Les Fonctions Avancées : Exercices (avec Tips)</span> 📘

---

## <span style="color:red;">Exercice 1 — `*args` et `**kwargs`</span> 🧺
**But :** accepter un nombre variable d’arguments et d’options nommées.

**Consignes :**
1. Écrivez `additionner(*nombres)` qui retourne la **somme** de tous les nombres passés (0 si rien).
2. Créez `fusion_config(base: dict, **overrides)` qui retourne un **nouveau dict** fusionnant `base` et les options fournies (sans modifier `base`).
3. Variante : si un `override` contient une **clé inconnue** (non présente dans `base`), affichez un **avertissement**.

**Exemples d’I/O attendus :**
- `additionner(1,2,3)` → `6` ; `additionner()` → `0`  
- `fusion_config({"theme":"light","debug":False}, debug=True)` → `{"theme":"light","debug":True}`

### 💡 Tips
- `*args` arrive sous forme de **tuple**, `**kwargs` sous forme de **dict**.  
- Signature conseillée : `def f(obligatoire, *args, option=None, **kwargs): ...`  
- **Ne modifiez pas** `base` : copiez-la (`copy()` ou `{**base, **overrides}`).

---

## <span style="color:red;">Exercice 2 — Valeurs par défaut & mutables</span> ⚠️
**But :** comprendre le **piège des mutables** comme valeurs par défaut.

**Consignes :**
1. Écrivez `ajouter_item_mauvais(x, liste=[])` et **appelez-la 3 fois** ; observez la surprise.
2. Expliquez (en 1–2 phrases) pourquoi le contenu s’**accumule**.
3. Réécrivez en version sûre : `ajouter_item(x, liste=None)` qui crée une **nouvelle liste** si besoin.

**Exemples d’I/O attendus :**
- Appels successifs → la version “mauvaise” réutilise la **même liste** entre appels.

### 💡 Tips
- Les valeurs par défaut sont **évaluées une seule fois** (à la **définition**).  
- Utilisez `None` comme **sentinelle**, puis créez la structure **dans** la fonction.  
- `id(obj)` peut vous montrer si c’est le **même objet** entre appels.

---

## <span style="color:red;">Exercice 3 — Fonctions comme objets (premier ordre)</span> 🧠
**But :** passer une fonction en paramètre et retourner une fonction.

**Consignes :**
1. Écrivez `appliquer(f, valeur)` qui **applique** la fonction `f` à `valeur`. Testez avec une fonction `carre`.
2. Créez `compose(f, g)` qui retourne une **nouvelle fonction** `h(x) = f(g(x))`. Testez.
3. Variante : `map_f(f, seq)` qui **retourne** une nouvelle liste en appliquant `f` à chaque élément.

**Exemples d’I/O attendus :**
- `appliquer(carre, 5)` → `25`  
- `compose(carre, abs)(-3)` → `9`

### 💡 Tips
- Une fonction est une **valeur** : on peut la stocker, la passer, la retourner.  
- Pour `compose`, attention à bien **retourner** la fonction interne (et pas son résultat).

---

## <span style="color:red;">Exercice 4 — Lambdas & Closures</span> 🧷
**But :** créer de petites fonctions anonymes et capturer un environnement.

**Consignes :**
1. Triez `notes = [("Alice",14),("Bob",9),("Chloé",16)]` **par la note** décroissante avec une **lambda**.
2. Écrivez `make_multiplier(n)` qui **retourne** une fonction `f(x)` calculant `x * n` (closure). Testez `times3 = make_multiplier(3)`.
3. Bonus (piège du “late binding”) : créez une liste de fonctions `[lambda: i for i in range(3)]` et observez le **résultat** quand vous les appelez. Corrigez en “gelant” `i` via un **paramètre par défaut**.

**Exemples d’I/O attendus :**
- `times3(4)` → `12`  
- Liste de lambdas non corrigée → toutes renvoient la **même valeur**.

### 💡 Tips
- Lambda = **une expression**, pas d’instructions multiples.  
- Closure : la fonction **retient** la variable de l’environnement.  
- Pour éviter le “late binding” : `lambda i=i: i`.

---

## <span style="color:red;">Exercice 5 — Générateurs & `yield`</span> ⚙️
**But :** produire paresseusement des valeurs, économiser la mémoire.

**Consignes :**
1. Écrivez `pairs_jusqua(limit)` qui **génère** `0,2,4,... ≤ limit`.  
2. Créez `lire_lignes_chemin(chemin)` qui **itère** sur les lignes d’un fichier **sans** tout charger (utilisez `yield`).
3. Bonus : `chunker(iterable, taille)` qui **rend** des blocs successifs de longueur `taille` (dernier bloc possiblement plus court).

**Exemples d’I/O attendus :**
- `list(pairs_jusqua(6))` → `[0, 2, 4, 6]`

### 💡 Tips
- `yield` **met en pause** la fonction et **reprend** au même endroit à l’appel suivant.  
- Un générateur est **consommable** : après l’avoir parcouru, il est **vide**.  
- Idéal pour **gros fichiers** / flux continus.

---

## <span style="color:red;">Exercice 6 — Décorateurs</span> 🎀
**But :** ajouter un comportement autour d’une fonction **sans** la modifier.

**Consignes :**
1. Écrivez un décorateur `logger(f)` qui affiche **avant/après** l’appel : nom de fonction + arguments + résultat.
2. Écrivez `timer(f)` qui affiche le **temps d’exécution** en ms.
3. Appliquez-les à une fonction `calcul_lent()` (ex. somme d’une grande plage).  
4. Bonus : utilisez `functools.wraps` pour **préserver** `__name__` et la docstring.

**Exemples d’I/O attendus :**
- Affichages du type : `→ appel calcul_lent(args=..., kwargs=...)` puis `← résultat ... (12.34 ms)`

### 💡 Tips
- Un décorateur prend une fonction et **retourne** une fonction.  
- La fonction interne doit accepter `*args, **kwargs`.  
- `@decorateur` équivaut à `fonction = decorateur(fonction)`.

---

## <span style="color:red;">Exercice 7 — Récursivité (cas de base & réduction)</span> 🔁
**But :** poser un **cas d’arrêt** clair et réduire le problème à chaque appel.

**Consignes :**
1. Implémentez `factorielle(n)` récursif (avec garde pour `n < 0`).  
2. Écrivez `somme_naturels(n)` qui retourne `1 + 2 + ... + n` récursivement.  
3. Bonus : `taille(nested)` qui calcule le **nombre total d’éléments** dans une **liste potentiellement imbriquée** (ex. `[1,[2,3],[4,[5]]]` → `5`).

**Exemples d’I/O attendus :**
- `factorielle(5)` → `120`  
- `somme_naturels(4)` → `10`

### 💡 Tips
- Toujours deux parties : **cas de base** + **cas récursif** (réduire `n`).  
- Vérifiez les **entrées invalides** (`n` négatif).  
- Beaucoup de récursions se convertissent en **boucles** (souvent plus simples).

---

## <span style="color:red;">Exercice 8 — Docstrings & Annotations de type</span> 📚
**But :** documenter clairement et typer pour la lisibilité/outillage.

**Consignes :**
1. Écrivez `normaliser_texte(texte: str, *, strip: bool = True, lower: bool = True) -> str` avec docstring (but, params, retour, exemple).  
2. Ajoutez **au moins 2 tests** d’appel montrant l’effet des options.  
3. Bonus : écrivez une petite **docstring** pour un générateur (`yield`) et vérifiez l’aperçu avec `help(votre_fonction)`.

**Exemples d’I/O attendus :**
- `normaliser_texte("  Bonjour  ")` → `"bonjour"` (si `strip=True` et `lower=True`).

### 💡 Tips
- Docstring = **but** + **paramètres** + **retour** + (éventuellement) **exemple**.  
- Les annotations sont **indicatives** : utiles pour IDE/linters/tests.  
- Gardez la signature **lisible** (keyword-only `*` pour options claires).

---

## <span style="color:lime;">Bonus (intégration)</span> 🧪
- **B1 — Cache facile :** utilisez `functools.lru_cache(maxsize=128)` pour **mémoriser** les résultats d’une fonction coûteuse (ex. `fib(n)`).  
- **B2 — Pipeline :** construisez un **pipeline** de fonctions (`strip` → `lower` → `remplacer_accents`) et appliquez-le à une liste de textes.  
- **B3 — Générateur + décorateur :** décorez un **générateur** pour compter combien d’éléments il a produits (affichage à la fin).

---

## 🎓 Conseils généraux
- **Commencez simple**, validez, puis améliorez (ajoutez options & contrôles).  
- **Nom clair**, **responsabilité unique**, **docstring courte**.  
- Préférez **retourner** des valeurs et gérer l’I/O **en dehors** des fonctions.  
- Testez les **cas limites** (vide, zéro, gros volumes, types inattendus).  
- Pour apprendre : **imprimez** des checkpoints dans décorateurs/générateurs pour **voir** le flux d’exécution.
