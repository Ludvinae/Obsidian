[[Dev]]


### [[HTML]]
### [[Wordpress]]



Le front-end est défini par une liste de technologies : HTML, CSS et Javascript. 

De l’autre côté du spectre, le back-end comprends des technologies coté serveur telles que PHP et SQL. 

HTML

“HyperText Markup Langage”  

La structure du code HTML est déterminante pour le référencement naturel d’un site internet.  

Les outils d’assistance analysent le code source HTML afin de restituer une page en mode accessibilité. 

La structure se fait avec des balises.  

Une bonne pratique est de rafraichir une page avec control + F5 plutôt que d’utiliser simplement F5, afin de vider le cache en même temps que le rafraichissement. 

Bonnes pratiques en HTML 

Le titre du document dans le head du HTML ne devrait jamais être laissé avec l’option par défaut. Si plusieurs pages du même site utilisent le même titre, le référencement pourrait considérer une situation de “duplicate content”, et ne pas apparaitre dans les moteurs de recherche. 

La balise <h1> représente le titre de la page, le heading. Il est impératif que cette balise ne soit présente qu’une seule fois par page. Cette balise est différente du <title> de la page, qui apparait dans l’onglet du navigateur. Le titre et le Healing devraient être différents. 

Au contraire, les autres heading de plus bas niveau (<h2>...<h6>) ne devraient pas être unique. En effet ils sont utilisés pour subdiviser la page pour la structurer de façon logique. Subdiviser en une partie n’aurait aucun sens. 

Au sein de la balise paragraphe <p>, les balises <strong> et <em> sont importantes, utilisées pour mettre des mots-clés en valeur. Ces balises sont venues remplacées les balises <b> et <i>, qui sont maintenant obsolètes, car n’impactant que la mise en forme, ce qui est considéré comme étant le rôle du CSS, et non du HTML. 

Une liste est un exemple de balises qui requiert plus que simplement une balise ouvrante et une fermante.  En effet à l’intérieur de ces balises, on utilisera d’autres balises pour indiquer les items de la liste. Il faut rester attentif à utiliser le type de liste de manière cohérente.  Il faudra utiliser un ordered list <ol> uniquement si l’ordre a un sens pour cette liste. Sinon on utilisera une unordered list <ul>. 

Les liens 

On peut naviguer entre les pages grâce à la balise d’ancre 

<a href=”www.ggogle.com” target=”_blank”> texte </a> 

<a href=”test2.html#name”>blabla</a>  ->  va sur l’ancre name de la page test2 ( <div id=”name”>) 

Les tableaux 

On utilise une balise <table> pour définir le tableau, puis des balises <tr> pour les lignes (rows). A l’intérieur de chaque ligne, on doit mettre le même nombre de balises <td> (col). 

On peut annoter le tableau avec une légende grâce à la balise <caption>. On met toujours cette balise tout en haut au niveau du HTML, même si lors de la mise en page on le place en dessous. 

On peut mettre des titres aux lignes et aux colonnes avec la balise <th>. Si on veut utiliser ces headers à la fois pour les lignes et pour les colonnes, il faut préciser des attributs à l’intérieur de ces balises : scope = “row” ou scope = “col”. 

De plus on peut ajouter des en-têtes et des pieds de pages au tableau avec les balises <thead> et <tfoot> respectivement. Dans ce cas, il faudra mettre le corps du tableau a l’intérieur de la balise <tbody>. 

On peut fusionner les cases d’un tableau pour avoir un nombre de colonnes ou de lignes différentes, tout en maintenant sa cohérence. On utilise les attributs “colspan” et “rowspan” pour fusionner plusieurs cellules. Cela s’applique soit à l’intérieur d’une balise <td>, soit dans une balise <th>. On place l’attribut dans la première balise <td> dans le sens de la lecture (en haut à gauche), et on n’inclut pas la seconde cellule de la fusion. 

On peut aussi imbriquer un second tableau a l’intérieur d’une cellule d’un tableau. 

Les balises LandMark 

Certaines balises servent à délimiter certaines parties du contenu. Par exemple <main> <header> et <footer>. De plus on peut sectionner un contenu spécifique avec <nav> pour la navigation ou <section> pour différentes parties séparées (une section devrait avoir un titre et un contexte). Un menu de navigation cohérent doit être une liste non ordonnée de liens à l’intérieur d’une balise <nav>. Si on a besoin de sous-menus, on utilise donc une sous-liste, une liste imbriquée dans la première liste. 

Les images 

<img src=”path\image.jpg” alt=”description”> 

Une image utilise une balise orpheline, contenant toujours au moins un attribut source pour indiquer où trouver le fichier. Il faut aussi ajouter aussi un attribut de nom alternatif “alt” afin de pouvoir décrire le contenu d’une image. Pour faire simple, si une image contient du texte ou des informations qui ne sont pas redondantes. Si l’image est simplement décorative et ne véhicule pas d’informations, elle ne nécessite donc pas de description et on utilisera alt=””. 

