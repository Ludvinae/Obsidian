Dans le chapitre précédent, vous avez appris à reconnaître différents types de variables qui permettent d’identifier une valeur à la fois. Mais comment faire pour identifier un élément avec plusieurs valeurs ? C’est le moment d’utiliser les objets !

# Découvrez les objets en JavaScript

Un **Object** (objet, en français) JavaScript est un **conteneur**. Il est composé de **propriétés** qui ont chacune une valeur. Ainsi, le type de donnée **Object** offre la possibilité de stocker plusieurs valeurs en une seule fois, plutôt que de devoir stocker séparément nos valeurs dans plusieurs variables différentes.

# Déclarez un objet en JavaScript

Pour déclarer un objet en JavaScript, vous devez utiliser les accolades  `{ }`  . Les propriétés d’un objet ont un nom et une valeur qui sont assignées avec deux points`:` . Les propriétés sont séparées entre elles par des virgules`,`*.

> Par exemple, pour déclarer l’objet _monPersonnage_ qui représente le personnage fictif Bruce Wayne, 35 ans, dont la couleur préférée est le noir et qui adore sortir la nuit, vous écrirez :

```
let monPersonnage = {
nom: "Wayne",
prenom: "Bruce",
age: 35,
couleurPreferee: "noir",
hobbies: "sortir la nuit"
}
```
## Ajoutez une propriété à un objet JavaScript

Un objet JavaScript peut être mis à jour au fur et à mesure de son évolution dans le code.

> Par exemple, si vous vous rendez compte que l’objet _monPersonnage_ a désormais un véhicule préféré, il vous faudra lui ajouter cette nouvelle propriété.

Pour ajouter une propriété, vous devez écrire le nom de votre objet, séparé par un point  `.`  avec le nom de votre nouvelle propriété :

```
monPersonnage.vehiculePrefere = "Batmobile"
```
## Accédez à une propriété d’un objet JavaScript

Lorsque vous manipulez des objets JavaScript, vous avez également besoin d’accéder à leurs propriétés pour les stocker dans des variables, et les utiliser dans la suite de votre code ou dans un autre contexte.

Vous pouvez accéder à la valeur d’une propriété en utilisant le point  `.`  et par exemple, la stocker dans une variable.

> Dans le cadre de l’objet _monPersonnage_, vous écrirez :

```
const nomDeMonPersonnage = monPersonnage.nom
// Vérification
console.log(nomDeMonPersonnage)
console.log(monPersonnage.nom)
```

# À vous de jouer !

Et maintenant, entraînez-vous à manipuler des variables avec cet [exercice CodePen](https://codepen.io/nicolaspatschkowski/pen/JjBvGwW).

Vous êtes chargé de la maintenance d’une borne automatique qui permet de récupérer son billet de cinéma. Vous devez préparer la sortie du prochain film Batman, et faire en sorte que les utilisateurs puissent récupérer un billet pour ce nouveau film.
## Déclarez le nouveau ticket de cinéma

Un ticket de cinéma a plusieurs propriétés : un nom de film, un prix, un numéro de salle.

- Déclarez un objet _ticket_ avec les propriétés suivantes :
    - _nomFilm_ ;
    - _prix_ ;
    - _numeroSalle_.
- Déclarez une variable _nom_ avec votre nom. 
## Affichez les informations sur la borne

- Affichez un message sur la borne : “Bonjour NOM, votre film NOMDEFILM est en salle NUMERODELASALLE”.
- Créez une variable _texteAffichage_ qui contient cette phrase, avec NOM, NOMDEFILM et NUMERODELASALLE remplacés par leur vraie valeur.
- Vérifiez le résultat avec un _console.log_. 
## Corrigé

Vous pouvez vérifier votre travail en [consultant le corrigé](https://codepen.io/nicolaspatschkowski/pen/YzjLwMe?editors=1111) et la vidéo ci-dessous : 

# En résumé

- Un objet en JavaScript peut posséder plusieurs propriétés qui auront pour chacune d’elles une valeur.
- Pour déclarer un objet en JavaScript, vous devez utiliser les accolades  `{ }`  .
- Pour ajouter ou récupérer une propriété, vous devez utiliser le point  `.`  .

_Vous savez maintenant comment structurer des données grâce aux objets. Suivez-moi dans le chapitre suivant pour découvrir comment créer des tableaux._