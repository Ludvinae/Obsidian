# <span style="color:red;">Les Tableaux en JavaScript : Correction Exercices</span> 📘

---

## <span style="color:red;">Exercice n°1 : Correction</span> 🧮  
**Création et Affichage d’un Tableau**
```js
const fruits = ["Pomme", "Banane", "Mangue", "Fraise"];

console.log(fruits);                  // Affiche tout le tableau
console.log("Premier :", fruits[0]);  // "Pomme"
console.log("Dernier :", fruits[fruits.length - 1]); // "Fraise"
```

---

## <span style="color:red;">Exercice n°2 : Correction</span> ✏️  
**Modification d’un Élément**
```js
const fruits = ["Pomme", "Banane", "Mangue", "Fraise"];

// Remplacer "Banane" par "Orange"
const indexBanane = fruits.indexOf("Banane");
if (indexBanane !== -1) {
  fruits[indexBanane] = "Orange";
}

// Ajouter "Cerise" à la fin
fruits.push("Cerise");

console.log(fruits); // ["Pomme","Orange","Mangue","Fraise","Cerise"]
```

---

## <span style="color:red;">Exercice n°3 : Correction</span> ➕➖  
**Ajout et Suppression d’Éléments**
```js
const nombres = [10, 20, 30, 40];

nombres.push(50);   // -> [10,20,30,40,50]
nombres.unshift(5); // -> [5,10,20,30,40,50]
nombres.pop();      // -> [5,10,20,30,40]
nombres.shift();    // -> [10,20,30,40]

console.log(nombres); // [10, 20, 30, 40]
```

---

## <span style="color:red;">Exercice n°4 : Correction</span> 🔍  
**Recherche d’un Élément dans un Tableau**
```js
const animaux = ["Chat", "Chien", "Lapin", "Poisson"];

const posChien = animaux.indexOf("Chien");   // 1
const tigrePresent = animaux.includes("Tigre"); // false

console.log("Index de 'Chien' :", posChien);
console.log("'Tigre' présent ?", tigrePresent);
```

---

## <span style="color:red;">Exercice n°5 : Correction</span> 🔁  
**Parcourir un Tableau**
```js
const pays = ["France", "Italie", "Espagne", "Portugal"];

// Boucle for
for (let i = 0; i < pays.length; i++) {
  console.log(`Je veux visiter ${pays[i]}`);
}

// Boucle for...of
for (const p of pays) {
  console.log(`Je veux visiter ${p}`);
}
```

---

## <span style="color:red;">Exercice n°6 : Correction</span> 🧠  
**Manipulations Avancées**
```js
const notes = [12, 18, 7, 14, 20];

// +2 à chaque note
const bonus = notes.map(n => n + 2);

// seulement >= 10
const reussite = notes.filter(n => n >= 10);

console.log("Notes d'origine :", notes); // intact
console.log("Avec bonus :", bonus);
console.log("Réussite (>=10) :", reussite);
```

---

## <span style="color:red;">Exercice n°7 : Correction</span> 📐  
**Tableaux Multidimensionnels**
```js
const matrice = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
];

// Afficher la valeur 5
console.log(matrice[1][1]); // 5

// Modifier 5 -> 50
matrice[1][1] = 50;

console.log(matrice);
// [
//   [1, 2, 3],
//   [4, 50, 6],
//   [7, 8, 9]
// ]
```

---

## <span style="color:red;">Exercice n°8 : Correction</span> 🧩  
**Concaténation et Extraction**
```js
const a = [1, 2, 3];
const b = [4, 5, 6];

const fusion = a.concat(b);   // [1,2,3,4,5,6]
const extrait = fusion.slice(0, 2); // [1,2]

console.log("Fusion :", fusion);
console.log("Extrait :", extrait);
```

---

## <span style="color:red;">Exercice n°9 : Correction</span> 🧮  
**Création d’une Phrase**
```js
const mots = ["Apprendre", "le", "JavaScript", "c’est", "génial"];

const phrase = mots.join(" ");
console.log(phrase); // "Apprendre le JavaScript c’est génial"
```

---

## <span style="color:red;">Exercice n°10 : Correction</span> ⚙️  
**Tri et Réorganisation**
```js
const nombres = [50, 10, 30, 20, 40];

// Tri croissant numérique
nombres.sort((a, b) => a - b);
console.log("Tri croissant :", nombres); // [10,20,30,40,50]

// Inverser l'ordre
nombres.reverse();
console.log("Ordre inversé :", nombres); // [50,40,30,20,10]
```
