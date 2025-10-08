# <span style="color:red;">Introduction aux Conditions et Boucles en PHP : Correction Exercices</span> 📘

---

## <span style="color:red;">Exercice n°1 : Correction (QCM)</span> ✅

1) **B** — Elle exécute un bloc de code uniquement si une condition est vraie.  
*Rappel :* `if (condition) { /* code */ }`

2) **B** —  
```php
if ($x > 10) {
    echo "OK";
} else {
    echo "NON";
}
```
*Pourquoi :* La syntaxe PHP requiert les parenthèses, les accolades et pas de `endif` (sauf en syntaxe alternative des templates).

3) **B** — `for` quand on connaît le nombre d’itérations.

4) **B** — `break` arrête totalement la boucle en cours.

5) **B** — `do...while` s’exécute **au moins une fois** car la condition est testée après le bloc.

---

## <span style="color:red;">Exercice n°2 : Correction (Conditions simples)</span> 🧠

**Objectif :** Afficher le statut selon l’âge.

```php
<?php
$age = 15;

if ($age < 13) {
    echo "Enfant";
} elseif ($age < 18) {
    echo "Adolescent";
} else {
    echo "Adulte";
}
```

*Notes :*  
- Les intervalles sont continus et exclusifs grâce à l’ordre des tests.  
- Toujours utiliser des accolades pour la lisibilité.

---

## <span style="color:red;">Exercice n°3 : Correction (Boucle for)</span> 🔢

**Objectif :** Afficher 1 à 10 sur des lignes séparées.

```php
<?php
for ($i = 1; $i <= 10; $i++) {
    echo $i . "<br>";
}
```

*Notes :*  
- Initialisation → condition → incrément.  
- Attention à la condition d’arrêt `<= 10`.

---

## <span style="color:red;">Exercice n°4 : Correction (while + condition pair/impair)</span> 🔄

```php
<?php
$x = 1;

while ($x <= 5) {
    if ($x % 2 == 0) {
        echo "$x est pair.<br>";
    } else {
        echo "$x est impair.<br>";
    }
    $x++;
}
```

*Notes :*  
- `%` renvoie le reste de la division ; `== 0` ⇒ pair.  
- Ne pas oublier l’incrément dans la boucle.

---

## <span style="color:red;">Exercice n°5 : Correction (foreach)</span> 🍎

**Version simple (valeurs) :**
```php
<?php
$fruits = ["Pomme", "Banane", "Cerise", "Orange"];

foreach ($fruits as $fruit) {
    echo "J’aime la $fruit.<br>";
}
```

**Avec index (clé + valeur) :**
```php
<?php
foreach ($fruits as $index => $fruit) {
    echo "Fruit $index : $fruit<br>";
}
```

*Notes :*  
- `foreach ($array as $value)` ou `foreach ($array as $key => $value)`.

---

## <span style="color:red;">Exercice n°6 : Correction (break & continue)</span> 🧩

**Consigne :** Boucle 1→10, `break` à 7, ignorer les pairs.

```php
<?php
for ($i = 1; $i <= 10; $i++) {
    if ($i == 7) break;          // stoppe totalement la boucle
    if ($i % 2 == 0) continue;   // saute les nombres pairs
    echo $i . "<br>";            // affiche : 1, 3, 5
}
```

*Sortie :* `1`, `3`, `5` (la boucle s’arrête avant d’atteindre 7).

---

## <span style="color:red;">Exercice Bonus : Correction (FizzBuzz)</span> 🧠

```php
<?php
for ($i = 1; $i <= 20; $i++) {
    if ($i % 3 == 0 && $i % 5 == 0) {
        echo "FizzBuzz<br>";
    } elseif ($i % 3 == 0) {
        echo "Fizz<br>";
    } elseif ($i % 5 == 0) {
        echo "Buzz<br>";
    } else {
        echo $i . "<br>";
    }
}
```

*Notes :*  
- Tester la condition **la plus spécifique** (3 **et** 5) en premier.  
- L’ordre des `elseif` évite les collisions de règles.

---
