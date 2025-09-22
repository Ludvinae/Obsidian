[[JavaScript]]

On peut utiliser différentes méthodes pour interagir avec une chaîne de caractères:

- **`variable.charAt(index)`**: renvoie le caractère à la position d'index choisie
- **`variable.indexOf("character")`**: renvoie l'index de la première occurrence de `"character"`
- **`variable.lastIndexOf("character")`**: renvoie l'index de la dernière occurrence de `"character"`
- **`variable.trim()`**: pour enlever les espaces au début et à la fin de la chaîne de caractères
- **`variable.toUpperCase()`** et **`variable.toLowerCase()`**: transforme le String en majuscules et minuscules respectivement
- **`variable.repeat(x)`**: répète la chaîne de caractères x fois
- **`variable.startsWith("character")`**: renvoie *`true`* si le String commence par `"character"` 
- **`variable.endsWith("character")`**: renvoie *`true`* si le String fini par `"character"`
- **`variable.includes("character")`**: renvoie *`true`* si le String inclue `"character"`
- **`variable.replaceAll("charA", "charB")`**: remplace toutes les occurrences de `"charA"` par `"charB"`
- **`variable.padStart(x, "character")`**: ajouter `"character"` au début du String pour atteindre une taille x
- **`variable.padEnd(x, "character")`**: ajouter `"character"` à la fin du String pour atteindre une taille x
- **`variable.slice(indexDepart, indexFin)`**: crée un nouveau String avec la partie qui commence à `indexDepart` et fini à l'index précèdent `indexFin`; on peut omettre l'index de fin.


On peut récupérer la longueur d'une chaîne de caractères avec **`variable.length`**
