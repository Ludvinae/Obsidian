# <span style="color:red;">Introduction aux Variables en JavaScript : Correction Exercices</span> 📘

---

## <span style="color:red;">Exercice n°1 : Correction</span> 🧮  
**Déclaration et Affichage de Variables**

```js
// 1) Déclarations
const prenom = "Alice";              // chaîne
let age = 22;                        // nombre
const couleurs = ["rouge", "vert", "bleu"]; // tableau
const utilisateur = { nom: "Dupont", ville: "Lyon" }; // objet

// 2) Affichages
console.log("Prénom :", prenom);
console.log("Âge :", age);
console.log("Couleurs :", couleurs);
console.log("Utilisateur :", utilisateur);

// Bonus : affichage lisible de l'objet
console.log(`Utilisateur -> Nom: ${utilisateur.nom}, Ville: ${utilisateur.ville}`);
```

✅ **À retenir** : utilisez `const` quand la référence ne change pas (ex. `couleurs`, `utilisateur`), `let` pour les valeurs amenées à évoluer (ex. `age`).

---

## <span style="color:red;">Exercice n°2 : Correction</span> 🔢  
**Types de Données & `typeof`**

```js
const n = 42;                 // Number
const s = "Bonjour";          // String
const b = true;               // Boolean
const arr = [1, 2, 3];        // Array (objet en JS)
const obj = { a: 1 };         // Object
const nul = null;             // Null (type historique "object")
let undef;                    // Undefined (non initialisée)

// Affichage des types
console.log(typeof n);    // "number"
console.log(typeof s);    // "string"
console.log(typeof b);    // "boolean"
console.log(typeof arr);  // "object"  <-- normal en JS
console.log(Array.isArray(arr)); // true (méthode correcte pour tester un tableau)
console.log(typeof obj);  // "object"
console.log(typeof nul);  // "object"  <-- particularité du langage
console.log(typeof undef);// "undefined"
```

✅ **À retenir** : `typeof []` renvoie `"object"`. Pour tester un tableau, utilisez **`Array.isArray()`**.

---

## <span style="color:red;">Exercice n°3 : Correction</span> 💬  
**Concaténation vs Template Strings**

```js
const prenom = "Alice";
const ville = "Toulouse";

// 1) Concaténation classique
console.log("Bonjour, je m'appelle " + prenom + " et j'habite à " + ville + ".");

// 2) Template string (recommandé)
console.log(`Bonjour, je m'appelle ${prenom} et j'habite à ${ville}.`);
```

✅ **À retenir** : les **template strings** (backticks) sont plus lisibles, surtout quand il y a plusieurs variables.

---

## <span style="color:red;">Exercice n°4 : Correction</span> ⚙️  
**Mise à Jour de Variables**

```js
let score = 0;   // valeur initiale

score += 10;     // score = 10
score += 5;      // score = 15
score -= 3;      // score = 12

console.log("Score final :", score); // 12
```

✅ **À retenir** : utilisez les **opérateurs composés** `+=`, `-=`, `*=`, `/=` pour écrire du code plus concis.

---

## <span style="color:red;">Exercice n°5 : Correction</span> 🧠  
**Profil Utilisateur Dynamique**

```js
// Saisie utilisateur (prompt renvoie une chaîne)
const saisiePrenom = prompt("Votre prénom :");
const saisieAge = prompt("Votre âge :");

// Conversion de l'âge en nombre
const age = Number(saisieAge);

// Construction de l'objet profil
const profil = {
  nom: saisiePrenom?.trim() || "Inconnu",
  age: Number.isNaN(age) ? null : age
};

// Affichage
if (profil.age === null) {
  console.log(`Bonjour ${profil.nom}, je n'ai pas compris votre âge.`);
} else {
  console.log(`Bonjour ${profil.nom}, vous avez ${profil.age} ans !`);
}

// Bonus : validation simple
if (profil.age !== null && profil.age < 0) {
  console.log("L'âge ne peut pas être négatif.");
}
```

💡 **Tips** :
- `prompt()` renvoie une **chaîne** → convertissez avec `Number(...)`.
- `Number.isNaN(...)` est préférable à `isNaN(...)` pour vérifier un nombre invalide.
- `trim()` nettoie les espaces superflus.
