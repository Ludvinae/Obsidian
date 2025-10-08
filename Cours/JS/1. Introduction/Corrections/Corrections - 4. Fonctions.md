# <span style="color:red;">Les Fonctions en JavaScript : Correction Exercices</span> 📘

---

## <span style="color:red;">Exercice n°1 : Correction</span> 🧮  
**Création et Appel de Fonction Simple**
```js
function direBonjour() {
  console.log("Bonjour à tous !");
}

// Appels (3 fois)
direBonjour();
direBonjour();
direBonjour();
```
✅ **À retenir :** Les **déclarations de fonctions** (avec `function`) sont *hoistées* : vous pouvez les appeler avant ou après leur définition. Ce n’est pas le cas des **expressions** ou **fonctions fléchées** assignées à une variable.

---

## <span style="color:red;">Exercice n°2 : Correction</span> ➕  
**Fonction avec Paramètres et Valeur de Retour**
```js
function addition(a, b) {
  return a + b;
}

const resultat1 = addition(4, 6);
const resultat2 = addition(10, 2);
console.log("Résultat 1 :", resultat1); // 10
console.log("Résultat 2 :", resultat2); // 12
```
✅ **À retenir :** Sans `return`, la fonction renvoie `undefined`.

---

## <span style="color:red;">Exercice n°3 : Correction</span> 🎯  
**Fonction avec Condition**
```js
function verifierAge(age) {
  if (age >= 18) {
    console.log("Vous êtes majeur");
  } else {
    console.log("Vous êtes mineur");
  }
}

// Tests
verifierAge(15);
verifierAge(18);
verifierAge(25);
```
✅ **Astuce :** L’égalité stricte et les comparaisons se font avec `===`, `>=`, etc.

---

## <span style="color:red;">Exercice n°4 : Correction</span> 🔁  
**Fonction avec Boucle Intégrée**
```js
function afficherMultiplication(nombre) {
  for (let i = 1; i <= 10; i++) {
    console.log(`${nombre} x ${i} = ${nombre * i}`);
  }
}

// Exemple
afficherMultiplication(3);
```
✅ **À retenir :** Structure d’une boucle `for` : `for (init; condition; miseAJour) { ... }`.

---

## <span style="color:red;">Exercice n°5 : Correction</span> 🧩  
**Fonction avec Paramètre par Défaut**
```js
function saluer(nom = "visiteur") {
  console.log(`Bonjour, ${nom} !`);
}

saluer();         // Bonjour, visiteur !
saluer("Alice");  // Bonjour, Alice !
```
✅ **Astuce :** Les valeurs par défaut évitent les `undefined` quand l’argument manque.

---

## <span style="color:red;">Exercice n°6 : Correction</span> ⚡  
**Fonction Fléchée (Arrow Function)**
```js
const carre = (x) => x * x;

console.log(carre(7)); // 49
```
✅ **À retenir :** Pour une **seule expression**, on peut omettre `{}` et `return`.

---

## <span style="color:red;">Exercice n°7 : Correction</span> 🧠  
**Fonction Callback**
```js
function executerFonction(fonction, valeur) {
  return fonction(valeur);
}

function doubler(x) {
  return x * 2;
}

const res = executerFonction(doubler, 10);
console.log(res); // 20
```
✅ **À retenir :** En JS, les fonctions sont des **valeurs** : on peut les passer en paramètres et les retourner.

---

## <span style="color:red;">Exercice n°8 : Correction</span> ⏰  
**Callback avec Temporisation**
```js
setTimeout(() => {
  console.log("Message affiché après 3 secondes");
}, 3000);
```
✅ **Astuce :** `setTimeout(fn, 3000)` lance `fn` après **3000 ms** (3 secondes).

---
