# <span style="color:red;">Introduction aux Variables en PHP : Correction Exercices</span> 📘

---

## <span style="color:red;">Exercice n°1 : Correction (QCM)</span> ✅
**1.** B) `$nom = "Alice";`  
**Explication :** En PHP, une variable commence toujours par `$`.

**2.** A) `15`  
**Explication :** `10 + 5 = 15`. L’opérateur `+` additionne deux nombres.

**3.** C) `var_dump()`  
**Explication :** `var_dump()` affiche **le type et la valeur**. `gettype()` ne donne que le type.

**4.** B) PHP fait la distinction (sensibilité à la casse).  
**Explication :** `$Nom` et `$nom` sont deux variables différentes.

**5.** A) `echo "$prenom $nom";` et C) `echo $prenom . $nom;` sont **toutes deux correctes**  
**Explication :**  
- **Interpolation** : `"$prenom $nom"` (dans des **guillemets doubles**)  
- **Concaténation** : `$prenom . " " . $nom` (avec le point `.`)

---

## <span style="color:red;">Exercice n°2 : Correction (Déclaration et Affichage)</span> ✍️
**Consigne rappel :** Déclarer `$prenom`, `$age`, `$ville` puis afficher une phrase complète.

**Proposition de correction :**
```php
<?php
$prenom = "Léo";
$age = 22;
$ville = "Lyon";

echo "Bonjour, je m'appelle $prenom, j'ai $age ans et j'habite à $ville.";
```

**Points clés :**
- Utiliser des **guillemets doubles** pour l’interpolation.
- Veiller aux **espaces** et à la **ponctuation** dans la chaîne.

---

## <span style="color:red;">Exercice n°3 : Correction (Concaténation)</span> 🔗
**Consigne rappel :** Afficher `Bonjour Emma Dupont !` via concaténation.

**Proposition de correction :**
```php
<?php
$prenom = "Emma";
$nom = "Dupont";

echo "Bonjour " . $prenom . " " . $nom . " !";
```

**Alternative (interpolation) :**
```php
<?php
echo "Bonjour $prenom $nom !";
```

**Point d’attention :** Ajouter un **espace** entre prénom et nom.

---

## <span style="color:red;">Exercice n°4 : Correction (Réaffectation)</span> 🔄
**Consigne rappel :** Partir de `5`, ajouter `3`, afficher le résultat.

**Proposition de correction :**
```php
<?php
$compteur = 5;
$compteur = $compteur + 3;
echo $compteur; // 8
```

**Version abrégée :**
```php
<?php
$compteur = 5;
$compteur += 3;
echo $compteur; // 8
```

**Point clé :** `+=` est une **notation composée** plus concise.

---

## <span style="color:red;">Exercice n°5 : Correction (Typage dynamique & var_dump)</span> 🔍
**Consigne rappel :** Créer plusieurs variables et utiliser `var_dump()`.

**Proposition de correction :**
```php
<?php
$texte = "Bonjour";
$nombre = 42;
$prix = 9.99;
$vrai = true;

var_dump($texte);  // string(7) "Bonjour"
var_dump($nombre); // int(42)
var_dump($prix);   // float(9.99)
var_dump($vrai);   // bool(true)
```

**Point clé :** PHP est **dynamique** : le type dépend de la **valeur affectée**.

---

## <span style="color:red;">Exercice n°6 : Correction (Suppression avec unset)</span> 🧹
**Consigne rappel :** Supprimer une variable avec `unset()` puis tenter de l’afficher.

**Proposition de correction :**
```php
<?php
$temp = "Donnée temporaire";
unset($temp);

// echo $temp; // ⚠️ Notice/Warning : variable non définie
// Pour éviter un avertissement :
if (isset($temp)) {
    echo $temp;
} else {
    echo "La variable \$temp n'existe plus.";
}
```

**Point clé :** Après `unset()`, la variable **n’est plus définie** (`isset($temp)` retourne `false`).

---

## <span style="color:red;">Exercice Bonus : Correction (Mélange des concepts)</span> 🧠
**Consigne rappel :** Afficher un message, réaffecter `$age`, réafficher.

**Proposition de correction :**
```php
<?php
$nom = "Lucas";
$age = 20;

echo "Bonjour $nom, tu as $age ans.<br>";

$age = $age + 5; // ou : $age += 5;
echo "Dans 5 ans, tu auras $age ans.";
```

**Points clés :**
- L’instruction est **séquentielle** : la seconde `echo` utilise la **nouvelle valeur**.
- Utiliser `<br>` pour un saut de ligne en sortie HTML.

---
