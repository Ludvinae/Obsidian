# <span style="color:red;">Introduction aux Conditions et Boucles en PHP : Exercices</span> 📘  

---

## <span style="color:red;">Exercice n°1 : QCM sur les Conditions et Boucles</span> 🧩  

### Objectif :  
Vérifier ta compréhension des structures conditionnelles et des boucles en PHP.  

### Questions :  
1. Que fait une **instruction `if`** en PHP ?  
   - A) Elle répète une action plusieurs fois.  
   - B) Elle exécute un bloc de code uniquement si une condition est vraie.  
   - C) Elle arrête le programme immédiatement.  

2. Quelle est la **bonne syntaxe** pour une condition `if...else` ?  
   - A)  
   ```php
   if condition:
       // code
   else:
       // code
   endif;
   ```  
   - B)  
   ```php
   if ($x > 10) {
       echo "OK";
   } else {
       echo "NON";
   }
   ```  
   - C)  
   ```php
   if ($x > 10);
   echo "OK";
   else echo "NON";
   ```  

3. Quelle boucle est utilisée quand on **connaît à l’avance le nombre d’itérations** ?  
   - A) `foreach`  
   - B) `for`  
   - C) `while`  

4. Que fait l’instruction `break` dans une boucle ?  
   - A) Elle saute une itération.  
   - B) Elle arrête totalement la boucle.  
   - C) Elle relance la boucle depuis le début.  

5. Quelle est la différence entre `while` et `do...while` ?  
   - A) Aucune, elles sont identiques.  
   - B) `do...while` s’exécute toujours au moins une fois.  
   - C) `while` s’exécute toujours au moins une fois.  

💡 **Tips pour apprenants :**  
- Retient :  
  - `if` = choix  
  - `for` = compter  
  - `while` = répéter tant que vrai  
  - `foreach` = parcourir un tableau  
- Les **conditions** pilotent les **décisions**, les **boucles** pilotent les **répétitions**.

---

## <span style="color:red;">Exercice n°2 : Conditions simples</span> 🧠  

### Objectif :  
Apprendre à utiliser les conditions `if`, `elseif`, et `else`.  

### Consigne :  
Écris un script PHP qui détermine le **statut d’un utilisateur** selon son âge :  
- Moins de 13 ans → “Enfant”  
- De 13 à 17 ans → “Adolescent”  
- 18 ans et plus → “Adulte”  

### Exemple attendu :
```php
$age = 15;

if ($age < 13) {
    echo "Enfant";
} elseif ($age < 18) {
    echo "Adolescent";
} else {
    echo "Adulte";
}
```

💡 **Tips pour apprenants :**  
Toujours mettre des **accolades `{}`** même si la condition ne contient qu’une ligne.  
Cela améliore la lisibilité et évite des erreurs futures.

---

## <span style="color:red;">Exercice n°3 : Boucle For</span> 🔢  

### Objectif :  
Pratiquer la boucle `for`.  

### Consigne :  
Écris une boucle `for` qui affiche les nombres de **1 à 10** sur des lignes séparées.  

### Exemple attendu :
```php
for ($i = 1; $i <= 10; $i++) {
    echo $i . "<br>";
}
```

💡 **Tips pour apprenants :**  
- `$i++` signifie “incrémente de 1”.  
- Si tu veux compter à rebours, utilise `$i--`.  
- Vérifie toujours la **condition d’arrêt**, sinon ta boucle peut devenir **infinie**.

---

## <span style="color:red;">Exercice n°4 : Boucle While et condition</span> 🔄  

### Objectif :  
Associer une **boucle** et une **condition** pour afficher des messages personnalisés.  

### Consigne :  
Crée une boucle `while` qui compte de 1 à 5 et affiche :  
- “Nombre pair” si le nombre est pair  
- “Nombre impair” sinon  

### Exemple attendu :
```php
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

💡 **Tips pour apprenants :**  
Le symbole `%` est l’**opérateur modulo** → il donne le **reste de la division**.  
- Exemple : `4 % 2 = 0` → pair  
- Exemple : `5 % 2 = 1` → impair  

---

## <span style="color:red;">Exercice n°5 : Boucle Foreach</span> 🍎  

### Objectif :  
Découvrir la boucle `foreach` pour parcourir un tableau.  

### Consigne :  
Affiche la phrase `"J’aime la [valeur]"` pour chaque fruit du tableau :  
```php
$fruits = ["Pomme", "Banane", "Cerise", "Orange"];
```

### Exemple attendu :
```php
$fruits = ["Pomme", "Banane", "Cerise", "Orange"];

foreach ($fruits as $fruit) {
    echo "J’aime la $fruit.<br>";
}
```

💡 **Tips pour apprenants :**  
- `foreach` est la **boucle la plus simple** pour lire un tableau.  
- Utilise la syntaxe `foreach ($tableau as $cle => $valeur)` pour afficher aussi les **clés** :
  ```php
  foreach ($fruits as $index => $fruit) {
      echo "Fruit $index : $fruit<br>";
  }
  ```

---

## <span style="color:red;">Exercice n°6 : Break et Continue</span> 🧩  

### Objectif :  
Comprendre comment contrôler le flux d’une boucle.  

### Consigne :  
Crée une boucle `for` allant de 1 à 10 :  
- Arrête la boucle quand `$i` atteint 7 avec `break`.  
- Ignore les nombres pairs avec `continue`.  

### Exemple attendu :
```php
for ($i = 1; $i <= 10; $i++) {
    if ($i == 7) break;
    if ($i % 2 == 0) continue;
    echo $i . "<br>";
}
```

💡 **Tips pour apprenants :**  
- `break` = “je sors complètement de la boucle”  
- `continue` = “je passe à la prochaine itération sans exécuter le reste du code”  

---

## <span style="color:red;">Exercice Bonus : Combinaison Boucles et Conditions</span> 🧠  

### Objectif :  
Mettre en pratique toutes les notions vues.  

### Consigne :  
Écris un programme qui affiche les nombres de 1 à 20.  
- Si le nombre est multiple de 3 → affiche “Fizz”  
- Si le nombre est multiple de 5 → affiche “Buzz”  
- Si le nombre est multiple de 3 et 5 → affiche “FizzBuzz”  

### Exemple attendu :
```php
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

💡 **Tips pour apprenants :**  
Cet exercice est un **classique** des tests de logique.  
Toujours **vérifier la condition la plus spécifique** (ici le double multiple de 3 et 5) **en premier**, sinon elle ne sera jamais exécutée.

---

✅ **Conseil final :**  
En PHP, les **conditions** et **boucles** sont les fondations de la logique de tout programme.  
Pratique-les en essayant d’automatiser de petites tâches :  
- compter,  
- filtrer des données,  
- ou répéter des actions.  

Chaque test t’aidera à comprendre **le raisonnement algorithmique**, essentiel pour devenir un bon développeur web. 💪
