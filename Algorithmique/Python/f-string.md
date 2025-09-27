[[Python]]

f-strings allow to format a string in a convenient way:

```
print(f"Du texte et {une variable}")
```

Il y'a aussi des moyens de formater le string différement:

- **`{variable:_}`**: affiche un *entier* avec des séparateurs pour rendre les grands nombre plus lisibles (on peut aussi remplacer *_* par *,*)
- **`{variable:.2f}`** : affiche un *float* avec deux chiffres après la virgule (arrondis au plus proche)
- **`{variable:^20}`** : affiche la variable centrée sur un espace de 20 caractères. On peut aussi utiliser *>* pour aligner à droite et *<* pour aligner a gauche (on peut ajouter un caractère avant la flèche pour remplacer les espaces par ce caractère)
- **`{variable:%d.%m.%y}`** : affiche une *date* avec l'ordre choisi. Ca marche aussi pour les heures avec %H, %M et %S (on peut utiliser le format local avec **%c**)
- **`{a + b = }`** : ajouter le signe égal lorsqu'on effectue une opération permet d'afficher l'opération elle-même en plus du résultat