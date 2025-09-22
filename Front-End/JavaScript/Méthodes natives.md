---
tags:
  - callback
---

[[JavaScript]]

#### forEach()

On peut utiliser cette méthode pour itérer sur une liste avec un callback de façon condensée. La fonction va automatiquement produire les éléments de la liste, les index et la liste à la fonction que l'on *callback*.

```
let liste = [1, 2, 3, 4, 5]

liste.forEach(double)

function double(element, index, array) {
array[index] = element * 2
}
```

