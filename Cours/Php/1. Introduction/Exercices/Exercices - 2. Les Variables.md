# <span style="color:red;">Introduction aux Variables en PHP : Exercices</span> 📘

---

## <span style="color:red;">Exercice n°1 : QCM sur les Variables</span> 🧩

### Objectif :
Tester ta compréhension des concepts fondamentaux liés aux variables en PHP.

### Questions :
1. Quelle est la bonne façon de déclarer une variable en PHP ?  
   - A) `nom = "Alice";`  
   - B) `$nom = "Alice";`  
   - C) `var nom = "Alice";`  

2. Quelle est la sortie du code suivant ?  
   ```php
   $x = 10;
   $y = 5;
   echo $x + $y;
   ```
   - A) 15  
   - B) 105  
   - C) Erreur de syntaxe  

3. Quelle fonction permet d’afficher le **type et la valeur** d’une variable ?  
   - A) `gettype()`  
   - B) `print()`  
   - C) `var_dump()`  

4. Quelle est la différence entre `$Nom` et `$nom` ?  
   - A) Aucune différence  
   - B) PHP fait la distinction entre les deux  
   - C) `$Nom` est réservé au système  

5. Quelle syntaxe est correcte pour concaténer deux variables `$prenom` et `$nom` ?  
   - A) `echo "$prenom $nom";`  
   - B) `echo $prenom + $nom;`  
   - C) `echo $prenom . $nom;`  

💡 **Tips pour apprenants :**  
Pense à relire la section sur la **concaténation** et la **sensibilité à la casse**. En PHP, `$nom` et `$Nom` sont deux variables totalement différentes !

---

## <span style="color:red;">Exercice n°2 : Déclaration et Affichage</span> ✍️

### Objectif :
Savoir déclarer et afficher des variables dans un script PHP.

### Consigne :
Déclare trois variables :  
- `$prenom` contenant ton prénom,  
- `$age` contenant ton âge,  
- `$ville` contenant ta ville.  

Affiche ensuite une phrase comme :  
```
Bonjour, je m'appelle [prenom], j'ai [age] ans et j'habite à [ville].
```

### Exemple attendu :
```php
$prenom = "Léo";
$age = 22;
$ville = "Lyon";

echo "Bonjour, je m'appelle $prenom, j'ai $age ans et j'habite à $ville.";
```

💡 **Tips pour apprenants :**  
Utilise les **guillemets doubles (`" "`)** pour insérer directement les variables dans la chaîne de texte. PHP interprète les variables dans les guillemets doubles, mais pas dans les simples (`' '`).

---

## <span style="color:red;">Exercice n°3 : Concaténation</span> 🔗

### Objectif :
Apprendre à combiner des chaînes avec des variables.

### Consigne :
Déclare deux variables :
- `$prenom = "Emma";`
- `$nom = "Dupont";`

Puis affiche le message :  
```
Bonjour Emma Dupont !
```
…en utilisant la **concaténation** (`.`).

### Exemple attendu :
```php
$prenom = "Emma";
$nom = "Dupont";

echo "Bonjour " . $prenom . " " . $nom . " !";
```

💡 **Tips pour apprenants :**  
La **concaténation** permet de relier plusieurs chaînes ou variables.  
Pense à ajouter des espaces manuellement avec `" "` sinon les mots seront collés !

---

## <span style="color:red;">Exercice n°4 : Changer la Valeur d'une Variable</span> 🔄

### Objectif :
Savoir modifier une variable et effectuer un calcul simple.

### Consigne :
1. Déclare une variable `$compteur` et attribue-lui la valeur `5`.  
2. Ajoute `3` à cette variable.  
3. Affiche le nouveau résultat.

### Exemple attendu :
```php
$compteur = 5;
$compteur = $compteur + 3;
echo $compteur; // Résultat : 8
```

💡 **Tips pour apprenants :**  
Tu peux aussi utiliser la notation abrégée :  
```php
$compteur += 3;
```
Elle signifie exactement la même chose !

---

## <span style="color:red;">Exercice n°5 : Typage Dynamique et var_dump()</span> 🔍

### Objectif :
Découvrir le typage dynamique et la fonction `var_dump()`.

### Consigne :
1. Crée plusieurs variables de types différents :
   ```php
   $texte = "Bonjour";
   $nombre = 42;
   $prix = 9.99;
   $vrai = true;
   ```
2. Utilise `var_dump()` pour afficher leur type et leur valeur.

### Exemple attendu :
```php
var_dump($texte);
var_dump($nombre);
var_dump($prix);
var_dump($vrai);
```

💡 **Tips pour apprenants :**  
La fonction `var_dump()` est ton **meilleur ami pour déboguer** ton code PHP.  
Elle te montre à la fois **le type** et **la valeur** de la variable. Très pratique pour comprendre le comportement de PHP.

---

## <span style="color:red;">Exercice n°6 : Variable et suppression</span> 🧹

### Objectif :
Apprendre à supprimer une variable avec `unset()`.

### Consigne :
1. Crée une variable `$temp = "Donnée temporaire";`  
2. Supprime-la avec `unset($temp);`  
3. Tente ensuite de faire un `echo $temp;` et observe ce qu’il se passe.

### Exemple attendu :
```php
$temp = "Donnée temporaire";
unset($temp);
echo $temp; // Erreur : variable inexistante
```

💡 **Tips pour apprenants :**  
Utiliser `unset()` libère la mémoire.  
C’est utile dans les scripts longs ou les boucles où tu veux nettoyer les variables devenues inutiles.

---

## <span style="color:red;">Exercice Bonus : Mélange des concepts</span> 🧠

### Objectif :
Mettre en pratique plusieurs notions (déclaration, concaténation, réaffectation).

### Consigne :
1. Crée une variable `$nom = "Lucas";`  
2. Crée une variable `$age = 20;`  
3. Affiche : `"Bonjour Lucas, tu as 20 ans."`  
4. Ajoute 5 à l’âge et affiche à nouveau : `"Dans 5 ans, tu auras 25 ans."`

### Exemple attendu :
```php
$nom = "Lucas";
$age = 20;

echo "Bonjour $nom, tu as $age ans.<br>";

$age = $age + 5;
echo "Dans 5 ans, tu auras $age ans.";
```

💡 **Tips pour apprenants :**  
Observe comment la **réaffectation** met à jour la valeur stockée dans `$age`.  
C’est un excellent exercice pour comprendre la **mémoire et la logique séquentielle** en PHP.

