[[JavaScript]]

Au lieu d’utiliser l’attribut `onclick` dans le HTML, il est recommandé d’utiliser `addEventListener`.
- Le premier paramètre est le **type d’événement** (`click`, `input`, `mouseover`…).
- Le second paramètre est la **fonction** à exécuter.

Types d'évenements:
- `click`|Clic sur un élément|
- `dblclick`|Double clic|
- `input`|Saisie dans un champ input|
- `change`|Modification d’un champ input ou select|
- `mouseover`|Souris sur un élément|
- `mouseout`|Souris quittant un élément|
- `keydown`|Touche du clavier pressée|
- `keyup`|Touche du clavier relâchée|
- `submit`|Formulaire soumis|

Délégation:
Les événements peuvent être **propagés** vers les éléments parents et gérés via la **délégation** d'un parent commun