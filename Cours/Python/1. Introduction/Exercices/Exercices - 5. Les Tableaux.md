# <span style="color:red;">Les Tableaux (Listes) en Python : Exercices</span> 📘

---

## <span style="color:red;">Exercice n°1 — Accès & Slicing</span> ✂️
**But :** manipuler les indices (positifs/négatifs) et les tranches.

1. Créez la liste `nombres = [10, 20, 30, 40, 50, 60, 70]`.
2. Récupérez :
   - le **premier** élément, le **dernier** (indice négatif) et l’élément du **milieu**.
   - la sous-liste des éléments d’**indice 2 à 4** (fin **exclue**).
   - la sous-liste des **3 premiers** éléments, puis des **3 derniers**.
   - la liste des éléments **un sur deux** (pas = 2).
   - la liste **inversée** (sans utiliser `reverse()`).
3. Affichez chaque résultat avec un libellé clair.

**Tips :**
- `L[a:b]` **exclut** `b`.  
- `L[::-1]` renvoie une **copie inversée**.

---

## <span style="color:red;">Exercice n°2 — Ajouts & Suppressions</span> ➕➖
**But :** utiliser `append`, `insert`, `extend`, `pop`, `remove`, `del`, `clear`.

1. Partez de `L = [10, 20, 30]`.
2. Ajoutez `40` en fin, puis insérez `15` à l’indice `1`.
3. Étendez `L` avec `[41, 42]` en une seule instruction.
4. Supprimez la **première occurrence** de `15`.
5. Retirez et **récupérez** le dernier élément (puis affichez-le).
6. Supprimez l’élément d’indice `1` **sans** le récupérer.
7. Videz la liste.
8. À chaque étape, affichez `L`.

**Tips :**
- `remove(val)` lève `ValueError` si `val` n’existe pas → vérifiez avec `if val in L:`  
- `pop()` **retourne** l’élément supprimé.

---

## <span style="color:red;">Exercice n°3 — Recherche, Comptage & Tri</span> 🔎🗂️
**But :** pratiquer `in`, `count`, `index`, `sort`, `sorted`, `reverse`.

1. Créez `couleurs = ["rouge", "vert", "bleu", "Bleu", "jaune", "bleu"]`.
2. Vérifiez si `"vert"` est présent. Comptez le nombre d’occurrences de `"bleu"`.
3. Trouvez l’**indice** de la **première** occurrence de `"bleu"`, puis celui de la **suivante** (en démarrant après l’indice trouvé).
4. Triez **en place** `couleurs` en tenant **compte de la casse**, puis affichez.
5. Créez ensuite **une nouvelle** liste triée **sans** tenir compte de la casse (la liste d’origine ne doit pas être modifiée cette fois).
6. Inversez l’ordre actuel (en place) et affichez.

**Tips :**
- `list.sort()` modifie la liste et **retourne `None`**.  
- `sorted(itérable, key=str.lower)` renvoie une **nouvelle liste**.

---

## <span style="color:red;">Exercice n°4 — Listes 2D (création sûre & accès)</span> 🧭
**But :** créer correctement des tableaux 2D et les parcourir.

1. **Ne faites pas** `grille = [[0]*3]*4` (piège).  
   Créez une **grille 4×3** de zéros avec une **compréhension** (lignes indépendantes).
2. Remplacez la valeur en **ligne 0, colonne 0** par `1` puis affichez la grille.
3. Calculez la **somme de chaque ligne** et affichez une ligne par somme.
4. Extrait la **première colonne** dans une liste `col0`.
5. Créez une **copie** de la grille qui ne réutilise pas les mêmes sous-listes (copie **ligne par ligne**).

**Tips :**
- `[[0]*3 for _ in range(4)]` crée **4 sous-listes distinctes**.  
- Copie 2D simple : `[ligne[:] for ligne in grille]`.

---

## <span style="color:red;">Exercice n°5 — Compréhensions & Agrégats</span> ⚡🧮
**But :** transformer/filtrer rapidement et calculer des agrégats.

1. À partir de `vals = [3, -1, 5, -7, 2, 0, 9]` :
   - créez `positives` ne contenant que les valeurs **≥ 0** ;
   - créez `carres` contenant le carré de chaque valeur ;
   - créez `as_str` qui convertit chaque **valeur** en chaîne de caractères ;
2. À partir de `mat = [[1, 2], [3, 4], [5]]`, créez `plat = [1, 2, 3, 4, 5]` via une **compréhension imbriquée**.
3. Calculez `len(plat)`, `sum(plat)`, `min(plat)`, `max(plat)`, et :
   - `all(v > 0 for v in plat)`
   - `any(v % 2 == 0 for v in plat)`

**Tips :**
- `[f(x) for x in seq if cond(x)]` : transformation + filtre.  
- Aplatissement : `[x for ligne in mat for x in ligne]`.

---

## <span style="color:red;">Exercice BONUS — Mini “Pacman” en console (avec listes)</span> 👾🎮
**But :** réaliser un petit jeu textuel en console, en représentant la carte avec des **listes de listes**.

### Règles & Contraintes
1. **Carte** : une grille 2D (liste de listes de caractères) avec :
   - `'#'` = mur, `'.'` = pac-gomme, `' '` = vide, `'P'` = Pacman, `'G'` = fantôme.
2. **Affichage** (console) :
   - Affichez la grille à chaque tour (effacez l’écran avant : `cls` sur Windows, `clear` sur macOS/Linux).
3. **Contrôles** :
   - Lire un caractère `z`/`q`/`s`/`d` (ou flèches si vous gérez) pour déplacer `P` (haut/gauche/bas/droite).  
   - Ne pas traverser les `'#'`.
4. **Score & fin** :
   - Ramasser une `'.'` augmente le **score** ; la case devient `' '` (mangée).  
   - **Victoire** quand il n’y a plus de `'.'`.  
   - **Défaite** si `P` entre en collision avec `G`.
5. **Fantôme** :
   - Au minimum, déplacez `G` **aléatoirement** d’une case par tour (sans traverser les murs).  
   - (Option ++) Faites-le **poursuivre** approximativement `P`.
6. **Boucle de jeu** :
   - Répéter : afficher → lire entrée → déplacer `P` → déplacer `G` → tester **victoire/défaite**.
7. **Techniques autorisées** :
   - **Listes** et **listes de listes** pour la carte et les positions ; modules standards (`random`, `time`, `os`, `sys`) si besoin.  
   - Pas de bibliothèques externes.

### Étapes suggérées
- [ ] Représenter la carte en **liste de listes** (chaque ligne = liste de caractères).  
- [ ] Trouver les positions initiales de `P` et `G`.  
- [ ] Écrire une fonction `afficher(grille)` qui imprime la carte.  
- [ ] Écrire `deplacer(grille, pos, direction)` qui renvoie la **nouvelle position** (sans passer les murs).  
- [ ] Boucle : lire une touche → déplacer `P` → manger la pac-gomme si `'.'`.  
- [ ] Déplacer `G` (aléatoire au début).  
- [ ] Tester conditions de fin (plus de `'.'` ou collision).

**Tips :**
- Pour effacer l’écran :  
  ```python
  import os
  os.system("cls" if os.name == "nt" else "clear")
  ```
- Pour compter les pac-gommes restantes : **parcourir** la grille et compter les `'.'`.  
- Gardez la carte **immuable** pour les murs ; ne modifiez que les cases parcourues (`'.'` → `' '`).  
- Utilisez des **tuples** `(ligne, colonne)` pour manipuler les positions, et une **liste** de déplacements possibles pour `G`.

---

### ✅ Recommandations générales
- Affichez des **messages clairs** à chaque étape (avant/après, indices, etc.).  
- Testez aussi des **cas limites** (listes vides, indices hors bornes, grilles 1×N, etc.).  
- Privilégiez des fonctions **courtes** (affichage, déplacement, comptages…) pour mieux tester.
