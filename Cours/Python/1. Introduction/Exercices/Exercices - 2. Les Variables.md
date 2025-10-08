# <span style="color:red;">Les Variables en Python : Exercices avec Astuces</span> 📘

---

## <span style="color:red;">Exercice 1 : Opérations Mathématiques</span> 🧩

1. Créez deux variables numériques.  
2. Calculez leur somme, différence, produit et quotient.  
3. Affichez les résultats de chaque opération.

---

### 💡 **Tips pour les apprenants :**
- 🔢 **Choisissez des valeurs simples** au début (par exemple `x = 10` et `y = 2`) pour bien comprendre le fonctionnement des opérations.  
- ⚙️ Vous pouvez tester vos calculs dans un **interpréteur Python interactif** (par exemple dans *Thonny*, *VS Code* ou directement dans le terminal avec `python`).  
- 🧠 **Retenez les opérateurs essentiels :**
  - `+` → addition  
  - `-` → soustraction  
  - `*` → multiplication  
  - `/` → division (résultat décimal)  
  - `//` → division entière (résultat sans décimale)  
  - `%` → reste d’une division  
- 🧾 **Bon réflexe :** affichez toujours vos résultats avec des phrases claires (ex. : `"La somme est :",somme`) pour faciliter la lecture du programme.

---

## <span style="color:red;">Exercice 2 : Concaténation de Chaînes</span> 🧩

1. Créez deux variables contenant un prénom et un nom.  
2. Concaténez-les pour afficher le nom complet d’une personne.

---

### 💡 **Tips pour les apprenants :**
- ✍️ En programmation, **la concaténation** signifie “mettre bout à bout” des chaînes de caractères.  
- 🔡 Pour ajouter un espace entre le prénom et le nom, **pensez à inclure `" "`** (un espace entre guillemets) lors de la concaténation.  
- ⚠️ Si vous oubliez l’espace, le résultat sera collé (ex. : `"JohnDoe"` au lieu de `"John Doe"`).  
- 🧩 Python offre plusieurs façons d’assembler du texte :
  - Avec `+` : `prenom + " " + nom`
  - Avec une **f-string** : `f"{prenom} {nom}"` → plus lisible et plus moderne.  
- 💬 Vous pouvez aussi personnaliser le message :  
  `print("Bonjour,", prenom, nom)` → Python ajoute automatiquement un espace entre les éléments.

---

## <span style="color:red;">Exercice 3 : Vérification de la Majorité</span> 🧩

1. Créez une variable contenant un âge.  
2. Affichez un message indiquant si la personne est majeure ou mineure selon la valeur.

---

### 💡 **Tips pour les apprenants :**
- ⚖️ **Les conditions** permettent à votre programme de “prendre des décisions”.  
  Python lit le test logique (`if`, `else`) et choisit le bloc de code à exécuter.  
- 🧠 **Rappel de syntaxe :**
  - `if condition:` → si la condition est vraie  
  - `else:` → sinon  
- ⚙️ L’indentation (les **espaces au début de la ligne**) est obligatoire après un `if` ou un `else`.  
  Sans cela, Python affichera une erreur `IndentationError`.  
- 👀 Testez votre code avec plusieurs valeurs (ex. `age = 17`, `age = 18`, `age = 25`) pour bien comprendre le comportement.  
- 🧩 Bonus : essayez une **version courte** du test, appelée *opérateur ternaire* :  
  ```python
  print("Majeur" if age >= 18 else "Mineur")
  ```
  C’est une manière rapide d’écrire une condition simple sur une seule ligne.

---

## <span style="color:lime;">Conseils Généraux pour Bien Débuter avec les Variables</span> 🌱

1. 🏷️ **Nommez vos variables clairement.**  
   Évitez les noms vagues comme `a`, `b`, `t`. Préférez `age`, `prix_total`, `nom_utilisateur`...  

2. 🧩 **Un type = un usage.**  
   Gardez une variable pour un type de donnée précis : évitez de transformer une variable nombre en texte sans raison.  

3. 💬 **Commentez votre code.**  
   Ajoutez des commentaires (`# ...`) pour expliquer vos choix ou étapes — c’est une excellente habitude.  

4. 🧠 **Expérimentez !**  
   Changez les valeurs, les opérateurs, testez différents scénarios. L’apprentissage passe par la pratique et l’erreur.  

5. 🚫 **Pas de copier-coller aveugle.**  
   Tapez le code à la main au moins une fois : cela renforce la mémoire et aide à repérer les erreurs de syntaxe.

---

## <span style="color:lime;">🎯 Objectif Pédagogique</span>

Ces exercices visent à :
- Assimiler la notion de **variable** et d’**affectation**.  
- Découvrir les **opérations de base** (mathématiques et textuelles).  
- Comprendre l’utilisation d’**une condition simple (`if / else`)**.  
- Commencer à adopter de **bonnes pratiques de lisibilité et de test de code**.
