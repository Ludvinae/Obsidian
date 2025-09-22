Vous savez désormais déclarer différents types de variables. En tant que développeur, vous aurez aussi souvent besoin de stocker plusieurs données dans des listes. Pour cela, l’option la plus simple est d’utiliser des tableaux.

# Découvrez les tableaux en JavaScript

Si vous manipulez des données similaires ou qui partagent la même thématique, il est préférable de les regrouper dans un tableau, plutôt que de les stocker individuellement dans des variables différentes. Cela vous permet de les retrouver en un seul endroit, et de limiter le nombre de variables dans votre code.

Un **tableau** en JavaScript est donc un objet qui permet de lister plusieurs variables ou valeurs, et de les regrouper.

# Déclarez un tableau en JavaScript

Pour déclarer un tableau en JavaScript, vous devez utiliser les crochets  `[ ]`  . Chaque valeur contenue dans le tableau est séparée par une virgule  `,`  :

```
const maCollectionDeFilms = ["Titanic", "Jurassic Park", "Le Seigneur des Anneaux"]
```

Vous pouvez également stocker des variables dans votre tableau :

```
const monFilmPrefere = "Titanic"
const monPremierFilm = "Le Seigneur des Anneaux"
const maCollectionDeFilms = [monFilmPrefere, monPremierFilm]
// maCollectionDeFilms vaut ["Titanic", "Le Seigneur des Anneaux"]
```
## Accédez à un élément de votre tableau

Pour accéder à un élément de votre tableau, vous devez utiliser les crochets, et mettre entre crochets le numéro de la case que vous voulez regarder. **La première case du tableau** correspond à la **case numéro zéro**.

> Pour accéder au contenu de cette case, vous écrirez donc :

```
let premierFilmDuTableau = maCollectionDeFilms[0]
```
## Comptez le nombre d’éléments de votre tableau

Pour connaître le nombre d’éléments que contient votre tableau, vous devez accéder à la propriété **length**, en utilisant le point  `.`  , comme pour les objets. Cette propriété est préétablie par JavaScript. Elle est donc automatiquement disponible pour tous les tableaux. Pratique !

> Imaginons que vous vouliez connaître le nombre total de films que vous possédez dans votre collection. Vous écrirez  :

```
const maCollectionDeFilms = ["Titanic", "Le Seigneur des Anneaux"]
const nombreDeFilms = maCollectionDeFilms.length
console.log(nombreDeFilms)
// nombreDeFilms vaut 2
```
## Modifiez votre tableau grâce aux méthodes

Les tableaux sont des **conteneurs**, comme les objets que nous avons vus dans le chapitre précédent. Pour effectuer des actions sur les données stockées dans votre tableau (ajouter, supprimer des données…), vous utiliserez des **méthodes**.

Les **méthodes** s’utilisent avec des parenthèses  `( )`  . À l’intérieur de ces parenthèses vous pouvez passer des valeurs, c'est-à-dire des données, qui serviront à la méthode pour modifier les données de votre tableau. En réalité, vous avez déjà utilisé une méthode fournie par JavaScript : _console.log()_ ! 
### Ajoutez des données grâce à la méthode push

Pour ajouter des données à un tableau, vous devez utiliser la méthode **push** en lui indiquant la valeur que vous souhaitez ajouter.

> Si vous voulez ajouter _Retour vers le futur_ à votre liste de films, vous écrirez :

```
let mesFilms = ["Titanic", "Jurassic Park"]
mesFilms.push("Retour vers le futur")
console.log(mesFilms)
// mesFilms vaut ["Titanic", "Jurassic Park", "Retour vers le Futur"]
```

Avec la méthode push, la donnée qui est entre les parenthèses (ici “Retour vers le futur”) sera ajoutée en dernier dans votre tableau.
### Supprimez des données grâce à la méthode pop

Pour supprimer la dernière donnée de votre tableau, vous pouvez utiliser la méthode **pop** sans avoir besoin de passer de valeurs (c'est-à-dire, sans rien écrire entre les parenthèses).

> Si vous voulez retirer _Retour vers le futur_ de votre liste de films, vous écrirez :

```
let mesFilms = ["Titanic", "Jurassic Park", "Retour vers le futur"]
mesFilms.pop()
// mesFilms vaut ["Titanic", "Jurassic Park"]
```

Sachez qu’il existe beaucoup d’autres méthodes pour manipuler les données d’un tableau, comme la méthode splice pour supprimer une donnée précise, ou la méthode sort pour trier les données. Pour en savoir plus, il y a toujours [la documentation](https://developer.mozilla.org/fr/docs/Learn/JavaScript/First_steps/Arrays) !

# Distinguez les copies par “valeur” et par “référence”

## La copie par valeur

Lorsqu’on programme, il arrive parfois que l’on veuille dupliquer une variable. C’est le cas lorsque l’on doit sauvegarder une valeur avant de la modifier, par exemple. Pour cela, le plus simple est de **copier le contenu d’une variable à l’intérieur d’une autre variable**.

Mais que se passe-t-il en réalité lorsque nous effectuons cette opération ?

```
// Copie par valeur
let variableSimple1 = 25
let variableSimple2 = variableSimple1
```

Eh bien, cela va dépendre du type de la variable. Si _variable2_ est un type simple (boolean, number ou string), alors le contenu sera **dupliqué**.

Souvenez-vous, dans le [deuxième chapitre du cours](http://xxxx), je vous expliquais que, lorsqu’on crée une variable, on lui attribue une étiquette. Pour reprendre notre métaphore de l’armoire, ce qui est dans le tiroir _variable1_ va être dupliqué, et la copie sera mise dans _variable2_. Au final, nous aurons **deux tiroirs indépendants** **avec chacun une valeur** à l’intérieur.

C’est ce qu’on appelle la **copie par** **valeur**. Nous avons copié le contenu d’une variable à l’intérieur d’une autre variable. Nous avons donc deux variables indépendantes.
## La copie par référence

Imaginez maintenant que vous vouliez copier une variable qui contient un contenu de type “complexe” :  un objet ou un tableau, par exemple. Dans ce cas, JavaScript fait une **copie par** **référence**.

```
let variableComplexe1 = ['pomme', 'cerise']
let variableComplexe2 = variableComplexe1
```

Ici, nous n’avons pas deux tiroirs, c’est l’étiquette qui a été copiée. En d’autre termes, _variable1_ et _variable2_ sont deux étiquettes différentes pour le même tiroir. Nous avons donc deux variables qui pointent sur le même contenu.

*Oui mais concrètement, quelle est la différence ?*

Dans le cas d’une copie par valeur, si vous modifiez la valeur d’une des deux variables, la valeur de l’autre ne change pas. Dans le cas d’une copie par référence, si vous changez la valeur de la première variable, la valeur de la seconde est affectée aussi.

*Et si je veux vraiment dupliquer mon tableau, alors ?*

Dans ce cas, vous devez déclarer un nouveau tableau et recopier toutes les valeurs une par une.

*Ahh !!!! Mais ça va prendre des heures ! 😱*

Eh bien non, car JavaScript a pensé à tout ! 😃 Vous n’aurez donc qu’à utiliser un **spread operator**. Comme le  `++`  que nous avons déjà croisé, c’est un opérateur qui nous permet de faire automatiquement la copie, et cet opérateur s’écrit`…`

```
let variableComplexe3 = [...variableComplexe1];
```

Ici, je dis que dans _variableComplexe3_, je recopie un par un tous les éléments qui sont dans _variableComplexe1_. Comme ces variables sont de type simple, nous avons une vraie copie, et les deux tableaux sont indépendants !

> Voici un exemple pour illustrer tout ça :

```
////////////////////
// Copie par valeur
////////////////////
let variableSimple1 = 25
let variableSimple2 = variableSimple1

variableSimple2 = 30

// Le console.log va afficher 25, le fait d’avoir changé la valeur de variableSimple2 ne change rien pour variableSimple1
console.log("variableSimple1", variableSimple1)
console.log("variableSimple2", variableSimple2)

///////////////////////
// Copie par référence
///////////////////////
let variableComplexe1 = ['pomme', 'cerise']
let variableComplexe2 = variableComplexe1
let variableComplexe3 = [...variableComplexe1];

variableComplexe2.push('poire')

// Le console.log va afficher pomme cerise ET poire. On a modifié la seconde variable, mais le contenu de la première a été changé aussi, parce que c’est le même contenu.
console.log('variableComplexe1', variableComplexe1)
console.log('variableComplexe2', variableComplexe2)
console.log('variableComplexe3', variableComplexe3)
```

C’est également pour cette raison que les tableaux sont souvent déclarés avec _const_ en JavaScript, même s'ils évoluent tout au long du code. Ce qui est constant, ce n’est pas le contenu, mais l’**endroit en mémoire où est stocké le tableau**. 

# À vous de jouer !

Et maintenant, entraînez-vous à manipuler des tableaux avec cet [exercice CodePen](https://codepen.io/nicolaspatschkowski/pen/eYjrLOb).

Vous organisez une soirée avec des amis. Une bonne soirée, c’est souvent une bonne musique ! Mais pour cela, vous devez vous organiser.
## Déclarez les morceaux de votre playlist

Commençons par faire un inventaire des CD en votre possession.

1. Déclarez un tableau playlist qui contiendra trois de vos morceaux préférés.
2. Stockez le nombre de morceaux disponibles dans une variable _totalMorceaux_.
## Ajoutez les morceaux de vos amis

Pour plaire à tout le monde, vous décidez de laisser vos amis choisir deux morceaux supplémentaires pour compléter votre collection.

- Ajoutez deux morceaux au tableau playlist de manière à porter le total à cinq morceaux.
## Enlevez le dernier morceau de votre playlist

Malheureusement, certains ne sont pas d’accord avec le dernier morceau ajouté. Il va falloir faire du tri ! 😱

- Supprimez le dernier morceau ajouté à votre collection.
## Corrigé

Vous pouvez vérifier votre travail en [consultant le corrigé](https://codepen.io/nicolaspatschkowski/pen/GRBdXgW?editors=0010) et la vidéo ci-dessous : 

# En résumé

- Un tableau est un conteneur qui permet de regrouper plusieurs valeurs ou variables.
- Un tableau possède une propriété length qui permet de connaître le nombre de données contenues dans un tableau.
- Une méthode s’utilise avec des parenthèses  `( )`  , et permet d’interagir avec le contenu du tableau. Il existe de nombreuses méthodes différentes mises à disposition par le langage.
- Lorsqu’on copie une variable simple, JavaScript réalise une copie par valeur (la valeur est dupliquée).
- Lorsqu’on copie une variable complexe, JavaScript réalise une copie par référence (les deux variables pointent sur la même valeur).

_Et voilà, vous venez de faire vos premiers pas en JavaScript. Vous savez désormais manipuler des données, toutes mes félicitations ! 🥳_

_Dans la prochaine partie du cours, nous rentrerons dans la logique de programmation en rédigeant notre premier fichier JavaScript. Mais avant, je vous propose de tester vos connaissances grâce au quiz._