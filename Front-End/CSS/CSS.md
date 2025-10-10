[[Front-End]]
[[DOM]]

On essaye généralement de positionner les sélecteurs CSS du plus générique au plus précis de haut en bas. On peut mettre des lignes de commentaires entre les grandes parties du CSS afin de visuellement organiser le fichier.

**inline**  -> prends seulement l'espace horizontal requis
**block** -> prends tout l'espace horizontal disponible

**Super propriété**: propriété qui regroupe plusieurs autres propriétés.

## Sélecteurs

Un **parent** est une balise qui précède la balise dans le DOM; lorsque l'on parle de la balise qui précède directement on parle de **parent direct**.
Les **siblings** sont les balises qui ont le même parent direct en commun;

- Sélectionner une balise qui a pour parent:
```
p strong {
color: red;
}
```

- Sélectionner une balise qui a pour parent direct:
```
p>strong {
color:red;
}
```

- Sélectionner les lignes paires: 
```
nav ul li:nth-child(even) {
background-colod: grey;
}
```
(on utilise `odd` pour les lignes impaires)

- Sélectionner le premier sibling qui suit une balise:
```
h2+p {
}
```

- Exclure un élément de la sélection:
```
p:not(.intro, h2+p)
```



