# <span style="color:red;">Collections Python : Exercices </span> 📘

---

## <span style="color:red;">Exercice n°1 — Choisir la bonne collection</span> 🧭
**But :** identifier la structure la plus adaptée (**list/tuple/set/dict**).

1. Pour enregistrer l’**ordre** des étapes d’un tutoriel que vous modifiez souvent.  
2. Pour représenter une **coordonnée** `(x, y)` qui ne doit pas changer.  
3. Pour stocker la **liste des e-mails uniques** inscrits à une newsletter (doublons possibles à l’entrée).  
4. Pour associer des **codes produits** à leurs **prix**.  
5. Pour conserver un **historique** d’actions (ordre et doublons importants).  
6. Pour manipuler un **jeu de tags** (ordre indifférent, pas de doublon).

### 💡 Tips
- **Ordre + modif + index** → `list`  
- **Paquet figé** → `tuple`  
- **Unicité / appartenance** → `set`  
- **Association clé→valeur** → `dict`

---

## <span style="color:red;">Exercice n°2 — Tuples (immutabilité & dépack)</span> 📦
**But :** manipuler des **tuples** et comprendre leur **immutabilité**.

1. Créez `point = (12.5, -3.0)` puis affectez `x, y = point`.  
2. Essayez conceptuellement de modifier `point[0]` (expliquez ce qui se passerait).  
3. Créez un **tuple à 1 élément** contenant `"unique"` (syntaxe correcte attendue).  
4. Créez `couleur = ("rouge", "vert", "bleu")`, effectuez un **dépack** en `r, v, b`.  
5. Expliquez quand un **tuple** peut être utilisé comme **clé** de dictionnaire.

### 💡 Tips
- Tuple **immutables** → pas d’assignation d’index.  
- Tuple à 1 élément : **virgule obligatoire** (ex. `("a",)`).  
- Clé hachable : le **tuple** et ses **éléments** doivent l’être.

---

## <span style="color:red;">Exercice n°3 — Ensembles (unicité & opérations)</span> 🛑
**But :** dédupliquer, tester l’appartenance, pratiquer **union / intersection / différence**.

1. À partir de `emails = ["a@x", "b@y", "a@x", "c@z", "b@y"]`, obtenez l’ensemble des **e-mails uniques**.  
2. Donnez la **taille** de cet ensemble.  
3. Soit `A = {"python", "java", "go"}` et `B = {"go", "rust", "python"}` : calculez **A ∪ B**, **A ∩ B**, **A \ B**, **A Δ B**.  
4. Testez l’**appartenance** de `"rust"` à `A`.

### 💡 Tips
- `{}` → **dict vide** ; ensemble vide → `set()`.  
- `|` union, `&` intersection, `-` différence, `^` diff. symétrique.  
- Les éléments d’un `set` doivent être **hachables**.

---

## <span style="color:red;">Exercice n°4 — Dictionnaires (CRUD & parcours)</span> 📚
**But :** créer, lire, mettre à jour et supprimer dans un **dict** ; parcourir clés/valeurs.

1. Créez `produit = {"ref": "A42", "nom": "Clavier", "prix": 39.9}`.  
2. **Ajoutez** une clé `"stock": 120`.  
3. **Modifiez** `"prix"` à `34.9`.  
4. Récupérez la valeur `"couleur"` en renvoyant `"inconnue"` si absente (**sans** lever d’erreur).  
5. **Supprimez** la clé `"stock"` proprement.  
6. Parcourez `produit` pour afficher `clé → valeur` sur chaque ligne.

### 💡 Tips
- Accès sûr : `d.get("clé", valeur_par_défaut)`  
- Suppression : `pop("clé")` ou `del d["clé"]`.  
- Parcours : `for k, v in d.items(): ...`

---

## <span style="color:red;">Exercice n°5 — Compréhensions (list/set/dict)</span> ⚡
**But :** transformer et filtrer rapidement avec des compréhensions.

1. À partir de `nums = [1, 2, 3, 4, 5, 6]`, créez :  
   - `carres` : la **liste** des carrés.  
   - `pairs` : l’**ensemble** des nombres pairs.  
   - `parite` : le **dictionnaire** `{n: "pair"|"impair"}`.  
2. À partir de `mots = ["Zèbre", "avion", "Banane", "avion"]`, créez un **set** des mots **normalisés** (minuscule).  
3. À partir de `notes = {"Alice": 15, "Bob": 9, "Chloé": 18}` créez `mentions` : `{nom: "OK" si note≥10 sinon "KO"}`.

### 💡 Tips
- `[...]` list, `{... for ...}` set, `{k: v for ...}` dict.  
- Un **set** supprime les **doublons** automatiquement.

---

## <span style="color:red;">Exercice n°6 — Conversions entre collections</span> 🔁
**But :** passer d’un type de collection à un autre selon le besoin.

1. Transformez `liste_tuples = [("FR", "Paris"), ("ES", "Madrid"), ("IT", "Rome")]` en **dictionnaire** `{"FR":"Paris", ...}`.  
2. À partir de `d = {"a": 1, "b": 2, "c": 3}`, créez :  
   - la **liste des clés**, la **liste des valeurs**, la **liste des (clé, valeur)**.  
3. À partir du **texte** `"Python est cool et Python est lisible"`, construisez l’**ensemble** des **mots uniques** (minuscule, séparés par espace).  
4. Créez un **dict de fréquences** `{mot: nb_occurrences}` pour ce texte.

### 💡 Tips
- `dict(liste_de_paires)` → dict.  
- `d.keys()/d.values()/d.items()` → vues convertibles en liste.  
- Normalisez (minuscule) **avant** de compter.

---

## <span style="color:red;">Exercice n°7 — Étude de cas : mini “catalogue”</span> 🛒
**But :** choisir/combiner les bonnes collections.

1. Représentez un **catalogue** de produits où chaque **référence** (clé) pointe vers un **dict** de propriétés (`nom`, `prix`, `stock`).  
2. Ajoutez **3 produits** puis :  
   - **mettez à jour** le stock d’une référence ;  
   - **appliquez** une réduction de 10% sur **tous** les prix via un **parcours** ;  
   - **listez** les références **épuisées** (stock = 0) dans une **liste**.  
3. Construisez l’**ensemble** des **noms** de produits (unicité).

### 💡 Tips
- Catalogue : `dict` de `dict`.  
- Parcours : `for ref, infos in catalog.items(): ...`  
- Unicité des noms : `set(...)`.

---

## <span style="color:red;">Exercice n°8 — Copies, alias & mutabilité</span> 🧯
**But :** éviter les **alias** involontaires et comprendre **shallow vs deep copy**.

1. Créez `L = [[1, 2], [3, 4]]`.  
2. Faites `A = L` (alias) puis modifiez `A[0][0]`. Observez l’effet attendu sur `L`.  
3. Créez une **copie superficielle** `B` qui **duplique les sous-listes** (pas un simple alias). Modifiez `B[0][0]` et vérifiez l’impact sur `L`.  
4. Expliquez quand une **copie profonde** serait nécessaire.

### 💡 Tips
- Alias : `B = A` (même objet).  
- Copie superficielle 2D : `[row[:] for row in L]`.  
- Copie **profonde** : `copy.deepcopy(obj)` (structures imbriquées complexes).

---

## <span style="color:lime;">Exercice BONUS — Index inversé de mots</span> 🔍
**But :** combiner **set**, **dict** et compréhensions pour créer un **index inversé**.

1. Soient trois **phrases** (chaînes). Normalisez : **minuscule**, remplacez `,.;:!?` par espace, et **split**.  
2. Construisez `index = {mot: set({indices_de_phrases_où_il_apparaît})}`.  
   - Ex. si `"python"` apparaît dans la phrase 0 et 2 → `index["python"] == {0, 2}`  
3. Affichez, trié par mot, la **liste des phrases** où chaque mot apparaît.

### 💡 Tips
- Dédoublonnez par phrase avec `set(mots_de_la_phrase)`.  
- Mettez à jour `index` : si mot absent → créer une **nouvelle entrée**.  
- `dict` des **sets** : pratique pour l’indexation.

---

### ✅ Recommandations générales
- **D’abord le besoin**, **ensuite** la collection : ordre ? unicité ? clés nommées ? immutabilité ?  
- Évitez les **modifs en place** non nécessaires : préférez créer de **nouvelles** collections lors de transformations.  
- Attention à la **mutabilité** (alias) et aux **copies**.  
- Les **compréhensions** sont top pour des opérations simples ; au-delà, préférez des **boucles** lisibles.
