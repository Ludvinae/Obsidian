# <span style="color:red;">Les Collections en JavaScript : Exercices</span> 📘

---

## <span style="color:red;">Exercice n°1</span> 📖  
**Objets : création et accès**

Créez un objet `utilisateur` avec les propriétés suivantes :  
- `nom` (string)  
- `age` (number)  
- `ville` (string)  

Affichez ensuite dans la console :  
- Le nom de l’utilisateur  
- La phrase : `"[nom] a [age] ans et habite à [ville]."`

💡 **Tips pour apprenants :**  
> Accédez aux propriétés avec `obj.prop` ou `obj["prop"]`. Les deux fonctionnent.

---

## <span style="color:red;">Exercice n°2</span> 🛠️  
**Objets : ajout, modification, suppression**

À partir de l’objet `utilisateur` :  
1. Ajoutez la propriété `email` (string).  
2. Modifiez la `ville`.  
3. Supprimez la propriété `age`.  
4. Affichez l’objet final dans la console.

💡 **Tips pour apprenants :**  
> Utilisez `objet.nouvelleProp = valeur` pour ajouter, et `delete objet.prop` pour supprimer.

---

## <span style="color:red;">Exercice n°3</span> 📦  
**Set : valeurs uniques**

Créez un tableau `tags = ["js", "web", "js", "node", "web"]`.  
- Convertissez-le en `Set` pour supprimer les doublons.  
- Reconvertissez le `Set` en tableau `tagsUniques`.  
- Affichez `tagsUniques`.

💡 **Tips pour apprenants :**  
> Conversion rapide : `const uniques = [...new Set(tableau)]`.

---

## <span style="color:red;">Exercice n°4</span> 🗺️  
**Map : clés → valeurs**

Créez une `Map` nommée `produits` avec ces paires :  
- `"p1" → "Clavier"`  
- `"p2" → "Souris"`  
- `"p3" → "Écran"`

Ensuite :  
- Ajoutez la paire `"p4" → "Casque"`  
- Affichez la valeur associée à `"p2"`  
- Vérifiez si `"p3"` existe  
- Supprimez `"p1"`  
- Affichez la taille de la `Map`

💡 **Tips pour apprenants :**  
> Méthodes utiles : `.set()`, `.get()`, `.has()`, `.delete()`, `.size`.

---

## <span style="color:red;">Exercice n°5</span> 🔄  
**Itérer sur Set et Map**

1. Créez un `Set` avec les valeurs `1, 2, 3, 4`. Parcourez-le et affichez chaque valeur.  
2. Parcourez la `Map` `produits` (de l’exercice 4) et affichez :  
   - `Clé: [clé] — Valeur: [valeur]`

💡 **Tips pour apprenants :**  
> Utilisez `for...of` :  
> - `for (const v of monSet) { ... }`  
> - `for (const [k, v] of maMap) { ... }`

---

## <span style="color:red;">Exercice n°6</span> 🧮  
**Fréquence des éléments (Map vs Object)**

Étant donné `mots = ["js", "web", "js", "node", "js", "web"]` :  
- Créez un **compteur de fréquences** avec un **Object** (`{ js: 3, web: 2, node: 1 }`).  
- Faites la même chose avec une **Map**.  
- Affichez les deux résultats.

💡 **Tips pour apprenants :**  
> Incrémentez avec : `compteur[mot] = (compteur[mot] || 0) + 1`.

---

## <span style="color:red;">Exercice n°7</span> 🎛️  
**Choisir la bonne collection**

Pour chaque besoin, indiquez quelle collection utiliser (**Array**, **Object**, **Set**, **Map**) puis créez une structure minimale :  
1. Une liste ordonnée de tâches à faire.  
2. Un carnet d’adresses (association `email → contact`).  
3. Un ensemble d’étiquettes sans doublon.  
4. La fiche d’un produit (nom, prix, enStock).

💡 **Tips pour apprenants :**  
> Pensez **type de clé**, **unicité**, **ordre**, **accès**.

---

## <span style="color:red;">Exercice n°8</span> 🔁  
**Transformations entre collections**

À partir de l’objet :  
```js
const utilisateur = { nom: "Alice", age: 25, ville: "Paris" };
```
- Transformez-le en **entries** (tableau de paires) puis en **Map**.  
- À partir de la **Map**, retransformez en **Object**.  
- Affichez chaque étape.

💡 **Tips pour apprenants :**  
> `Object.entries(obj)`, `new Map(entries)`, `Object.fromEntries(map)`.

---

## <span style="color:red;">Exercice n°9</span> 🧠  
**Set : opérations ensemblistes (facile++)**

Étant :  
```js
const a = new Set([1, 2, 3, 4]);
const b = new Set([3, 4, 5, 6]);
```
Créez :  
- **Union** → `{1,2,3,4,5,6}`  
- **Intersection** → `{3,4}`  
- **Différence** `a - b` → `{1,2}`  

Affichez chaque résultat (sous forme de tableau).

💡 **Tips pour apprenants :**  
> Utilisez le spread `[...]` et `filter()` avec `set.has(val)`.

---

## <span style="color:red;">Exercice n°10</span> 🧩  
**Map avancée : clés objets**

Créez une `Map` qui associe un **objet utilisateur** (`{id, nom}`) à son **score**.  
- Ajoutez deux utilisateurs (`{id:1, nom:"Alice"}`, `{id:2, nom:"Bob"}`) et des scores (ex : 120, 95).  
- Récupérez le score d’Alice via son objet comme clé.  
- Mettez à jour le score de Bob (+10).  
- Affichez toutes les paires.

💡 **Tips pour apprenants :**  
> Les **clés d’une Map** peuvent être des **objets** — pas seulement des chaînes.

---
