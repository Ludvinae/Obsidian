[[Pseudo-code structuré]]

## Cheat Sheet — Pseudo-code structuré[](https://formations.nicolas.sh/algorithms/pseudo-code-cheatsheet?authuser=0#cheatsheet-pseudo)

Conventions, structures de contrôle, fonctions et exemples prêts à copier.

### Conventions[](https://formations.nicolas.sh/algorithms/pseudo-code-cheatsheet?authuser=0#conventions)

- **Commentaires** : `// this is a comment`
- **Affectation** : `x ← value` (flèche gauche)
- **Comparaison** : `=` `!=` `<` `<=` `>=`
- **Logique** : `AND` `OR` `NOT`
- **Nommage** : `snake_case` ou `camelCase`, verbes pour les actions
- **Indentation** : 2 espaces par niveau

|Catégorie|Opérateurs|
|---|---|
|Arithmétique|`+` `-` `*` `/` `DIV` `MOD`|
|Comparaison|`=` `!=` `<` `<=` `>=`|
|Logique|`AND` `OR` `NOT` `XOR`|

**Note sur les divisions**

Il existe 3 opérateurs de division :

- `/` : division entière (`7/2` = 3.5)
- `DIV` : division entière (retourne le quotient, `7 DIV 2` = 3)
- `MOD` : division entière (retourne le reste, `7 MOD 2` = 1)

### Entrées / Sorties & Variables[](https://formations.nicolas.sh/algorithms/pseudo-code-cheatsheet?authuser=0#io-variables)

```
ALGORITHM GreetUser
VARIABLES
  name: STRING
  age: INTEGER

CONSTANTS
  MAJORITY_AGE = 18

BEGIN
  // Input
  PRINT("Your name?")
  READ(name)

  PRINT("Your age?")
  READ(age)

  // Output
  PRINT("Hello ", name, "! You are ", age, " years old.")
  IF age >= MAJORITY_AGE
    PRINT("You are an adult.")
  ELSE
    PRINT("You are a minor.")
  END_IF
END
```

### Conditions[](https://formations.nicolas.sh/algorithms/pseudo-code-cheatsheet?authuser=0#conditions)

La boucle `IF` (`SI` en français) permet d'exécuter un bloc de code si une condition est vraie.

```
IF age < 18
  PRINT("Minor")
ELSE IF age < 65
  PRINT("Adult")
ELSE
  PRINT("Senior")
END_IF
```

Il est également possible de terminer la condition grâce au mot clé `THEN`

```
IF age < 18 THEN
  PRINT("Minor")
ELSE IF age < 65 THEN
  PRINT("Adult")
ELSE
  PRINT("Senior")
END_IF
```

Le mot clé `SWITCH` (`SELON` en français) permet de gérer plusieurs cas selon la valeur d'une variable. Ce mot clé permet notamment d'éviter une succession de `IF` imbriqués.

```
SWITCH day
  CASE "monday","tuesday","wednesday","thursday","friday":
    PRINT("Weekday")
  CASE "saturday","sunday":
    PRINT("Weekend")
  DEFAULT:
    PRINT("Unknown")
END_SWITCH
```

### Boucles[](https://formations.nicolas.sh/algorithms/pseudo-code-cheatsheet?authuser=0#boucles)

Les boucles permettent de répéter un bloc de code plusieurs fois.

La boucle `WHILE` (`TANT QUE` en français) s'exécute tant qu'une condition est vraie. La condition est vérifier **avant** l'exécution du bloc de code.

```
n ← 10
i ← 0
WHILE i < n
  PRINT(i)
  i ← i + 1
END_WHILE
```

La boucle `FOR` (`POUR` en français) s'exécute un nombre déterminé de fois. Elle est généralement utilisée lorsque le nombre d'itérations est connu à l'avance (par exemple, lors de l'itération sur un tableau de données).

```
FOR i IN RANGE(1, 10)
  sum ← sum + i
END_FOR

FOR j IN ["apple", "banana", "cherry"]
  PRINT(j)
END_FOR
```

La boucle `DO` (`FAIRE` en français) s'exécute au moins une fois, puis continue tant qu'une condition est vraie.

```
DO
  READ(x)
WHILE x = 0
```

La variante `REPEAT` (`RÉPÉTER` en français) s'exécute au moins une fois, puis continue tant que la condition est fausse.

```
REPEAT
  READ(x)
UNTIL x > 0
```

### Fonctions & Procédures[](https://formations.nicolas.sh/algorithms/pseudo-code-cheatsheet?authuser=0#fonctions)

Les **fonctions** sont des blocs de code réutilisables qui prennent des entrées, effectuent des opérations et renvoient une valeur. Les **procédures** sont similaires, mais ne renvoient pas de valeur.

```
FUNCTION isEven(n: INTEGER): BOOLEAN
  RETURN (n MOD 2 = 0)
END_FUNCTION

IF isEven(10)
  PRINT("Even")
ELSE
  PRINT("Odd")
END_IF
```

```
PROCEDURE swap(REF a: INT, REF b: INT)
  tmp ← a
  a   ← b
  b   ← tmp
END_PROCEDURE

// Utilisation
swap(x, y)
```

### Rappels & bonnes pratiques[](https://formations.nicolas.sh/algorithms/pseudo-code-cheatsheet?authuser=0#rappels)

- Une **instruction par ligne**, gardez des phrases courtes et claires.
- Préférez des **prédicats simples** ; décomposez les chaînes complexes de `AND`/`OR` (que vous pouvez extraire dans des fonctions par exemple).
- Complexités usuelles : `O(1)`, `O(log n)`, `O(n)`, `O(n log n)`, `O(n^2)`.
- Testez toujours les **cas limites** : vide, élément unique, doublons, bornes.