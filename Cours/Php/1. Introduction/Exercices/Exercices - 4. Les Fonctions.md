# <span style="color:red;">Introduction aux Fonctions en PHP : Exercices</span> 📘  

---

## <span style="color:red;">Exercice n°1 : QCM sur les Fonctions</span> 🧩  

### Objectif :  
Vérifier ta compréhension des bases des fonctions en PHP.  

### Questions :  
1. Quelle instruction permet de **déclarer** une fonction en PHP ?  
   - A) `declare`  
   - B) `function`  
   - C) `def`  

2. Quelle est la **bonne façon** d’appeler une fonction nommée `direBonjour` ?  
   - A) `direBonjour;`  
   - B) `direBonjour();`  
   - C) `echo direBonjour;`  

3. Que fait l’instruction `return` dans une fonction ?  
   - A) Elle affiche du texte.  
   - B) Elle arrête la fonction et renvoie une valeur.  
   - C) Elle efface toutes les variables.  

4. Quelle est la différence entre une **variable locale** et une **variable globale** ?  
   - A) Aucune différence.  
   - B) La variable locale existe uniquement dans la fonction.  
   - C) La variable globale est détruite après la fonction.  

5. Quelle fonction PHP renvoie la longueur d’une chaîne de caractères ?  
   - A) `count()`  
   - B) `strlen()`  
   - C) `size()`  

💡 **Tips pour apprenants :**  
- Les **fonctions** sont toujours créées avec le mot-clé `function`.  
- `return` permet de **récupérer une valeur**, tandis que `echo` **affiche** le texte directement.  
- Les variables **locales** sont internes à la fonction, contrairement aux **globales**.  

---

## <span style="color:red;">Exercice n°2 : Créer une fonction simple</span> ✏️  

### Objectif :  
Apprendre à déclarer et appeler une fonction.  

### Consigne :  
Crée une fonction appelée `direBonjour()` qui affiche **"Bonjour et bienvenue en PHP !"**  

### Exemple attendu :
```php
<?php
function direBonjour() {
    echo "Bonjour et bienvenue en PHP !";
}

direBonjour();
```

💡 **Tips pour apprenants :**  
- Toujours mettre les **parenthèses** après le nom de la fonction, même si elle n’a **aucun paramètre**.  
- Tu peux appeler la fonction **autant de fois que tu veux**.

---

## <span style="color:red;">Exercice n°3 : Fonction avec Paramètre</span> 💬  

### Objectif :  
Comprendre comment passer un paramètre à une fonction.  

### Consigne :  
Crée une fonction `saluer($nom)` qui affiche le message :  
```
Bonjour, [nom] !
```  
Appelle-la avec plusieurs prénoms différents.  

### Exemple attendu :
```php
<?php
function saluer($nom) {
    echo "Bonjour, $nom !<br>";
}

saluer("Alice");
saluer("Bob");
saluer("Charlie");
```

💡 **Tips pour apprenants :**  
Les **paramètres** rendent ta fonction **dynamique** et réutilisable pour plusieurs valeurs.  

---

## <span style="color:red;">Exercice n°4 : Valeur par Défaut</span> ⚙️  

### Objectif :  
Apprendre à définir des paramètres optionnels avec une valeur par défaut.  

### Consigne :  
Crée une fonction `presentation($nom = "Inconnu")` qui affiche :  
```
Bonjour, je m'appelle [nom].
```  
Teste la fonction **avec** et **sans** argument.  

### Exemple attendu :
```php
<?php
function presentation($nom = "Inconnu") {
    echo "Bonjour, je m'appelle $nom.<br>";
}

presentation("Léa");
presentation();
```

💡 **Tips pour apprenants :**  
Si une valeur par défaut est définie, PHP l’utilisera **automatiquement** si tu n’envoies pas d’argument.  

---

## <span style="color:red;">Exercice n°5 : Fonction avec Valeur de Retour</span> ↩️  

### Objectif :  
Savoir récupérer une valeur renvoyée par une fonction.  

### Consigne :  
Crée une fonction `additionner($a, $b)` qui retourne la somme des deux nombres.  
Affiche ensuite le résultat avec `echo`.  

### Exemple attendu :
```php
<?php
function additionner($a, $b) {
    return $a + $b;
}

$resultat = additionner(4, 6);
echo "Le résultat est : $resultat";
```

💡 **Tips pour apprenants :**  
- `return` **renvoie la valeur**, mais ne l’affiche pas.  
- Pour afficher, il faut utiliser `echo` ou stocker le résultat dans une variable.  

---

## <span style="color:red;">Exercice n°6 : Variables Locales et Globales</span> 🎯  

### Objectif :  
Comprendre la différence entre portée locale et globale.  

### Consigne :  
1. Crée une variable `$message = "Bonjour global !";`  
2. Crée une fonction `afficherMessage()` qui affiche cette variable **en utilisant `global`**.  

### Exemple attendu :
```php
<?php
$message = "Bonjour global !";

function afficherMessage() {
    global $message;
    echo $message;
}

afficherMessage();
```

💡 **Tips pour apprenants :**  
- Par défaut, les fonctions **ne voient pas** les variables globales.  
- Le mot-clé `global` permet de **rendre la variable accessible** à l’intérieur de la fonction.  

---

## <span style="color:red;">Exercice n°7 : Plusieurs Valeurs de Retour</span> 📦  

### Objectif :  
Retourner plusieurs valeurs en utilisant un tableau.  

### Consigne :  
Crée une fonction `operations($a, $b)` qui retourne la **somme** et le **produit** de `$a` et `$b`.  
Affiche les résultats avec `list()`.  

### Exemple attendu :
```php
<?php
function operations($a, $b) {
    $somme = $a + $b;
    $produit = $a * $b;
    return [$somme, $produit];
}

list($s, $p) = operations(4, 3);
echo "Somme : $s, Produit : $p";
```

💡 **Tips pour apprenants :**  
- `list()` permet d’extraire plusieurs valeurs d’un tableau en une seule ligne.  
- Toujours retourner un **tableau** si tu veux renvoyer plusieurs résultats.  

---

## <span style="color:red;">Exercice n°8 : Fonctions Prédéfinies</span> 🧰  

### Objectif :  
Découvrir les fonctions natives de PHP.  

### Consigne :  
Crée un script qui utilise les fonctions suivantes :  
1. `strlen()` → pour afficher la longueur d’une chaîne  
2. `strtoupper()` → pour la mettre en majuscules  
3. `rand()` → pour générer un nombre aléatoire entre 1 et 50  

### Exemple attendu :
```php
<?php
$texte = "PHP est amusant !";
echo "Longueur : " . strlen($texte) . "<br>";
echo "Majuscules : " . strtoupper($texte) . "<br>";
echo "Nombre aléatoire : " . rand(1, 50);
```

💡 **Tips pour apprenants :**  
- PHP dispose de **centaines de fonctions intégrées**.  
- Utilise la documentation officielle 👉 [https://www.php.net/manual/fr/](https://www.php.net/manual/fr/)  

---

## <span style="color:red;">Exercice Bonus : Fonction Anonyme</span> ⚡  

### Objectif :  
Créer et utiliser une fonction anonyme.  

### Consigne :  
Crée une fonction anonyme assignée à une variable `$saluer` qui prend un nom et renvoie une phrase du type :  
```
Salut, [nom] !
```  
Appelle ensuite cette fonction avec plusieurs prénoms.  

### Exemple attendu :
```php
<?php
$saluer = function($nom) {
    return "Salut, $nom !";
};

echo $saluer("Emma") . "<br>";
echo $saluer("Paul");
```

💡 **Tips pour apprenants :**  
Les **fonctions anonymes** sont très utiles quand tu veux passer une fonction **en argument** à une autre (comme dans `array_map()` ou `array_filter()`).  

---

✅ **Conseil final :**  
Les **fonctions** te permettent d’organiser ton code efficacement.  
En les combinant avec des conditions, des boucles et des tableaux,  
tu pourras créer des scripts **puissants et maintenables**. 🚀  
