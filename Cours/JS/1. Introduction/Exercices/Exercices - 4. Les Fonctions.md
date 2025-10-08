# <span style="color:red;">Les Fonctions en JavaScript : Exercices</span> 📘

---

## <span style="color:red;">Exercice n°1</span> 🧮  
**Création et Appel de Fonction Simple**

Créez une fonction `direBonjour()` qui affiche dans la console :  
👉 `"Bonjour à tous !"`

Ensuite, appelez cette fonction **3 fois** de suite.

💡 **Tips pour apprenants :**  
> Les fonctions doivent être **déclarées avant leur appel** (sauf si vous utilisez une fonction fléchée stockée dans une variable).

---

## <span style="color:red;">Exercice n°2</span> ➕  
**Fonction avec Paramètres et Valeur de Retour**

Créez une fonction `addition(a, b)` qui **additionne deux nombres** et renvoie le résultat.  
Affichez le résultat dans la console.

💡 **Tips pour apprenants :**  
> Pensez à utiliser `return` pour récupérer la valeur hors de la fonction.  
> Sans `return`, la fonction renverra `undefined`.

---

## <span style="color:red;">Exercice n°3</span> 🎯  
**Fonction avec Condition**

Créez une fonction `verifierAge(age)` qui affiche :
- `"Vous êtes majeur"` si `age >= 18`
- `"Vous êtes mineur"` sinon.

Testez la fonction avec plusieurs valeurs.

💡 **Tips pour apprenants :**  
> Vous pouvez passer différents arguments à chaque appel de fonction, par exemple :  
> `verifierAge(15)` ou `verifierAge(25)`.

---

## <span style="color:red;">Exercice n°4</span> 🔁  
**Fonction avec Boucle Intégrée**

Créez une fonction `afficherMultiplication(nombre)` qui affiche la **table de multiplication** du nombre passé en argument.  
Exemple pour `afficherMultiplication(3)` :  
```
3 x 1 = 3  
3 x 2 = 6  
3 x 3 = 9  
...
```

💡 **Tips pour apprenants :**  
> Utilisez une boucle `for` à l’intérieur de la fonction.  
> La table va de 1 à 10.

---

## <span style="color:red;">Exercice n°5</span> 🧩  
**Fonction avec Paramètre par Défaut**

Créez une fonction `saluer(nom = "visiteur")` qui affiche :  
👉 `"Bonjour, [nom] !"`

Appelez la fonction **avec** et **sans** argument.

💡 **Tips pour apprenants :**  
> Les paramètres par défaut sont pratiques pour éviter les erreurs si aucun argument n’est fourni.

---

## <span style="color:red;">Exercice n°6</span> ⚡  
**Fonction Fléchée (Arrow Function)**

Créez une fonction fléchée `carre` qui prend un nombre et retourne son carré.  
Affichez le résultat pour le nombre `7`.

💡 **Tips pour apprenants :**  
> Les fonctions fléchées sont plus concises.  
> Exemple :  
> ```js
> const carre = (x) => x * x;
> ```

---

## <span style="color:red;">Exercice n°7</span> 🧠  
**Fonction Callback**

Créez une fonction `executerFonction(fonction, valeur)` qui prend **une fonction** et **une valeur**,  
puis exécute la fonction avec cette valeur.  

Ensuite, créez une fonction `doubler(x)` qui retourne le double de `x`.  
Appelez `executerFonction(doubler, 10)` pour afficher le résultat.

💡 **Tips pour apprenants :**  
> C’est le principe des **callbacks** : passer une fonction comme argument d’une autre.

---

## <span style="color:red;">Exercice n°8</span> ⏰  
**Callback avec Temporisation**

Utilisez la fonction `setTimeout()` pour afficher dans la console :  
👉 `"Message affiché après 3 secondes"`  
après un délai de **3 secondes**.

💡 **Tips pour apprenants :**  
> Le deuxième paramètre de `setTimeout()` correspond au temps en **millisecondes** (1000 ms = 1 seconde).
