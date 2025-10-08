# <span style="color:red;">Les Tableaux en JavaScript : Exercices</span> 📘

---

## <span style="color:red;">Exercice n°1</span> 🧮  
**Création et Affichage d’un Tableau**

Créez un tableau `fruits` contenant les éléments suivants : `"Pomme"`, `"Banane"`, `"Mangue"`, `"Fraise"`.  
Affichez le tableau entier dans la console, puis affichez uniquement le **premier** et le **dernier** élément.

💡 **Tips pour apprenants :**  
> Vous pouvez accéder à un élément avec `tableau[indice]` et obtenir le dernier élément avec `tableau[tableau.length - 1]`.

---

## <span style="color:red;">Exercice n°2</span> ✏️  
**Modification d’un Élément**

À partir du tableau `fruits` créé précédemment :  
- Remplacez `"Banane"` par `"Orange"`.  
- Ajoutez `"Cerise"` à la fin du tableau.  
- Affichez le tableau modifié dans la console.

💡 **Tips pour apprenants :**  
> Utilisez `push()` pour ajouter à la fin et l’accès par indice pour remplacer un élément.

---

## <span style="color:red;">Exercice n°3</span> ➕➖  
**Ajout et Suppression d’Éléments**

Créez un tableau `nombres = [10, 20, 30, 40]`.  
- Ajoutez `50` à la fin avec `push()`.  
- Ajoutez `5` au début avec `unshift()`.  
- Supprimez le dernier élément avec `pop()`.  
- Supprimez le premier élément avec `shift()`.  
Affichez le tableau final.

💡 **Tips pour apprenants :**  
> Les méthodes `push`, `pop`, `shift` et `unshift` modifient directement le tableau.

---

## <span style="color:red;">Exercice n°4</span> 🔍  
**Recherche d’un Élément dans un Tableau**

Créez un tableau `animaux = ["Chat", "Chien", "Lapin", "Poisson"]`.  
- Trouvez la position de `"Chien"` à l’aide de `indexOf()`.  
- Vérifiez si `"Tigre"` est présent à l’aide de `includes()`.  
- Affichez les résultats dans la console.

💡 **Tips pour apprenants :**  
> `indexOf()` renvoie `-1` si l’élément n’existe pas dans le tableau.

---

## <span style="color:red;">Exercice n°5</span> 🔁  
**Parcourir un Tableau**

Créez un tableau `pays = ["France", "Italie", "Espagne", "Portugal"]`.  
- Utilisez une boucle `for` pour afficher chaque pays.  
- Ensuite, utilisez une boucle `for...of` pour faire la même chose.  
- Affichez dans la console : `"Je veux visiter [pays]"`.

💡 **Tips pour apprenants :**  
> `for...of` est plus moderne et lisible pour parcourir les tableaux.

---

## <span style="color:red;">Exercice n°6</span> 🧠  
**Manipulations Avancées**

Créez un tableau `notes = [12, 18, 7, 14, 20]`.  
- Utilisez `map()` pour créer un nouveau tableau `bonus` où chaque note est augmentée de `2`.  
- Utilisez `filter()` pour créer un tableau `reussite` contenant uniquement les notes **supérieures ou égales à 10**.  
- Affichez les deux nouveaux tableaux dans la console.

💡 **Tips pour apprenants :**  
> `map()` ne modifie pas le tableau original, il crée un **nouveau tableau**.

---

## <span style="color:red;">Exercice n°7</span> 📐  
**Tableaux Multidimensionnels**

Créez une matrice (tableau de tableaux) :
```js
let matrice = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
];
```
- Affichez la valeur `5` dans la console.  
- Changez cette valeur en `50`.  
- Affichez la matrice mise à jour.

💡 **Tips pour apprenants :**  
> Utilisez `matrice[ligne][colonne]` pour accéder à un élément précis.

---

## <span style="color:red;">Exercice n°8</span> 🧩  
**Concaténation et Extraction**

Créez deux tableaux :
```js
let a = [1, 2, 3];
let b = [4, 5, 6];
```
- Fusionnez-les dans un tableau `fusion` avec `concat()`.  
- Extrayez les deux premiers éléments avec `slice()` et stockez-les dans `extrait`.  
- Affichez les deux tableaux (`fusion` et `extrait`).

💡 **Tips pour apprenants :**  
> `concat()` ne modifie pas les tableaux d’origine, il retourne un **nouveau tableau**.

---

## <span style="color:red;">Exercice n°9</span> 🧮  
**Création d’une Phrase**

Créez un tableau :
```js
let mots = ["Apprendre", "le", "JavaScript", "c’est", "génial"];
```
- Utilisez `join(" ")` pour créer une phrase complète.  
- Affichez la phrase dans la console.

💡 **Tips pour apprenants :**  
> `join()` est parfait pour transformer un tableau de mots en phrase lisible.

---

## <span style="color:red;">Exercice n°10</span> ⚙️  
**Tri et Réorganisation**

Créez un tableau :
```js
let nombres = [50, 10, 30, 20, 40];
```
- Triez les nombres par ordre croissant à l’aide de `sort()`.  
- Inversez l’ordre avec `reverse()`.  
- Affichez les résultats après chaque opération.

💡 **Tips pour apprenants :**  
> `sort()` trie les valeurs **comme des chaînes** par défaut.  
> Pour trier correctement des nombres, utilisez :  
> ```js
> nombres.sort((a, b) => a - b);
> ```
