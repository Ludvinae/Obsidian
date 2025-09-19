[[Front-End]]

Langage de programmation orienté web, JavaScript s'occupe de la *logique* et du **comportement**. Le standard du  langage est défini par ECMAScript.

Types de variables:
- **var**: variable globale
- **let**: variable locale
- **const**: constant

Type de données:
- Boolean
- Number (integer & float)
- String
- Null
- Undefined
- Object (dictionnaire) 
- Array (liste)

**Switch**:
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

Les boucles:
- **for**:
	for (let i = 1; i <= 5; i++) {
	 console.log( "compteur: " + i);
	}
- **while**
	let i = 1;
	while (i <= 5) {
	    console.log("Compteur : " + i);
	    i++;
	}
- **do ... while** 
	let i = 1;
	do {
     console.log("Compteur : " + i);
     i++;
	} while (i <= 5);
- **for ... of**
	let fruits = ["pomme", "banane", "cerise"];
	for (let fruit of fruits) {
	    console.log(fruit);
	}

**Gestion des exceptions**:
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


### Fonctions

- Les **paramètres** sont définis lors de la déclaration.
- Les **arguments** sont passés lors de l’appel.

Fonctions **déclarées**:
	function saluer(nom) {
    console.log("Bonjour " + nom + " !");
	}
	saluer("Alice"); // Bonjour Alice !

Fonctions **expression**:
	const direBonjour = function(nom) {
    console.log("Salut " + nom + " !");
	};
	direBonjour("Bob"); // Salut Bob !

Fonctions **fléchées**:
	const addition = (a, b) => a + b;
	console.log(addition(5, 3)); // 8
	const afficherNom = nom => console.log(nom);
	afficherNom("Charlie"); // Charlie
