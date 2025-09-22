Apprendre un langage de programmation, c’est comme apprendre une nouvelle langue. Dans la première partie de ce cours, nous allons découvrir le langage JavaScript : son vocabulaire et sa syntaxe… et vous aurez surtout l’occasion de vous entraîner sur des exercices !

# Découvrez les variables

En informatique, une **variable** est un conteneur qui stocke la donnée temporairement au sein de votre code. Cela vous permet d’enregistrer des données.

En tant que développeur, vous utilisez des variables pour stocker un nom d’utilisateur ou encore un chiffre représentant le nombre de produits restants dans votre stock. Cela vous permet de retrouver ces données plus facilement.

*Heuu…. Comment ça, “les retrouver plus facilement” ?*

Eh oui ! La mémoire d’un ordinateur est un peu comme une énorme armoire avec des milliers de tiroirs qui permettent de ranger les données que l’on stocke. Et comme il y a des milliers de tiroirs, nous identifions chacun d’entre eux grâce à une “étiquette”.

Pour identifier facilement le tiroir qui contient le nom d’un utilisateur, par exemple, nous lui attribuons l’étiquette _nomUtilisateur_. Ainsi, à chaque fois que nous voudrons consulter ou mettre à jour cette donnée, nous irons directement dans le tiroir _nomUtilisateur_. Ce conteneur de données est donc une **variable**. Et l’étiquette, c’est le **nom de la variable**. 

Chaque variable possède un **type**. Cela permet à l’ordinateur d’attribuer le “tiroir” le plus approprié à chaque donnée.

![Illustration d'une variable sous forme de tiroir. La valeur et le nom sont indiqués en bleu. Le type est indiqué de différentes couleurs selon leur nature (texte, chiffre...).](https://user.oc-static.com/upload/2023/05/09/16836417758704_STATIC-P1C2-1.png)

Il existe des  **types basiques** :
- number : la donnée est un chiffre ;
- string : la donnée est une chaîne de caractères (du texte, comme “David”, par exemple) ;
- boolean : la donnée est vraie ou fausse.

Il existe aussi d’autres types dit “complexes”, que nous verrons en détail dans les prochains chapitres.
Revenons à nos variables, et voyons comment écrire une variable en JavaScript. 😃

# Déclarez une variable en JavaScript

Lorsque vous déclarez une variable, c’est-à-dire lorsque vous la créez, vous devez utiliser une syntaxe précise qui permettra à votre programme informatique d’interpréter correctement votre code. Vous allez donc déclarer votre variable en utilisant **une instruction**.

Les instructions sont des mots-clés uniques qui permettent au code d’être correctement interprété. Pour déclarer des variables, vous utiliserez les instructions **let** et **const**.
## L’instruction let

Utilisons l’instruction _let_ suivie du nom de la variable :

```
let monAge = 42
```

Avec ce code, je viens de déclarer une variable _monAge_ qui possède la valeur 42.

Je peux faire évoluer cette valeur en écrivant :

```
monAge = 43
```

Notez que je n’ai pas réécrit l’instruction _let_. En effet, une fois la variable déclarée une première fois grâce à _let_, je peux l’utiliser directement.

Dans ce cours, nous avons fait le choix de ne pas mettre le caractère**`;`**pour indiquer la fin d’une ligne de code. Vous serez cependant amené à le retrouver dans certains extraits de code. Les deux écritures sont acceptées.

L’écriture _let monAge = 42;_ est donc tout à fait valide. L’idéal est de faire un choix au départ, et de rester cohérent tout au long d’un même projet.  
## L’instruction const

Utilisons l’instruction _const_ suivie du nom de la variable :

```
const monPrenom = "David"
```

Dans le code ci-dessus, j’ai déclaré une variable _monPrenom_ qui a comme valeur “David”.

*Mais c’est pareil que **let**, alors ?*

Eh bien non ! _const_ signifie “constante”. Donc, une fois déclaré, _monPrénom_ ne pourra plus changer. Si on essaie, JavaScript refusera d’exécuter l’instruction et affichera une erreur. En revanche, _monAge_, déclaré avec _let,_ pourra évoluer dans le code.

L’instruction _**var**_ peut également être utilisée pour déclarer une variable, mais elle est considérée comme obsolète. Pour autant, ne soyez pas surpris d’en trouver parfois dans le code d’autres développeurs, ou dans de vieux projets.
## L’instruction console.log()

Pour vérifier le contenu d’une variable, il est possible d’utiliser l’instruction _console.log()_, avec entre les parenthèses, le nom de la variable.

```
let monAge = 42
console.log(monAge)
```

Je vous propose de vérifier le résultat de cet extrait de code dans [CodePen](https://codepen.io/pen/), un éditeur de code en ligne :  

- copiez l’extrait de code dans la partie JS, puisque nous écrivons du code en JavaScript ;
- accédez à la console en cliquant sur l’onglet Console en bas de page. 

[![Capture d'écran de l'interface de CodePen. Elle affiche en haut un titre](https://user.oc-static.com/upload/2023/04/12/16812932541289_image17.png)](https://user.oc-static.com/upload/2023/04/12/16812932541289_image17.png)

Je vous encourage vivement à vous servir de console.log tout au long de ce cours. Cela vous permettra de vérifier les valeurs de n’importe quelle variable, et de vous assurer que notre code produit bien les résultats attendus.

# Codez proprement

Il n’est jamais trop tôt pour coder proprement, et cela commence dès que vous déclarez une variable ! Ainsi, il est très important de nommer correctement nos variables.

*Qu’est-ce que tu entends par “correctement” ?*

Concrètement : **donnez du sens** aux noms de vos variables, et décrivez précisément leur contenu.

Dans mon exemple, pour mon prénom j’ai nommé ma variable _monPrenom_. De cette façon, je m’assure que si un autre développeur lit mon code, il saura précisément ce que contient ma variable tout au long du code.

C’est également utile pour moi, lorsque je reviens sur du code écrit il y a longtemps, pour l’améliorer ou ajouter quelque chose. Avec des variables bien nommées, je suis sûr de retrouver le sens de ce qui a été codé. 😉

# En résumé

- Vous pouvez identifier une valeur en lui attribuant un nom grâce à une variable.
- Pour déclarer une variable en JavaScript, vous devez utiliser les instructions : 
    - _let_ si la valeur de la variable évolue dans le code ;
    - _const_ si la valeur de la variable est constante.
- Utilisez l’instruction _console.log(nomDeMaVariable)_ pour vérifier le contenu d’une variable.
- Le mot-clé _var_ ne doit plus être utilisé. Vous pourrez néanmoins le retrouver dans des codes plus anciens.
- Veillez à bien nommer vos variables : indiquez leur contenu de manière explicite pour rendre votre code lisible pour tout le monde. 

_Vous avez déclaré votre première variable : bravo ! 🥳 Suivez-moi dans le chapitre suivant pour savoir comment la modifier !_