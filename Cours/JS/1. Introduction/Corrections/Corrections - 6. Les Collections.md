# <span style="color:red;">Les Collections en JavaScript : Correction Exercices</span> 📘

---

## <span style="color:red;">Exercice n°1 : Correction</span> 📖  
**Objets : création et accès**
```js
const utilisateur = {
  nom: "Alice",
  age: 25,
  ville: "Paris",
};

console.log(utilisateur.nom); // "Alice"
console.log(`${utilisateur.nom} a ${utilisateur.age} ans et habite à ${utilisateur.ville}.`);
```

---

## <span style="color:red;">Exercice n°2 : Correction</span> 🛠️  
**Objets : ajout, modification, suppression**
```js
const utilisateur = {
  nom: "Alice",
  age: 25,
  ville: "Paris",
};

// 1) Ajout
utilisateur.email = "alice@example.com";

// 2) Modification
utilisateur.ville = "Lyon";

// 3) Suppression
delete utilisateur.age;

// 4) Affichage final
console.log(utilisateur); // { nom: 'Alice', ville: 'Lyon', email: 'alice@example.com' }
```

---

## <span style="color:red;">Exercice n°3 : Correction</span> 📦  
**Set : valeurs uniques**
```js
const tags = ["js", "web", "js", "node", "web"];

// Vers Set (suppression des doublons)
const setTags = new Set(tags);

// Retour vers un tableau
const tagsUniques = [...setTags];

console.log(tagsUniques); // ["js", "web", "node"]
```

---

## <span style="color:red;">Exercice n°4 : Correction</span> 🗺️  
**Map : clés → valeurs**
```js
const produits = new Map([
  ["p1", "Clavier"],
  ["p2", "Souris"],
  ["p3", "Écran"],
]);

// Ajout
produits.set("p4", "Casque");

// Lecture
console.log(produits.get("p2")); // "Souris"

// Vérification
console.log(produits.has("p3")); // true

// Suppression
produits.delete("p1");

// Taille
console.log(produits.size); // 3

// Affichage complet
for (const [k, v] of produits) {
  console.log(`${k} → ${v}`);
}
```

---

## <span style="color:red;">Exercice n°5 : Correction</span> 🔄  
**Itérer sur Set et Map**
```js
// 1) Parcourir un Set
const valeurs = new Set([1, 2, 3, 4]);
for (const v of valeurs) {
  console.log(v);
}

// 2) Parcourir la Map 'produits'
const produits = new Map([
  ["p2", "Souris"],
  ["p3", "Écran"],
  ["p4", "Casque"],
]);

for (const [cle, val] of produits) {
  console.log(`Clé: ${cle} — Valeur: ${val}`);
}
```

---

## <span style="color:red;">Exercice n°6 : Correction</span> 🧮  
**Fréquence des éléments (Map vs Object)**
```js
const mots = ["js", "web", "js", "node", "js", "web"];

// 1) Compteur avec Object
const freqObj = {};
for (const mot of mots) {
  freqObj[mot] = (freqObj[mot] || 0) + 1;
}
console.log("Object :", freqObj); // { js: 3, web: 2, node: 1 }

// 2) Compteur avec Map
const freqMap = new Map();
for (const mot of mots) {
  freqMap.set(mot, (freqMap.get(mot) || 0) + 1);
}
console.log("Map :");
for (const [mot, count] of freqMap) {
  console.log(`${mot} → ${count}`);
}
```

---

## <span style="color:red;">Exercice n°7 : Correction</span> 🎛️  
**Choisir la bonne collection**
```js
// 1) Liste ordonnée de tâches → Array
const taches = ["Acheter du lait", "Écrire un mail", "Aller courir"];

// 2) Carnet d’adresses email → contact → Map
const carnet = new Map([
  ["alice@example.com", { nom: "Alice", tel: "0102030405" }],
  ["bob@example.com", { nom: "Bob", tel: "0607080910" }],
]);

// 3) Ensemble d’étiquettes sans doublon → Set
const etiquettes = new Set(["urgent", "maison", "urgent"]);

// 4) Fiche produit (nom, prix, enStock) → Object
const produit = { nom: "Clavier", prix: 79.9, enStock: true };

// Affichages
console.log(taches);
console.log(carnet.get("alice@example.com"));
console.log([...etiquettes]); // ["urgent", "maison"]
console.log(produit);
```

---

## <span style="color:red;">Exercice n°8 : Correction</span> 🔁  
**Transformations entre collections**
```js
const utilisateur = { nom: "Alice", age: 25, ville: "Paris" };

// Object → entries (tableau de paires)
const entries = Object.entries(utilisateur);
console.log("Entries :", entries);

// entries → Map
const map = new Map(entries);
console.log("Map :", map);

// Map → Object
const deMapVersObj = Object.fromEntries(map);
console.log("Object :", deMapVersObj);
```

---

## <span style="color:red;">Exercice n°9 : Correction</span> 🧠  
**Set : opérations ensemblistes**
```js
const a = new Set([1, 2, 3, 4]);
const b = new Set([3, 4, 5, 6]);

// Union
const union = new Set([...a, ...b]); // {1,2,3,4,5,6}

// Intersection
const intersection = new Set([...a].filter(x => b.has(x))); // {3,4}

// Différence a - b
const difference = new Set([...a].filter(x => !b.has(x))); // {1,2}

// Affichage sous forme de tableaux
console.log("Union :", [...union]);               // [1,2,3,4,5,6]
console.log("Intersection :", [...intersection]); // [3,4]
console.log("Différence :", [...difference]);     // [1,2]
```

---

## <span style="color:red;">Exercice n°10 : Correction</span> 🧩  
**Map avancée : clés objets**
```js
// Clés = objets utilisateur (il faut garder les mêmes références)
const alice = { id: 1, nom: "Alice" };
const bob   = { id: 2, nom: "Bob" };

const scores = new Map();
scores.set(alice, 120);
scores.set(bob, 95);

// Récupérer le score d'Alice
console.log("Score d'Alice :", scores.get(alice)); // 120

// Mettre à jour le score de Bob (+10)
scores.set(bob, scores.get(bob) + 10);

// Afficher toutes les paires clé-valeur
for (const [user, score] of scores) {
  console.log(`{id:${user.id}, nom:${user.nom}} → ${score}`);
}
```
