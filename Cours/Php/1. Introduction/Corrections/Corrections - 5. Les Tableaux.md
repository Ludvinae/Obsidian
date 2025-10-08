# <span style="color:red;">Introduction aux Tableaux en PHP : Correction Exercices</span> 📘

---

## <span style="color:red;">Exercice n°1 : Correction (QCM – Bases des tableaux)</span> ✅

1) **B** — `$t = array(1,2,3);`  
*`array(...)` ou `[...]` créent un tableau. `(1,2,3)` n’est pas valide en PHP.*

2) **B** — `vert`  
*Les index commencent à 0, donc `1` pointe sur le deuxième élément.*

3) **C** — `count()`  
*`length()` et `size()` n’existent pas en PHP pour les tableaux.*

4) **A** — `array_push($nums, 10);`  
*`array_unshift` ajoute au **début**. `$nums[0] = 10` écrase l’index 0, n’ajoute pas forcément en fin.*

---

## <span style="color:red;">Exercice n°2 : Correction (Déclaration & Accès)</span> ✍️

```php
<?php
// 1) Tableau indexé + accès au 1er et 3e élément
$prenoms = ["Alice", "Bob", "Chloé"];
echo $prenoms[0] . "<br>"; // Alice
echo $prenoms[2] . "<br>"; // Chloé

// 2) Tableau associatif + affichage formaté
$profil = [
    "nom"  => "Martin",
    "age"  => 27,
    "ville"=> "Bordeaux"
];

echo "Nom : {$profil['nom']} – Âge : {$profil['age']} – Ville : {$profil['ville']}";
```

---

## <span style="color:red;">Exercice n°3 : Correction (Ajouter, supprimer, réindexer)</span> ➕➖

```php
<?php
$fruits = ["Pomme", "Banane"];

// Ajoute "Cerise" en fin
$fruits[] = "Cerise";              // ou array_push($fruits, "Cerise");

// Ajoute "Kiwi" en début
array_unshift($fruits, "Kiwi");

// Supprime le premier élément
array_shift($fruits);

// Supprime l’élément d’index 1 s’il existe
if (isset($fruits[1])) {
    unset($fruits[1]);
}

// Réindexe pour repartir de 0
$fruits = array_values($fruits);

print_r($fruits);
```

*Remarque :* `array_values()` reconstruit des index consécutifs `0..n-1`.

---

## <span style="color:red;">Exercice n°4 : Correction (Parcourir avec foreach)</span> 🔁

```php
<?php
// 1) Indexé : afficher index et valeur
$notes = [12, 15, 9, 18];
foreach ($notes as $i => $val) {
    echo "Note #$i : $val<br>";
}

// 2) Associatif : afficher clé => valeur
$user = ["nom" => "Luc", "age" => 28, "ville" => "Lyon"];
foreach ($user as $cle => $valeur) {
    echo "$cle => $valeur<br>";
}
```

---

## <span style="color:red;">Exercice n°5 : Correction (Tri, fusion, recherche)</span> 🧪

```php
<?php
// 1) Tri décroissant en préservant les clés
$scores = ["Alice" => 15, "Bob" => 12, "Chloé" => 18, "David" => 14];
arsort($scores); // Chloé, Alice, David, Bob

foreach ($scores as $nom => $score) {
    echo "$nom : $score<br>";
}

echo "<hr>";

// 2) Fusion puis suppression des doublons
$a = ["rouge", "vert", "bleu"];
$b = ["bleu", "jaune"];

$fusion = array_merge($a, $b);   // ["rouge","vert","bleu","bleu","jaune"]
$unique = array_unique($fusion); // ["rouge","vert","bleu","jaune"]
print_r($unique);

echo "<hr>";

// 3) Recherche de "Paris"
$villes = ["Lyon", "Paris", "Marseille"];
if (in_array("Paris", $villes)) {
    echo "Paris est présent dans la liste.";
} else {
    echo "Paris n'est pas présent dans la liste.";
}
```

*Points clés :*  
- `arsort()` = tri **décroissant** en **préservant les clés**.  
- `array_merge()` concatène des tableaux indexés.  
- `array_unique()` retire les doublons et **préserve le premier index rencontré** (réindexer avec `array_values()` si besoin).  
- `in_array()` teste la présence d’une **valeur** dans un tableau.

---
