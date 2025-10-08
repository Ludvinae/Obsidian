# <span style="color:red;">Introduction aux Fonctions en PHP : Correction Exercices</span> 📘

---

## <span style="color:red;">Exercice n°1 : Correction (QCM)</span> ✅

1) **B** — `function`  
*Rappel :* déclarer une fonction se fait avec le mot-clé **`function`**.

2) **B** — `direBonjour();`  
*Rappel :* l’**appel** d’une fonction nécessite les **parenthèses**.

3) **B** — Elle **arrête** la fonction et **renvoie** une valeur.  
*Note :* `return` n’affiche rien ; il transmet une valeur au code appelant.

4) **B** — La **variable locale** existe uniquement **dans** la fonction.  
*Note :* les variables globales ne sont pas visibles dans une fonction sans `global`.

5) **B** — `strlen()`  
*Rappel :* `count()` sert aux **tableaux**, pas aux chaînes.

---

## <span style="color:red;">Exercice n°2 : Correction (Créer une fonction simple)</span> ✏️

```php
<?php
function direBonjour() {
    echo "Bonjour et bienvenue en PHP !";
}

direBonjour(); // Appel
```

**Points clés :**
- Parenthèses obligatoires même sans paramètres.
- On peut appeler la fonction autant de fois que nécessaire.

---

## <span style="color:red;">Exercice n°3 : Correction (Fonction avec paramètre)</span> 💬

```php
<?php
function saluer($nom) {
    echo "Bonjour, $nom !<br>";
}

saluer("Alice");
saluer("Bob");
saluer("Charlie");
```

**Points clés :**
- `$nom` est un **paramètre** local.
- L’interpolation fonctionne dans les **guillemets doubles**.

---

## <span style="color:red;">Exercice n°4 : Correction (Valeur par défaut)</span> ⚙️

```php
<?php
function presentation($nom = "Inconnu") {
    echo "Bonjour, je m'appelle $nom.<br>";
}

presentation("Léa"); // Bonjour, je m'appelle Léa.
presentation();      // Bonjour, je m'appelle Inconnu.
```

**Point clé :**
- La **valeur par défaut** est utilisée si aucun argument n’est fourni.

---

## <span style="color:red;">Exercice n°5 : Correction (Valeur de retour)</span> ↩️

```php
<?php
function additionner($a, $b) {
    return $a + $b;
}

$resultat = additionner(4, 6);
echo "Le résultat est : $resultat"; // Le résultat est : 10
```

**Points clés :**
- `return` **renvoie** la somme.
- Pour **afficher**, on utilise `echo` sur la valeur retournée.

---

## <span style="color:red;">Exercice n°6 : Correction (Locales vs Globales)</span> 🎯

```php
<?php
$message = "Bonjour global !";

function afficherMessage() {
    global $message; // rend la variable globale accessible ici
    echo $message;
}

afficherMessage(); // Affiche : Bonjour global !
```

**Points clés :**
- Sans `global`, `$message` serait **indéfinie** dans la fonction.
- Préférer **passer en paramètre** quand c’est possible (meilleure lisibilité/testabilité).

---

## <span style="color:red;">Exercice n°7 : Correction (Plusieurs valeurs de retour)</span> 📦

```php
<?php
function operations($a, $b) {
    $somme = $a + $b;
    $produit = $a * $b;
    return [$somme, $produit];
}

list($s, $p) = operations(4, 3);
echo "Somme : $s, Produit : $p"; // Somme : 7, Produit : 12
```

**Point clé :**
- On retourne un **tableau** puis on **déstructure** avec `list()`.

---

## <span style="color:red;">Exercice n°8 : Correction (Fonctions prédéfinies)</span> 🧰

```php
<?php
$texte = "PHP est amusant !";
echo "Longueur : " . strlen($texte) . "<br>";
echo "Majuscules : " . strtoupper($texte) . "<br>";
echo "Nombre aléatoire : " . rand(1, 50);
```

**Points clés :**
- `strlen()` → longueur de la chaîne.
- `strtoupper()` → majuscules.
- `rand(min, max)` → entier pseudo-aléatoire dans l’intervalle.

---

## <span style="color:red;">Exercice Bonus : Correction (Fonction anonyme)</span> ⚡

```php
<?php
$saluer = function($nom) {
    return "Salut, $nom !";
};

echo $saluer("Emma") . "<br>";
echo $saluer("Paul");
```

**Points clés :**
- Une **fonction anonyme** est stockée dans une **variable**.
- Très utile comme **callback** (ex. `array_map`, `array_filter`).

---
