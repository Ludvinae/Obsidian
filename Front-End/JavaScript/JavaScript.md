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
- Object ( {nom : "Alice"} )
- Array 

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