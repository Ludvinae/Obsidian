# <span style="color:red;">Katas JavaScript — Niveaux 1 à 4 + Mini-projets : Exercices</span> 📘

Chaque exercice inclut sa description, une **signature conseillée**, des **exemples**, un bloc **Exercice bonus**, et des **TIPS** pour vous guider. (Pas de solutions ici 😉)

---

# <span style="color:gold;">Niveau 1 — Mise en route</span> 🟢

## <span style="color:red;">Exercice 1 — Somme & Moyenne</span> ➗
**But :** `somme(arr)` et `moyenne(arr)`  
**Contraintes :** `arr` est un tableau de nombres (peut être vide).  
**Règle + :** renvoyer `null` si tableau vide.

**Signature conseillée :**
```js
function somme(arr) { /* ... */ }
function moyenne(arr) { /* ... */ }
```

**Exemples :**
- `[2,4,6] → somme=12, moyenne=4`
- `[] → somme=null, moyenne=null`

**Exercice bonus :**
- Gérer la présence de `NaN` (retourner `null` s’il y en a).
- Accepter aussi des nombres sous forme de chaînes `"3"` (les convertir).

**TIPS :**
- Vérifiez `arr.length === 0`.
- Évitez `reduce` sans valeur initiale si le tableau peut être vide.
- `Number.isNaN(x)` pour filtrer les valeurs invalides.

---

## <span style="color:red;">Exercice 2 — Min & Max (une passe)</span> ⤴️⤵️
**But :** `minMax(arr) → { min, max }`  
**Règle + :** `[] → null`  
**Contrainte :** **une seule passe** (un seul parcours).

**Signature conseillée :**
```js
function minMax(arr) { /* ... */ }
```

**Exemples :**
- `[5,1,9,7] → {min:1, max:9}`
- `[] → null`

**Exercice bonus :**
- Supporter des `-Infinity` / `Infinity`.
- Ignorer les `NaN`.

**TIPS :**
- Initialisez `min` et `max` avec le **premier élément** puis itérez.
- Comparez avec `if (x < min) ...` et `if (x > max) ...`.

---

## <span style="color:red;">Exercice 3 — Recherche linéaire</span> 🔎
**But :** `indexOf(arr, x) → index | -1` et `contient(arr, x) → boolean`.

**Signature conseillée :**
```js
function indexOfLinear(arr, x) { /* ... */ }
function contient(arr, x) { /* ... */ }
```

**Exemples :**
- `["a","b","c"], "b" → 1` ; `"z" → -1`
- `contient(["a","b","c"],"b") → true`

**Exercice bonus :**
- Accepter un **comparateur** optionnel `(a,b)=>boolean`.
- Ajouter un paramètre `fromIndex` de départ.

**TIPS :**
- Utilisez `===` pour l’égalité stricte par défaut.
- Retour **immédiat** dès qu’on trouve l’élément.

---

## <span style="color:red;">Exercice 4 — Dédoublonnage simple</span> 🧼
**But :** `dedupe([1,2,2,3,3,3]) → [1,2,3]`  
**Règle + :** version **sans `Set`** (boucle + `includes`).

**Signature conseillée :**
```js
function dedupe(arr) { /* Set */ }
function dedupeSansSet(arr) { /* boucle + includes */ }
```

**Exemples :**
- `[1,2,2,3,3,3] → [1,2,3]`
- `["a","a","b"] → ["a","b"]`

**Exercice bonus :**
- Garder **le premier** ou **le dernier** doublon selon un paramètre.

**TIPS :**
- `new Set(arr)` élimine les doublons en O(n).
- Version sans `Set` : créez un `out=[]`, et poussez si `!out.includes(x)`.

---

## <span style="color:red;">Exercice 5 — Compteur d’occurrences</span> 🔢
**But :** `frequences(["js","web","js"]) → { js:2, web:1 }`  
**Règle + :** version `Map`.

**Signature conseillée :**
```js
function frequencesObj(arr) { /* ... */ }  // retourne un Object
function frequencesMap(arr) { /* ... */ }  // retourne une Map
```

**Exemples :**
- `["js","web","js"] → { js:2, web:1 }`

**Exercice bonus :**
- Retourner aussi l’élément le plus fréquent.

**TIPS :**
- Incrémentez via `obj[k] = (obj[k] || 0) + 1`.
- Avec `Map`, utilisez `map.set(k, (map.get(k) || 0) + 1)`.

---

# <span style="color:gold;">Niveau 2 — Chaînes & Parcours</span> 🟡

## <span style="color:red;">Exercice 6 — Palindrome “propre”</span> 🔁
**But :** `estPalindrome(s)` en ignorant **espaces/majuscules**.  
**Règle + :** ignorer aussi **ponctuation**.

**Signature conseillée :**
```js
function estPalindrome(s) { /* ... */ }
```

**Exemples :**
- `"Esope reste ici et se repose" → true`
- `"kayak" → true`, `"bonjour" → false`

**Exercice bonus :**
- Version **deux pointeurs** sans recréer la chaîne nettoyée.

**TIPS :**
- Normalisez : `s.toLowerCase().replace(/[^a-z0-9]/gi, "")`.
- Comparez la chaîne à son renversé.

---

## <span style="color:red;">Exercice 7 — Mot le plus long</span> 🥇
**But :** `motPlusLong("le code en js") → "code"`  
**Contraintes :** mots séparés par espaces.  
**Règle + :** en cas d’égalité, renvoyer le **premier**.

**Signature conseillée :**
```js
function motPlusLong(phrase) { /* ... */ }
```

**Exemples :**
- `"le code en js" → "code"`

**Exercice bonus :**
- Normaliser multiples espaces et ponctuation simple.

**TIPS :**
- `phrase.trim().split(/\s+/)` pour découper proprement.

---

## <span style="color:red;">Exercice 8 — Anagrammes</span> 🔤
**But :** `sontAnagrammes(a, b) → bool`.  
**Règle + :** ignorer **espaces/accents/majuscules**.

**Signature conseillée :**
```js
function sontAnagrammes(a, b) { /* ... */ }
```

**Exemples :**
- `"listen","silent" → true` ; `"rat","car" → false`

**Exercice bonus :**
- Utiliser un **compteur** plutôt qu’un tri (meilleure complexité).

**TIPS :**
- Supprimez les accents :  
  `s.normalize('NFD').replace(/[\u0300-\u036f]/g, '')`.
- Comparez soit via tri des lettres, soit via fréquences.

---

## <span style="color:red;">Exercice 9 — Compression RLE</span> 📦
**But :** `compresser("aaabbc") → "a3b2c1"`  
**Règle + :** si la compression **n’écourte pas**, renvoyer l’original.

**Signature conseillée :**
```js
function compresser(s) { /* ... */ }
```

**Exemples :**
- `"aaabbc" → "a3b2c1"`
- `"abc" → "a1b1c1"` (→ renvoyer `"abc"` car pas plus court)

**Exercice bonus :**
- Gérer la **casse** (A ≠ a) selon un paramètre.

**TIPS :**
- Parcourez en comptant les répétitions consécutives.
- Concaténez `char + count`, comparez les longueurs.

---

## <span style="color:red;">Exercice 10 — Inverser les mots</span> 🔄
**But :** `inverseMots("hello world js") → "js world hello"`  
**Règle + :** normaliser les **espaces multiples**.

**Signature conseillée :**
```js
function inverseMots(s) { /* ... */ }
```

**Exemples :**
- `"  hello   world  js  " → "js world hello"`

**Exercice bonus :**
- Préserver la **ponctuation** accolée si besoin (option).

**TIPS :**
- `s.trim().split(/\s+/).reverse().join(" ")`.

---

# <span style="color:gold;">Niveau 3 — Tableaux & Logique</span> 🟠

## <span style="color:red;">Exercice 11 — Deuxième plus grand (sans trier)</span> 🥈
**But :** `secondMax([5,1,9,7,9,3]) → 7`  
**Règle + :** `null` si tous identiques ou longueur `< 2`.

**Signature conseillée :**
```js
function secondMax(arr) { /* ... */ }
```

**Exemples :**
- `[5,1,9,7,9,3] → 7` ; `[9,9] → null` ; `[] → null`

**Exercice bonus :**
- Gérer les **négatifs** et `-Infinity`.

**TIPS :**
- Maintenez `max1` et `max2` en une passe, **uniques**.

---

## <span style="color:red;">Exercice 12 — Pivot de somme</span> ⚖️
**But :** index `i` tel que somme gauche == somme droite.  
**Règle + :** premier pivot si plusieurs, sinon `-1`.

**Signature conseillée :**
```js
function pivotIndex(arr) { /* ... */ }
```

**Exemples :**
- `[1,7,3,6,5,6] → 3` (1+7+3 = 5+6)

**Exercice bonus :**
- Version qui retourne **tous** les pivots.

**TIPS :**
- Calculez `total`, puis balayez en gardant `leftSum`.

---

## <span style="color:red;">Exercice 13 — Somme de paires</span> 🤝
**But :** `aDeuxNombresQuiFont(arr, cible) → bool`  
**Règle + :** renvoyer **les indices** de la **première** paire trouvée.

**Signature conseillée :**
```js
function aDeuxNombresQuiFont(arr, cible) { /* ... */ }      // bool
function indicesPremierePaire(arr, cible) { /* ... */ }     // [i,j] ou null
```

**Exemples :**
- `[2,7,11,15], 9 → true` ; indices → `[0,1]`

**Exercice bonus :**
- Gérer les **doublons** (ex. cible=10 avec `[5,5]`).

**TIPS :**
- Map de `valeur → index`. Vérifiez `cible - val` pendant l’itération.

---

## <span style="color:red;">Exercice 14 — Fusion de deux triés (deux pointeurs)</span> 🧷
**But :** `fusionTries([1,4,7],[2,3,9]) → [1,2,3,4,7,9]`  
**Règle + :** **stabilité** : en cas d’égalité, prendre depuis `a` d’abord.

**Signature conseillée :**
```js
function fusionTries(a, b) { /* ... */ }
```

**Exemples :**
- `[1,4,7] + [2,3,9] → [1,2,3,4,7,9]`

**Exercice bonus :**
- Calculer aussi la **complexité** et justifier.

**TIPS :**
- Deux index `i,j`, comparez `a[i]` et `b[j]`, poussez le plus petit.

---

## <span style="color:red;">Exercice 15 — Fenêtre glissante : somme max (taille k)</span> 🪟
**But :** `sommeMax([1,2,3,4,5], 2) → 9` (4+5)  
**Règle + :** renvoyer l’intervalle `[start,end]`.

**Signature conseillée :**
```js
function sommeMax(arr, k) { /* ... */ }            // retourne la somme max
function sommeMaxInterval(arr, k) { /* ... */ }    // { somme, start, end }
```

**Exemples :**
- `[1,2,3,4,5], k=2 → somme=9, interval=[3,4]`

**Exercice bonus :**
- Gérer `k > arr.length` (retourner `null`).

**TIPS :**
- Faites une **somme initiale** des `k` premiers, puis **glissez**.

---

# <span style="color:gold;">Niveau 4 — Structures & Décisions</span> 🔴

## <span style="color:red;">Exercice 16 — Parenthèses bien formées</span> 🧮
**But :** `valide("(()())") → true`, `")(" → false`  
**Indice :** compteur `+1` sur `(`, `-1` sur `)`, jamais négatif, fini à 0.  
**Règle + :** supporter `[] {}` en plus (**pile**).

**Signature conseillée :**
```js
function valideParenthesesSimple(s) { /* ... */ }  // seulement ()
function valideParenthesesMulti(s) { /* ... */ }   // (), [], {}
```

**Exemples :**
- `"()()((()))" → true`, `"())(" → false`

**Exercice bonus :**
- Ignorer les caractères non-parenthèses.

**TIPS :**
- Multi-brackets : map `closing→opening`, utilisez une **stack**.

---

## <span style="color:red;">Exercice 17 — Regrouper par clé</span> 🧱
**But :** `groupBy(users, "ville")`  
**Règle + :** clé manquante → groupe `"inconnu"`.

**Signature conseillée :**
```js
function groupBy(arr, key) { /* ... */ }
```

**Exemple :**
```js
// [{nom:"A", ville:"Lyon"}, {nom:"B", ville:"Paris"}, {nom:"C", ville:"Lyon"}]
→ { Lyon:[{A},{C}], Paris:[{B}] }
```

**Exercice bonus :**
- Supporter une **fonction clé** `(item)=>string` au lieu d’un nom de propriété.

**TIPS :**
- `reduce` est votre ami pour construire un objet de groupes.

---

## <span style="color:red;">Exercice 18 — Tri par comptage (Count sort “lite”)</span> 📊
**But :** trier un **tableau d’entiers petits et non négatifs** sans `sort()`.  
**Règle + :** renvoyer aussi la **table de fréquences**.

**Signature conseillée :**
```js
function countSortLite(arr) { /* ... */ } // retourne { sorted, freq }
```

**Exemples :**
- `[1,4,1,2,7,5,2] → [1,1,2,2,4,5,7]`

**Exercice bonus :**
- Gérer un **max** dynamique et vérifier valeurs négatives (erreur).

**TIPS :**
- Construisez `freq` de taille `max+1`, puis reconstruisez le tableau.

---

## <span style="color:red;">Exercice 19 — Racine digitale (digital root)</span> 🔂
**But :** `racineDigitale(942) → 6` (9+4+2=15, 1+5=6)  
**Règle + :** version **boucle** (sans récursion).

**Signature conseillée :**
```js
function racineDigitale(n) { /* ... */ }
```

**Exemples :**
- `38 → 2` (3+8=11, 1+1=2)

**Exercice bonus :**
- Variante **arithmétique** : `n === 0 ? 0 : 1 + (n - 1) % 9` (documenter limites).

**TIPS :**
- Additionnez les chiffres tant que la somme ≥ 10.

---

## <span style="color:red;">Exercice 20 — Zigzag (up/down)</span> 📈📉
**But :** vérifier si l’array **alterne** `>` / `<` **strictement**.  
**Règle + :** renvoyer **l’index où ça casse** si `false`.

**Signature conseillée :**
```js
function estZigzag(arr) { /* ... */ }            // boolean
function estZigzagAvecRupture(arr) { /* ... */ } // { ok, ruptureIndex: number|null }
```

**Exemples :**
- `[1,3,2,4,3] → true` ; `[1,1,2] → false (rupture à 1)`

**Exercice bonus :**
- Tolérer des **égaux** via un paramètre (par défaut strict).

**TIPS :**
- Déterminez le **sens** initial, puis alternez à chaque pas.

---

# <span style="color:gold;">Mini-projets (bonus fun)</span> ⭐

## <span style="color:red;">Exercice 21 — Bulls & Cows (juste prix de chiffres)</span> 🐂🐄
**But :** comparer `secret` vs `guess`.  
**Sortie :** format `"xAyB"` (x bulls, y cows).  
- **Bull** : chiffre correct à la **bonne position**  
- **Cow** : chiffre présent mais à la **mauvaise position**

**Signature conseillée :**
```js
function bullsAndCows(secret, guess) { /* ... */ } // "1A3B"
```

**Exemples :**
- `secret="1807", guess="7810" → "1A3B"`

**Exercice bonus :**
- Supporter des **caractères non numériques** (lettres autorisées).

**TIPS :**
- 1ère passe : compter les **bulls**.  
- 2ème passe : comptez fréquences pour calculer les **cows** sans double-compte.

---

## <span style="color:red;">Exercice 22 — Horloge en mots</span> ⏰
**But :** `enMots(h, m)`  
**Exemples :**  
- `13,5 → "une heure cinq"`  
- `0,0 → "minuit"`  
**Plus :** gérer singulier/pluriel, `et quart`, `et demie`, `moins le quart`.

**Signature conseillée :**
```js
function enMots(h, m) { /* ... */ }
```

**Exercice bonus :**
- Supporter `m=45` → `"moins le quart"`, `m=30` → `"et demie"`.

**TIPS :**
- Dictionnaire nombres→mots (0..59).  
- Traitez cas spéciaux **avant** le cas général.

---

## <span style="color:red;">Exercice 23 — Romain ↔ Décimal (borné)</span> 🏛️
**Bornes :** `1..3999`, validation simple.

**Signatures conseillées :**
```js
function romainVersInt(s) { /* ... */ }
function intVersRomain(n) { /* ... */ }
```

**Exemples :**
- `"XIV" → 14` ; `58 → "LVIII"`

**Exercice bonus :**
- Rejeter les formes invalides (`IL`, `VX`, etc.).

**TIPS :**
- Paires soustractives : `IV, IX, XL, XC, CD, CM`.  
- Construction **gloutonne** du plus grand symbole possible.

---

## <span style="color:red;">Exercice 24 — Tableaux 2D : îles de 1</span> 🏝️
**But :** compter les “îles” de `1`.  
**Version simple :** compter seulement les **blocs horizontaux/verticaux** (pas de diagonale).  
**Plus :** vraie **DFS/BFS** (haut/bas/gauche/droite).

**Signatures conseillées :**
```js
function compterIlesSimple(grid) { /* ... */ }
function compterIlesDFS(grid) { /* ... */ }
```

**Exercice bonus :**
- Marquer les **visités** sans modifier la grille (Set de clés `"r,c"`).

**TIPS :**
- Parcours cellule par cellule, lancez une **exploration** quand vous voyez un `1`.

---

## <span style="color:red;">Exercice 25 — Validateur de mot de passe</span> 🔐
**But :** renvoyer **raisons d’échec** : longueur, maj, min, chiffre, spécial.  
**Plus :** retourner un **score sur 5**.

**Signature conseillée :**
```js
function validerMotDePasse(pwd) {
  // retourne { ok:boolean, raisons:string[], score:number }
}
```

**Exemples de règles :**
- Longueur `>= 8`
- Au moins une **majuscule** `[A-Z]`
- Au moins une **minuscule** `[a-z]`
- Au moins un **chiffre** `[0-9]`
- Au moins un **spécial** `[^A-Za-z0-9]`

**Exercice bonus :**
- Ajouter une règle d’**entropie** (ex. pénaliser répétitions `"aaaa"`).

**TIPS :**
- Compilez vos **regex** et testez chacune, cumulez les raisons.

---

# <span style="color:gold;">Annexe — Blocs de départ (copier/coller)</span> 🧩

```js
// N1
function somme(arr) {}
function moyenne(arr) {}
function minMax(arr) {}
function indexOfLinear(arr, x) {}
function contient(arr, x) {}
function dedupe(arr) {}
function dedupeSansSet(arr) {}
function frequencesObj(arr) {}
function frequencesMap(arr) {}

// N2
function estPalindrome(s) {}
function motPlusLong(phrase) {}
function sontAnagrammes(a, b) {}
function compresser(s) {}
function inverseMots(s) {}

// N3
function secondMax(arr) {}
function pivotIndex(arr) {}
function aDeuxNombresQuiFont(arr, cible) {}
function indicesPremierePaire(arr, cible) {}
function fusionTries(a, b) {}
function sommeMax(arr, k) {}
function sommeMaxInterval(arr, k) {}

// N4
function valideParenthesesSimple(s) {}
function valideParenthesesMulti(s) {}
function groupBy(arr, key) {}
function countSortLite(arr) {}
function racineDigitale(n) {}
function estZigzag(arr) {}
function estZigzagAvecRupture(arr) {}

// Mini-projets
function bullsAndCows(secret, guess) {}
function enMots(h, m) {}
function romainVersInt(s) {}
function intVersRomain(n) {}
function compterIlesSimple(grid) {}
function compterIlesDFS(grid) {}
function validerMotDePasse(pwd) {}
```

---
