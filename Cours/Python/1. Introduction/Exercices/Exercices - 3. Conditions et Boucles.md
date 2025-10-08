# <span style="color:red;">Conditions & Boucles : Exercices (avec Tips)</span> 📘

---

## <span style="color:red;">Exercice 1 : Vérification de la Majorité</span> 🧩

1. Demandez à l’utilisateur d’entrer son âge.
2. S’il a **18 ans ou plus**, affichez un message indiquant qu’il est **majeur** ; sinon **mineur**.
3. Gérez les **entrées invalides** (vides, négatives, non numériques) en redemandant une valeur.
4. Variante : ajoutez une catégorie **“senior”** à partir de 65 ans.

**Exemples attendus :**
- Entrée : `17` → Sortie : `Mineur`
- Entrée : `18` → Sortie : `Majeur`
- Entrée : `-2` → Sortie : message d’erreur puis nouvelle demande

### 💡 Tips apprenants
- Vérifiez les entrées **avant** d’évaluer la condition (principe “valider puis traiter”).
- Pensez à l’ordre logique : d’abord **tests simples / probables**, ensuite les cas particuliers.
- Utilisez des **messages explicites** pour guider l’utilisateur en cas d’erreur.

---

## <span style="color:red;">Exercice 2 : Table de Multiplication</span> 🧩

1. Demandez un **entier** à l’utilisateur.
2. Affichez sa **table de multiplication** de `1` à `10` avec une **boucle for**.
3. Formatage lisible (alignement, symbole `x`, signe `=`).
4. Variante : proposez de choisir la **borne supérieure** (ex. jusqu’à `n`).

**Exemples attendus :**
- Entrée : `3` → Sortie : lignes de `3 x 1 = 3` à `3 x 10 = 30`.

### 💡 Tips apprenants
- `range(1, 11)` produit 1→10 (la borne haute est **exclusive**).
- Soignez l’**affichage** : un résultat lisible aide à déboguer.
- Testez avec des **valeurs négatives** et `0` pour observer le comportement.

---

## <span style="color:red;">Exercice 3 : Somme des Nombres Premiers</span> 🧩

1. Demandez un entier **n ≥ 0**.
2. Calculez la **somme** de tous les nombres **premiers** de `2` à `n`.
3. Affichez le résultat final.
4. Variante : affichez aussi la **liste** des nombres premiers trouvés.

**Exemples attendus :**
- Entrée : `10` → Nombres premiers : `2, 3, 5, 7` → Somme : `17`.

### 💡 Tips apprenants
- Un nombre `< 2` **n’est pas** premier.
- Optimisez le test de primalité jusqu’à `√n` pour éviter des boucles inutiles.
- Commencez simple (tests naïfs), puis **améliorez** (optimisation progressive).

---

## <span style="color:red;">Exercice 4 : Affichage des Caractères</span> 🧩

1. Demandez une **chaîne de caractères** à l’utilisateur.
2. Affichez **chaque caractère** accompagné de son **index** (position) avec une boucle.
3. Variante : indiquez si le caractère est un **espace**, une **lettre**, un **chiffre** ou un **symbole**.

**Exemples attendus :**
- Entrée : `Hi!`  
  Sortie :
  - `Index 0 : H`
  - `Index 1 : i`
  - `Index 2 : !`

### 💡 Tips apprenants
- Parcourez une chaîne **comme une liste** : un caractère à la fois.
- Pensez aux **chaînes vides** et aux **espaces** (ils comptent !).
- Catégoriser les caractères vous fait pratiquer les **conditions multiples**.

---

## <span style="color:red;">Exercice 5 : Calcul de la Moyenne</span> 🧩

1. Demandez une série de **nombres** séparés par des **espaces**.
2. Convertissez-les en **liste numérique**.
3. Calculez et affichez la **moyenne** (somme / quantité).
4. Gérez le cas **liste vide** (aucun nombre saisi).
5. Variante : acceptez les **virgules** comme séparateur décimal.

**Exemples d’I/O attendus :**
- Entrée : `10 20 30` → Sortie : `Moyenne = 20.0`

### 💡 Tips apprenants
- Séparez les responsabilités : **lire**, **valider**, **convertir**, **calculer**, **afficher**.
- Gérez les **erreurs de conversion** proprement (ne plantez pas !).
- Cas limite : une seule valeur, ou valeurs négatives / décimales.

---

## <span style="color:lime;">Bonus (Optionnels)</span> 🧪

- **B1 — Deviner le nombre :**  
  Générez un nombre secret. L’utilisateur propose des valeurs jusqu’à trouver la bonne.  
  Indiquez “plus grand/plus petit”. **Limitez** le nombre d’essais → utilisez `while`, `break`.

- **B2 — Filtre pair/impair :**  
  Demandez une série d’entiers. Affichez séparément les **pairs** et **impairs**.  
  **Ignorez** les entrées invalides avec `continue`.

- **B3 — Recherche dans une liste :**  
  Donnez une liste de mots. Demandez un mot à chercher.  
  Parcourez avec `for` ; si trouvé, affichez l’index et utilisez `break`.  
  Si non trouvé, utilisez le `else` de boucle pour afficher “introuvable”.

---

## 🎓 Tips transversaux

- **Validez d’abord, traitez ensuite** : évitez de faire des calculs sur des entrées douteuses.  
- **Cas limites avant cas normaux** : zéro, vide, extrêmes, négatifs.  
- **Indentation stricte (4 espaces)** : c’est la structure de votre programme.  
- **Messages utiles** : pensez à l’utilisateur final, expliquez quoi saisir et pourquoi ça échoue.  
- **Itérez par versions** : version simple qui marche → puis ajoutez variantes et contrôles.

---
