[[HTML]]


Le titre du document dans le head du HTML ne devrait jamais être laissé avec l’option par défaut. Si plusieurs pages du même site utilisent le même titre, le référencement pourrait considérer une situation de “duplicate content”, et ne pas apparaitre dans les moteurs de recherche. 

La balise <h1> représente le titre de la page, le heading. Il est impératif que cette balise ne soit présente qu’une seule fois par page. Cette balise est différente du <title> de la page, qui apparait dans l’onglet du navigateur. Le titre et le Healing devraient être différents. 

Au contraire, les autres heading de plus bas niveau (<h2>...<h6>) ne devraient pas être unique. En effet ils sont utilisés pour subdiviser la page pour la structurer de façon logique. Subdiviser en une partie n’aurait aucun sens. 

Au sein de la balise paragraphe <p>, les balises <strong> et <em> sont importantes, utilisées pour mettre des mots-clés en valeur. Ces balises sont venues remplacées les balises <b> et <i>, qui sont maintenant obsolètes, car n’impactant que la mise en forme, ce qui est considéré comme étant le rôle du CSS, et non du HTML. 

Une liste est un exemple de balises qui requiert plus que simplement une balise ouvrante et une fermante.  En effet à l’intérieur de ces balises, on utilisera d’autres balises pour indiquer les items de la liste. Il faut rester attentif à utiliser le type de liste de manière cohérente.  Il faudra utiliser un ordered list <ol> uniquement si l’ordre a un sens pour cette liste. Sinon on utilisera une unordered list <ul>. 