[[Python]]

- **Tableau** (ou liste)
- **Tuple**
- **Dictionnaire**
- **Set**

## Listes

On initialise un **tableau** (ou liste), un type de [[Structure de données]], avec des crochets []. On rajoute des éléments individuels a cette liste avec la méthode .append(). 
	liste = []
On accède aux éléments de la liste grâce à son index (liste[0] pour le premier élément, liste[-1] pour le dernier).
	liste[1:-1] pour afficher les valeurs entre le second index et l'avant-dernier.
	liste[:3] pour afficher les trois premières valeurs

Pour modifier une liste, on peut utiliser plusieurs méthodes:
- **liste.append(valeur)**: ajouter la valeur entre parenthèse a la fin de la liste
- **liste.insert(index, valeur)**: ajoute la valeur a la position d'index, en poussant les index des valeurs suivantes
- **liste.remove(valeur)**: enlève tous les éléments du tableau avec la valeur donnée
- **liste.pop(index)**: enlève l'élément a l'index donné, ou le dernier élément de la liste si pas précisé
- **liste.clear()** : vide la liste
- **liste.reverse()**: inverse tous les éléments de la liste
- **liste.sort()**: trie les éléments par ordre alphabétique (pour trier par ordre inverse, on ajoute "reverse=True")

Pour accéder a tous les éléments d'une liste, on utilise généralement un boucle For.


## Sets

Chaque élément dans un set est **unique**, et n'as pas de **position**. On utilise souvent les sets pour vérifier rapidement si un élément est présent dedans. 
	sac = {"element1", "element2"}

Quelques méthodes pour modifier un set:
- **`sac.add("element3")`** : ajouter l'élément au set si il n'existe pas déjà dedans.
- **`sac.remove("element")`** : enlève l'élément du set.

De plus, les sets ont des méthodes qui permettent facilement de comparer deux sets différents entre eux:
- **`set1.union(set2)`** : fusionne les deux sets sans créer de doublons
- **`set1.interection(set2)`** : retrouve les données présentes à la fois dans les deux sets
- **`set1.difference(set2)`** : retrouve les données de set1 qui ne sont pas présentes dans set2


## Dictionnaires

Chaque élément est associée a une clé pour pouvoir y accéder. On parle de **paires clé - valeurs**.
Les clés sont toujours uniques. On peut mélanger les types de données a l'intérieur des valeurs.

capitales = {"FR" : "Paris", "DE" : "Berlin"}

On peut par exemple accéder a la valeur "Paris" en tapant capitales["FR], et ajouter une paire avec capitales["ES"] = "Madrid". 
del capitales["FR"] va enlever la paire "FR" : "Paris"

Méthodes associées aux dictionnaires:
-  **capitales.keys()**: renvoie une liste de toutes les clés du dictionnaire du dictionnaire
- **capitales.values()**: renvoie une liste de toutes les valeurs du dictionnaire
- **capitales.items()**:  renvoie une liste de tuples des paires clé - valeur
- **capitales.get(key)**: renvoie la valeur associée a la clé


## Tuples

Arrange les données de manière ordonnée et immuable. On peut bouler dans une liste de tuples avec une boucle For. Dans ce cas, on associe chaque élément avec sa propre variable.

coord = (x, y)
