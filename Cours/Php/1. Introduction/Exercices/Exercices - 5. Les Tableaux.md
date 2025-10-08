# <span style="color:red;">Introduction aux Tableaux en PHP : Exercices</span> 📘

---

## <span style="color:red;">Exercice n°1 : QCM – Bases des tableaux</span> 🧩
**Objectif :** Valider les notions de base (déclaration, accès, fonctions simples).

1) Quelle syntaxe **déclare** correctement un tableau indexé ?  
   - A) `$t = (1,2,3);`  
   - B) `$t = array(1,2,3);`  
   - C) `$t = {1,2,3};`

2) Quelle est la **valeur affichée** ?  
```php
$couleurs = ["rouge", "vert", "bleu"];
echo $couleurs[1];
```
   - A) `rouge`  
   - B) `vert`  
   - C) `bleu`

3) Quelle fonction **compte** le nombre d’éléments ?  
   - A) `length()`  
   - B) `size()`  
   - C) `count()`

4) Quelle instruction **ajoute à la fin** du tableau `$nums` ?  
   - A) `array_push($nums, 10);`  
   - B) `array_unshift($nums, 10);`  
   - C) `$nums[0] = 10;`

🧠 **Tips pour apprenants :**  
- Déclaration : `array(...)` ou `[...]`.  
- Indexation des tableaux **indexés** : commence à `0`.  
- `count($t)` retourne la **taille**.

---

## <span style="color:red;">Exercice n°2 : Déclaration & Accès</span> ✍️
**Objectif :** Savoir créer des tableaux indexés et associatifs et accéder aux éléments.

1) Crée un tableau indexé `$prenoms` contenant `["Alice", "Bob", "Chloé"]`, puis affiche **le premier** et **le troisième** élément sur deux lignes.  
2) Crée un tableau associatif `$profil` avec les clés `nom`, `age`, `ville` (valeurs libres), puis affiche :  
`Nom : [nom] – Âge : [age] – Ville : [ville]`.

💡 **Tips pour apprenants :**  
- Indexé : `$t[0]`, `$t[2]`…  
- Associatif : `$t["cle"]`.

---

## <span style="color:red;">Exercice n°3 : Ajouter, supprimer, réindexer</span> ➕➖
**Objectif :** Maîtriser `[]`, `array_push`, `unset`, `array_pop`, `array_shift`, `array_values`.

1) À partir de `$fruits = ["Pomme", "Banane"];`  
   - Ajoute `"Cerise"` en **fin**.  
   - Ajoute `"Kiwi"` en **début**.  
   - Supprime **le premier** élément.  
2) Supprime **l’élément d’index 1** (s’il existe), puis **réindexe** le tableau pour qu’il reparte de `0`.

📌 **Zone de test :**
```php
$fruits = ["Pomme", "Banane"];
// Ton code ici
print_r($fruits);
```

🧠 **Tips pour apprenants :**  
- Fin : `$fruits[] = "..."` ou `array_push($fruits, "...")`.  
- Début : `array_unshift($fruits, "...")`.  
- Réindexer : `$fruits = array_values($fruits);`.

---

## <span style="color:red;">Exercice n°4 : Parcourir avec foreach (clés & valeurs)</span> 🔁
**Objectif :** Utiliser `foreach` pour lire un tableau indexé et associatif.

1) Avec `$notes = [12, 15, 9, 18];`, affiche :  
`Note #0 : 12`, `Note #1 : 15`, etc. (utilise l’**index** et la **valeur**).  
2) Avec `$user = ["nom" => "Luc", "age" => 28, "ville" => "Lyon"];`, affiche chaque **clé** et **valeur** au format :  
`nom => Luc`, `age => 28`, `ville => Lyon`.

📌 **Squelettes utiles :**
```php
// Indexé
foreach ($notes as $i => $val) {
    // ...
}

// Associatif
foreach ($user as $cle => $valeur) {
    // ...
}
```

🧠 **Tips pour apprenants :**  
- `foreach ($t as $val)` ou `foreach ($t as $cle => $val)` selon le besoin.  
- Très pratique pour éviter les erreurs d’index.

---

## <span style="color:red;">Exercice n°5 : Manipulations avancées (tri, fusion, recherche)</span> 🧪
**Objectif :** Enchaîner plusieurs fonctions courantes sur les tableaux.

1) **Tri décroissant** des scores (tout en **préservant les clés**) :  
```php
$scores = ["Alice" => 15, "Bob" => 12, "Chloé" => 18, "David" => 14];
// Trie pour obtenir Chloé, Alice, David, Bob
```

2) **Fusion** de deux tableaux indexés puis **suppression des doublons** :  
```php
$a = ["rouge", "vert", "bleu"];
$b = ["bleu", "jaune"];
// Fusionne $a et $b puis retire les doublons
```

3) **Recherche** : Vérifie si `"Paris"` est présent dans :  
```php
$villes = ["Lyon", "Paris", "Marseille"];
```
Affiche un message en conséquence.

🧠 **Tips pour apprenants :**  
- Tri décroissant **avec clés** : `arsort($t)`.  
- Fusion : `array_merge($a, $b)`.  
- Uniques : `array_unique($t)`.  
- Recherche : `in_array($val, $t)`.

---
