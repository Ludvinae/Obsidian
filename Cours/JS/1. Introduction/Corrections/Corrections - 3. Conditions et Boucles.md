# <span style="color:red;">Introduction aux Conditions et Boucles en JavaScript : Correction Exercices</span> 📘

---

## <span style="color:red;">Exercice n°1 : Correction</span> 🧮  
**Condition simple : Vérification de l’âge**
```js
let age = 20; // changez la valeur pour tester

if (age >= 18) {
  console.log("Vous êtes majeur");
} else {
  console.log("Vous êtes mineur");
}
```
✅ **Point clé :** `if` évalue une condition booléenne. Un seul des deux blocs s’exécute.

---

## <span style="color:red;">Exercice n°2 : Correction</span> ⚙️  
**Note d’évaluation avec `if...else if...else`**
```js
let note = 85; // 0 à 100

if (note >= 90) {
  console.log("Excellent !");
} else if (note >= 80) {
  console.log("Très bien !");
} else if (note >= 70) {
  console.log("Bien.");
} else {
  console.log("À améliorer.");
}
```
✅ **Point clé :** l’ordre des conditions va du **plus précis** au **moins précis**.

---

## <span style="color:red;">Exercice n°3 : Correction</span> 🔢  
**Boucle `for` : Compteur simple**
```js
for (let i = 1; i <= 10; i++) {
  console.log(i);
}
```
✅ **Point clé :** `i++` incrémente de 1 à chaque itération.

---

## <span style="color:red;">Exercice n°4 : Correction</span> 🔁  
**Boucle + Condition : Pairs & Impairs**
```js
for (let n = 1; n <= 20; n++) {
  if (n % 2 === 0) {
    console.log(`${n} est pair`);
  } else {
    console.log(`${n} est impair`);
  }
}
```
✅ **Point clé :** `n % 2 === 0` signifie que `n` est divisible par 2 → **pair**.

---

## <span style="color:red;">Exercice n°5 : Correction</span> 🧠  
**Boucle `while` : Compte à rebours**
```js
let compteur = 10;

while (compteur >= 1) {
  console.log(compteur);
  compteur--; // décrémentation pour éviter la boucle infinie
}
console.log("Décollage 🚀");
```
✅ **Point clé :** toujours faire évoluer la variable qui contrôle la condition.

---

## <span style="color:red;">Exercice n°6 : Correction</span> 🧩  
**Boucle `for...of` : Parcourir un tableau**
```js
const fruits = ["Pomme", "Banane", "Fraise", "Mangue"];

for (const fruit of fruits) {
  console.log(`J’aime le fruit : ${fruit}`);
}
```
✅ **Point clé :** `for...of` parcourt **directement** les valeurs du tableau.

---

## <span style="color:red;">Exercice n°7 : Correction</span> 🎯  
**Combinaison : FizzBuzz**
```js
for (let i = 1; i <= 30; i++) {
  if (i % 15 === 0) {            // divisible par 3 ET 5
    console.log("FizzBuzz");
  } else if (i % 3 === 0) {
    console.log("Fizz");
  } else if (i % 5 === 0) {
    console.log("Buzz");
  } else {
    console.log(i);
  }
}
```
✅ **Point clé :** tester d’abord le cas **3 et 5** (i.e. `i % 15 === 0`) pour ne pas le masquer.

---

### 🎉 Bonus : Version compacte du FizzBuzz (optionnel)
```js
for (let i = 1; i <= 30; i++) {
  const fizz = (i % 3 === 0) ? "Fizz" : "";
  const buzz = (i % 5 === 0) ? "Buzz" : "";
  console.log(fizz || buzz ? fizz + buzz : i);
}
```
✅ **Astuce :** assembler des chaînes conditionnelles permet de réduire le nombre de `if`.
