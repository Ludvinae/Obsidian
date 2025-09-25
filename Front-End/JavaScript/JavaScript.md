---
tags:
  - callback
---

[[Front-End]]

Langage de programmation orienté web, JavaScript s'occupe de la *logique* et du *comportement*. Le standard du  langage est défini par ECMAScript.
On peut ajouter du Javascript directement dans le html en l'insérant directement entre des balises <script></script>, ou bien lier un fichier Javascript externe en utilisant l'attribut src="fichier.js" dans la balise script. Dans ce cas, il est conseillé de positionner la balise tout en bas du body.

**Types de variables**:
- *var*: variable globale (A éviter)
- *let*: variable locale
- *const*: constant

**Type de données**:
- Boolean
- Number (integer & float)
- String
- Null
- Undefined
- Object (dictionnaire) 
- Array (liste)

## Conditions:

On peut écrire une condition avec **if...else**:
```
if(condition) {
	exécute ce code si la condition est vraie
}
else {
	sinon exécute ce code
}
```

On peut aussi utiliser le **ternary operator** pour raccourcir la syntaxe lorsque l'on veux assigner une condition à une variable:
	let variable = condition ? codeSiVrai : codeSiFaux;

**Switch**:
Corresponds au *match* de Python. Contrairement à Python, on doit ajouter un *break* dans chaque *case* si l'on ne veux pas exécuter le code suivant le cas validé.

```
let jour = "lundi";

switch (jour) {
	case "lundi":
		console.log("Début de semaine");
		break;
	case "vendredi":
		console.log("Fin de semaine");
		break;
	default:
		console.log("Jour normal");
}
```

```ad-note
Dans l'exemple précèdent, si l'on inclus pas de *break* dans chaque cas, on afficherait les trois messages si la variable jour vaut "lundi". 
```

#### Opérateurs logiques

Pour combiner plusieurs conditions, on peut utiliser les opérateurs logiques:
- x **&&** y : x *et* y
- x **||** y : x *ou* y
- **!** x : *not* x
- (x **||** y) **&&** **!**(x **&&** y) : ou exclusif (x ou y, mais pas les deux en même temps)
  
## Boucles:

- **for**:
```
for (let i = 1; i <= 5; i++) {
	console.log( "compteur: " + i);
}
```

- **while**
```
let i = 1;
while (i <= 5) {
	console.log("Compteur : " + i);
	i++;
}
```

- **do ... while** 
```
let i = 1;
do {
	console.log("Compteur : " + i);
	i++;
} while (i <= 5);
```

- **for ... of**
```
let fruits = ["pomme", "banane", "cerise"];
for (let fruit of fruits) {
	console.log(fruit);
}
```


## Gestion des exceptions:

```
try {
	let result = 10 / 0;
	if (!isFinite(result)) {
		throw "Division par zéro impossible !";
	}
	console.log(result);
} catch (error) {
	console.log("Erreur : " + error);
} finally {
	console.log("Bloc finally exécuté quoi qu'il arrive.");
}
```


## Fonctions

- Les **paramètres** sont définis lors de la déclaration.
- Les **arguments** sont passés lors de l’appel.

Fonctions **déclarées**:
```
function saluer(nom) {
console.log("Bonjour " + nom + " !");
}
saluer("Alice"); // Bonjour Alice !
```

Fonctions **expression**:
```
const direBonjour = function(nom) {
console.log("Salut " + nom + " !");
};
direBonjour("Bob"); // Salut Bob !
```

Fonctions **fléchées**:
```
const addition = (a, b) => a + b;
console.log(addition(5, 3)); // 8
const afficherNom = nom => console.log(nom);
afficherNom("Charlie"); // Charlie
```

On peut aussi passer une fonction comme argument d'une autre fonction: c'est un **callback**. Le but est de n'afficher le callback qu'une fois que la première fonction ai fini d'exécuter. On passe la fonction que l'on veux appeler en second comme argument de la première *sans les parenthèses*, puis à la fin de la fonction on appelle le callback.

```
function hello(goodbye) {
console.log("Hello!");
goodbye();
}

function goodbye() {
console.log("Goodbye!")
}
```


## Structures de données

### Arrays

 Liste d'éléments qui peuvent être de type différents (mais ce n'est pas recommandé pour éviter les problèmes quand on traite ces données plus tard dans le programme)
  `let variable = ["element1", "element2", "element3"]`;
  
  On peut aussi faire une matrice avec un liste d'arrays:
```
	let variable = [[1, 2, 3]
					[4, 5, 6]
					[7, 8, 9]];
```

On peut utiliser un **spread operator** pour traiter les éléments d'un array de façon séparé sans passer par une boucle:

```
let variable = [1, 2, 3, 4, 5];
let maximum = Math.max(...variable);
```
(fonctionne aussi pour une chaîne de caractères)

**Rest parameters** fait l'inverse: on regroupe différents éléments à l'intérieur d'un array. Assigné à une fonction, on peut passer n'importe quel nombre d'arguments quand on l'appelle.

```
function regroupe(...liste) {
console.log(liste)}
let element1 = "abc"
let element2 = "def"
let element3 = "ghi"
regroupe(element1, element2, element3)
```

#### Array methods

##### map()
Accepte un callback en paramètre afin de parcourir une liste et appliquer cette fonction a toute la liste. map() va créer un nouvel array avec les données modifiées par la fonction.

```
const numbers = [1, 2, 3, 4, 5]
const squares = numbers.map(squareNumber)

def squareNumber(element) {
	return Math.pow(element, 2)
}
```

##### filter()
Crée une nouvelle liste avec les éléments filtrés par le callback ajouté en paramètre de la méthode filter().

```

```

