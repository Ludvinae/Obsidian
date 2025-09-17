[[Balises HTML]]

On utilise une balise <table> pour définir le tableau, puis des balises <tr> pour les lignes (rows). A l’intérieur de chaque ligne, on doit mettre le même nombre de balises <td> (col). 

On peut annoter le tableau avec une légende grâce à la balise <caption>. On met toujours cette balise tout en haut au niveau du HTML, même si lors de la mise en page on le place en dessous. 

On peut mettre des titres aux lignes et aux colonnes avec la balise <th>. Si on veut utiliser ces headers à la fois pour les lignes et pour les colonnes, il faut préciser des attributs à l’intérieur de ces balises : scope = “row” ou scope = “col”. 

De plus on peut ajouter des en-têtes et des pieds de pages au tableau avec les balises <thead> et <tfoot> respectivement. Dans ce cas, il faudra mettre le corps du tableau a l’intérieur de la balise <tbody>. 

On peut fusionner les cases d’un tableau pour avoir un nombre de colonnes ou de lignes différentes, tout en maintenant sa cohérence. On utilise les attributs “colspan” et “rowspan” pour fusionner plusieurs cellules. Cela s’applique soit à l’intérieur d’une balise <td>, soit dans une balise <th>. On place l’attribut dans la première balise <td> dans le sens de la lecture (en haut à gauche), et on n’inclut pas la seconde cellule de la fusion. 

On peut aussi imbriquer un second tableau a l’intérieur d’une cellule d’un tableau. 

[Exercice des drapeaux](https://www.formation.maxys.fr/cours/html/ressources/)
[[Flag.base]]
