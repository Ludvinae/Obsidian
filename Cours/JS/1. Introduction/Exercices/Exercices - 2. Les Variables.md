# <span style="color:red;">Introduction aux Variables en JavaScript : Exercices</span> 📘

---

## <span style="color:red;">Exercice n°1</span> 🧮  
**Déclaration et Affichage de Variables**

Déclarez les variables suivantes :
- Une chaîne `prenom` contenant votre prénom  
- Un nombre `age` contenant votre âge  
- Un tableau `couleurs` contenant trois couleurs de votre choix  
- Un objet `utilisateur` avec les propriétés `nom` et `ville`

Affichez ensuite toutes ces valeurs dans la console avec `console.log()`.

💡 **Tips pour apprenants :**  
> Utilisez `let` pour les variables que vous souhaitez modifier, et `const` pour celles qui ne changent pas.  
> N’oubliez pas les guillemets autour des chaînes de caractères !

---

## <span style="color:red;">Exercice n°2</span> 🔢  
**Types de Données**

Créez une variable de chaque type de données suivant :
- `Number`
- `String`
- `Boolean`
- `Array`
- `Object`
- `Null`
- `Undefined`

Affichez leur type dans la console avec `typeof`.

💡 **Tips pour apprenants :**  
> Utilisez la commande `console.log(typeof maVariable)` pour vérifier le type de données d’une variable.  
> C’est très utile pour déboguer votre code !

---

## <span style="color:red;">Exercice n°3</span> 💬  
**Concaténation et Template Strings**

Déclarez deux variables :  
- `prenom` = votre prénom  
- `ville` = votre ville  

Affichez dans la console une phrase du type :  
`Bonjour, je m'appelle [prenom] et j'habite à [ville].`  

💡 **Tips pour apprenants :**  
> Testez deux versions :  
> 1. Avec la concaténation classique (`+`)  
> 2. Avec les **template strings** (les backticks `` ` ``)

---

## <span style="color:red;">Exercice n°4</span> ⚙️  
**Mise à Jour de Variables**

Déclarez une variable `score` avec la valeur initiale `0`.  
Puis, augmentez sa valeur de `10`, puis de `5`, et enfin diminuez-la de `3`.  
Affichez le score final dans la console.

💡 **Tips pour apprenants :**  
> Vous pouvez écrire `score += 10` pour ajouter 10 à la valeur actuelle.  
> Même principe avec `-=` pour soustraire.

---

## <span style="color:red;">Exercice n°5</span> 🧠  
**Création d’un Profil Utilisateur Dynamique**

Créez un petit script qui :  
1. Demande à l’utilisateur son prénom et son âge avec `prompt()`  
2. Stocke ces valeurs dans un objet `profil`  
3. Affiche ensuite dans la console une phrase du type :  
   `"Bonjour [prenom], vous avez [age] ans !"`

💡 **Tips pour apprenants :**  
> Pour afficher plusieurs valeurs dans une phrase, préférez les **template strings** :  
> ```js
> console.log(`Bonjour ${profil.nom}, vous avez ${profil.age} ans.`);
> ```
> Cela rend votre code plus lisible et plus moderne.
