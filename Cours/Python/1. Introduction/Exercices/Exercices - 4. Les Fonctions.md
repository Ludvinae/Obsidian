# <span style="color:red;">Les Fonctions en python : Exercices</span> 📘

---

## <span style="color:red;">Exercices n°1 — Définir & Appeler une fonction</span> 📞
**Objectif :** Savoir créer une fonction simple avec docstring et la rappeler plusieurs fois.  
**Consignes :**
1. Écrivez une fonction `aire_rectangle(longueur, largeur)` qui **retourne** l’aire d’un rectangle.  
2. Ajoutez une **docstring** qui explique brièvement le rôle de la fonction, ses paramètres et sa valeur de retour.  
3. Appelez la fonction avec au moins **trois** jeux de valeurs différents et affichez les résultats.  
4. Vérifiez que la fonction **retourne** bien une valeur (ne pas utiliser `print` à l’intérieur pour l’aire).

---

## <span style="color:red;">Exercices n°2 — Paramètres & Arguments (positionnels / mots-clés)</span> 🧩
**Objectif :** Maîtriser les appels avec **arguments positionnels** et **mots-clés**.  
**Consignes :**
1. Créez une fonction `presenter(nom, age)` qui **affiche** une présentation du type :  
   _"Je m'appelle {nom} et j'ai {age} ans."_
2. Faites **deux appels** :
   - un avec **arguments positionnels** (dans l’ordre des paramètres) ;
   - un avec **arguments mots-clés** (ordre inversé).
3. Ajoutez une variante `presenter(nom, age, ville="Paris")` avec une **valeur par défaut** pour `ville`, et montrez **deux appels** :  
   - un en utilisant la valeur par défaut ;  
   - un en fournissant une autre ville.

---

## <span style="color:red;">Exercices n°3 — Fonctions avec et sans `return`</span> 🗣️
**Objectif :** Distinguer une fonction qui **retourne** une valeur d’une fonction qui **affiche** quelque chose.  
**Consignes :**
1. Écrivez `saluer(nom="monde")` qui **affiche** : _"Bonjour, {nom} !"_.  
2. Écrivez `phrase_bienvenue(nom)` qui **retourne** (et ne l’affiche pas) la chaîne : _"Bienvenue, {nom}."_  
3. Montrez dans votre script la différence d’usage :  
   - appelez `saluer()` et constatez qu’elle **n’a pas de valeur de retour** utile ;  
   - appelez `phrase_bienvenue("Nina")`, **stockez** le résultat dans une variable et **affichez** ensuite cette variable.

---

## <span style="color:red;">Exercices n°4 — Valeurs par défaut & conception de signature</span> 🧱
**Objectif :** Concevoir une signature de fonction claire avec des **paramètres optionnels**.  
**Consignes :**
1. Écrivez `prix_total(prix_unitaire, quantite=1, remise=0)` qui **retourne** le total à payer selon la formule :  
   `total = prix_unitaire * quantite * (1 - remise)`  
   où `remise` est un taux entre `0` et `1` (ex. `0.2` pour 20%).  
2. Ajoutez une **docstring** précisant les unités attendues et la signification de `remise`.  
3. Montrez **quatre appels** :
   - seulement avec `prix_unitaire` ;
   - avec `prix_unitaire` et `quantite` ;
   - avec `prix_unitaire` et `remise` en **mot-clé** ;
   - avec les trois paramètres, dont au moins un en **mot-clé**.  
4. Affichez chaque résultat et **commentez** en une ligne le cas d’usage (ex. “achat en quantité avec remise”).

---

## <span style="color:red;">Exercices n°5 — Portée (scope) : variable locale vs globale</span> 🔍
**Objectif :** Comprendre la différence entre **variable locale** et **globale**.  
**Consignes :**
1. Créez une variable **globale** `message = "global"`.  
2. Écrivez une fonction `demo_portee()` qui définit une **variable locale** `message = "local"` et l’affiche.  
3. Appelez `demo_portee()` puis affichez la variable `message` **en dehors** de la fonction.  
4. Expliquez en **1–2 phrases** dans un commentaire ce que vous observez et pourquoi.  
5. (Optionnel) Créez une seconde fonction qui **lit** la variable globale **sans** la modifier, et montrez la différence si vous essayez de l’**assigner** à l’intérieur.

---

## <span style="color:red;">Exercices n°6 — Refactorisation : éviter la répétition</span> 🔁
**Objectif :** Extraire une logique répétée dans une **fonction réutilisable**.  
**Consignes :**
1. Imaginez que vous deviez afficher des tickets de caisse pour **trois** achats différents (prix unitaire, quantité, remise éventuelle).  
2. Sans fonction : écrivez le code naïf pour les trois affichages (quelques lignes par ticket).  
3. **Refactorez** : écrivez une fonction `afficher_ticket(produit, prix_unitaire, quantite=1, remise=0)` qui s’occupe de l’**affichage formaté** (libellé, quantités, sous-total, remise, total).  
4. Remplacez votre code naïf par **trois appels** à cette fonction.  
5. Ajoutez une **docstring** décrivant le format produit et ce que la fonction **affiche** (elle ne retourne pas de valeur).

---

## <span style="color:red;">Exercices n°7 — Spécification claire via docstring</span> 📚
**Objectif :** Apprendre à **documenter** une fonction simplement et utilement.  
**Consignes :**
1. Écrivez une fonction `est_majeur(age)` qui **retourne** `True` si `age >= 18`, sinon `False`.  
2. Rédigez une **docstring** de 2–4 lignes précisant :
   - le **but** de la fonction ;
   - le **type** et la **valeur attendue** du paramètre ;
   - la **valeur de retour** (type et signification) ;
   - **un court exemple** d’appel.  
3. Ajoutez **trois tests** d’appel et affichez les résultats.

---

## <span style="color:red;">Exercices n°8 — Séparation I/O et logique</span> 🧪
**Objectif :** Séparer la **logique de calcul** de l’**interaction utilisateur**.  
**Consignes :**
1. Écrivez une fonction `moyenne(a, b, c)` qui **retourne** la moyenne de trois nombres (ne fait **aucun** `input`/`print`).  
2. Dans le **corps principal** de votre script, demandez trois valeurs à l’utilisateur (avec `input`), **convertissez**-les, puis **appelez** `moyenne`.  
3. Affichez le résultat **formaté** proprement (arrondi si besoin).  
4. (Optionnel) Ajoutez des **vérifications** simples (entrées vides, non numériques) **en dehors** de la fonction `moyenne`.

---

### ✅ Recommandations générales
- Donnez à vos fonctions des **noms explicites** (verbe + complément).  
- Une fonction = **une responsabilité** claire.  
- Préférez **retourner** des valeurs (calcul) et gérer l’**affichage** hors de la fonction quand c’est pertinent.  
- Rédigez une **docstring courte** (but, paramètres, retour) pour les fonctions non triviales.  
- Testez vos fonctions avec **plusieurs cas** (valeurs normales, limites, inattendues).
