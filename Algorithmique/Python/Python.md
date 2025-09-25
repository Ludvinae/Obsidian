[[Algorithme]]

5 types de données primitives en Python
- String (**str**)
- Integer (**int**)
- Float (**float**)
- Boolean (*bool*)
- None

On peut afficher du texte dans le terminal avec la commande **print**. On peut soit concaténer les éléments a l'intérieur du print a l'aide de **+**, soit utiliser un **f-string** et dans ce cas on met les noms de variables entre curly bracket {}.
	print("blabla" + var)
	print(f"blabla {var}")

Fonctions:
On peut définir une valeur par défaut a un paramètre en la précisant dans sa définition. Ce paramètre deviens doncoptionnel.

```
def welcome(nom, age=10)
	print(f"Bonjour {nom}, tu as {age} ans)
welcome(Alice, 70) => "Bonjour Alice, tu as 70 ans"
welcome(Paul) => "Bonjour Paul, tu as 10 ans"
```



