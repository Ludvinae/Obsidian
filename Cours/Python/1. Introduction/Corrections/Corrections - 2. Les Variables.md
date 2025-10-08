# <span style="color:red;">Les Variables en Python : Correction Exercices</span> 📘

---

## <span style="color:red;">Exercice 1 : Correction — Opérations Mathématiques</span> 🧮

**Objectif :** Manipuler des variables numériques et réaliser des opérations arithmétiques de base.  

```python
# Déclaration des variables
x = 12
y = 4

# Opérations mathématiques
somme = x + y
difference = x - y
produit = x * y
quotient = x / y

# Affichage des résultats
print("Somme :", somme)
print("Différence :", difference)
print("Produit :", produit)
print("Quotient :", quotient)
```

🧠 **Explications :**
- `x` et `y` sont des **variables numériques**.  
- Les opérations `+`, `-`, `*`, `/` permettent respectivement d’additionner, soustraire, multiplier et diviser.  
- Le résultat est stocké dans de nouvelles variables (`somme`, `difference`, etc.), puis affiché à l’écran.  

💡 **Astuce :**  
Vous pouvez aussi utiliser `//` pour une division entière et `%` pour obtenir le reste d’une division.

---

## <span style="color:red;">Exercice 2 : Correction — Concaténation de Chaînes</span> ✍️

**Objectif :** Créer et combiner des variables de type chaîne de caractères.  

```python
# Déclaration des variables
prenom = "Emma"
nom = "Durand"

# Concaténation des chaînes
nom_complet = prenom + " " + nom

# Affichage du résultat
print("Nom complet :", nom_complet)
```

🧠 **Explications :**
- Les variables `prenom` et `nom` contiennent du texte (*strings*).  
- L’opérateur `+` permet de les **assembler (concaténer)**.  
- `" "` (un espace entre guillemets) est ajouté entre les deux pour séparer le prénom et le nom.  

💡 **Astuce :**  
On peut aussi utiliser une **f-string** (plus moderne et lisible) :
```python
nom_complet = f"{prenom} {nom}"
```

---

## <span style="color:red;">Exercice 3 : Correction — Vérification de la Majorité</span> 🎂

**Objectif :** Utiliser une condition (`if / else`) pour tester la valeur d’une variable.  

```python
# Déclaration de la variable
age = 17

# Vérification de la majorité
if age >= 18:
    print("La personne est majeure.")
else:
    print("La personne est mineure.")
```

🧠 **Explications :**
- L’expression `age >= 18` vérifie si la valeur de `age` est supérieure ou égale à 18.  
- Si la condition est vraie, Python exécute le bloc situé **sous** le `if`.  
- Sinon, le bloc du `else` est exécuté.  

💡 **Astuce :**  
Vous pouvez aussi écrire une version plus concise avec un **opérateur ternaire** :
```python
print("Majeur" if age >= 18 else "Mineur")
```

---

## <span style="color:lime;">Résumé</span> 🧩

Ces exercices permettent de :
- Comprendre la création et l’utilisation de **variables**.  
- Manipuler des **nombres** et des **chaînes de caractères**.  
- Utiliser une **condition** pour prendre des décisions dans un programme.  

👉 Ces bases sont essentielles pour les prochains cours, où vous apprendrez à combiner ces concepts dans des programmes plus complexes (boucles, fonctions, et structures de données).
