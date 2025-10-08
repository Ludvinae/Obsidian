# <span style="color:red;">Conditions & Boucles : Correction des Exercices</span> 📘

---

## <span style="color:red;">Exercice 1 : Vérification de la Majorité — Correction</span> 🧩

```python
# --- Exercice 1 : Vérification de la majorité ---
def lire_age(prompt="Entrez votre âge : "):
    while True:
        s = input(prompt).strip()
        if s.startswith("+"):
            s = s[1:]
        if not s or not s.isdigit():
            print("⚠️ Veuillez entrer un entier positif (ex. 18).")
            continue
        age = int(s)
        if 0 <= age <= 130:
            return age
        print("⚠️ L'âge doit être compris entre 0 et 130.")

age = lire_age()

if age >= 65:
    print("✅ Vous êtes senior (majeur).")
elif age >= 18:
    print("✅ Vous êtes majeur.")
else:
    print("ℹ️ Vous êtes mineur.")

# Variante express en une ligne (résumé)
print("Résumé :", "Senior" if age >= 65 else ("Majeur" if age >= 18 else "Mineur"))
```

**💡 Tips apprenants**
- Validez **d’abord** l’entrée, traitez **ensuite** : évitez les `ValueError`.
- Ordonnez vos conditions du **plus spécifique** au **plus général** (ici `>= 65` avant `>= 18`).
- Testez avec `17`, `18`, `65`, `-1`, `131` pour couvrir les **cas limites**.

---

## <span style="color:red;">Exercice 2 : Table de Multiplication — Correction</span> 🧩

```python
# --- Exercice 2 : Table de multiplication ---
def lire_entier(prompt="Entrez un nombre entier : "):
    while True:
        s = input(prompt).strip()
        try:
            return int(s)
        except ValueError:
            print("⚠️ Entier valide requis (ex. 7).")

n = lire_entier()
# Variante : borne supérieure personnalisable
borne = input("Borne supérieure (laisser vide pour 10) : ").strip()
if borne == "":
    haut = 10
else:
    try:
        haut = int(borne)
    except ValueError:
        print("Valeur non valide, utilisation de 10 par défaut.")
        haut = 10

if haut < 1:
    print("ℹ️ Borne < 1 : rien à afficher.")
else:
    print(f"📋 Table de {n} (1 à {haut})")
    for i in range(1, haut + 1):
        print(f"{n} x {i} = {n * i}")
```

**💡 Tips apprenants**
- `range(1, 11)` génère 1→10 (la borne haute est **exclusive**).
- Soignez l’**affichage** (alignement, lisibilité) : c’est un outil de **débogage**.
- Essayez `n = 0` ou `n` négatif : observez que la logique reste correcte.

---

## <span style="color:red;">Exercice 3 : Somme des Nombres Premiers — Correction</span> 🧩

```python
# --- Exercice 3 : Somme des nombres premiers jusqu'à n ---
def lire_entier_positif(prompt="Entrez un entier n (≥ 0) : "):
    while True:
        s = input(prompt).strip()
        if s.startswith("+"):
            s = s[1:]
        if not s.isdigit():
            print("⚠️ Entrez un entier positif (ex. 20).")
            continue
        return int(s)

def est_premier(k: int) -> bool:
    """Test de primalité optimisé (√k et 6k±1)."""
    if k < 2:
        return False
    if k in (2, 3):
        return True
    if k % 2 == 0 or k % 3 == 0:
        return False
    i = 5
    while i * i <= k:
        if k % i == 0 or k % (i + 2) == 0:
            return False
        i += 6
    return True

n = lire_entier_positif()
premiers = []
somme = 0
for nombre in range(2, n + 1):
    if est_premier(nombre):
        premiers.append(nombre)
        somme += nombre

print(f"🔢 Nombres premiers ≤ {n} : {premiers}")
print(f"🧮 Somme : {somme}")
```

**💡 Tips apprenants**
- `< 2` ⇒ **pas premier** ; commencez la boucle à `2`.
- L’optimisation `6k ± 1` réduit nettement le nombre de divisions testées.
- Pour des **très grands n**, préférez un **crible d’Ératosthène**.

---

## <span style="color:red;">Exercice 4 : Affichage des Caractères — Correction</span> 🧩

```python
# --- Exercice 4 : Affichage des caractères avec leur index ---
texte = input("Entrez une chaîne de caractères : ")

if not texte:
    print("ℹ️ Chaîne vide : rien à afficher.")
else:
    print("🔤 Caractères et index :")
    for index, caractere in enumerate(texte):
        # Classification simple du caractère
        if caractere.isspace():
            nature = "espace"
        elif caractere.isalpha():
            nature = "lettre"
        elif caractere.isdigit():
            nature = "chiffre"
        else:
            nature = "symbole"
        print(f"Index {index} : {caractere} ({nature})")
```

**💡 Tips apprenants**
- `enumerate(texte)` vous donne `(index, caractère)` à chaque tour.
- Les **espaces** et caractères spéciaux **comptent** : ne les oubliez pas.
- La petite catégorisation vous fait pratiquer les **conditions multiples**.

---

## <span style="color:red;">Exercice 5 : Calcul de la Moyenne — Correction</span> 🧩

```python
# --- Exercice 5 : Moyenne d'une série de nombres ---
def lire_serie_nombres(prompt="Entrez des nombres séparés par des espaces : "):
    while True:
        s = input(prompt).strip()
        if not s:
            print("⚠️ Saisissez au moins un nombre.")
            continue
        # Autoriser virgule décimale : "3,5" → "3.5"
        tokens = [t.replace(",", ".") for t in s.split()]
        try:
            return [float(t) for t in tokens]
        except ValueError:
            print("⚠️ Utilisez uniquement des nombres (ex. 10 12.5 3,2).")

nombres = lire_serie_nombres()
moyenne = sum(nombres) / len(nombres)
print(f"📊 Nombres saisis : {nombres}")
print(f"📈 Moyenne : {moyenne}")
```

**💡 Tips apprenants**
- Séparez le flux : **lire → valider → convertir → calculer → afficher**.
- Gérez les **entrées vides** pour éviter `ZeroDivisionError`.
- Testez les cas : une seule valeur, valeurs **négatives** et **décimales**.

---

## <span style="color:lime;">(Optionnel) Bonus — Corrections rapides</span> 🧪

### B1 — Deviner le nombre
```python
import random

secret = random.randint(1, 100)
essais_max = 7
print("🎯 Devinez le nombre entre 1 et 100. Vous avez", essais_max, "essais.")

for essai in range(1, essais_max + 1):
    try:
        guess = int(input(f"Essai {essai}/{essais_max} : "))
    except ValueError:
        print("⚠️ Entrez un entier.")
        continue
    if guess == secret:
        print("✅ Bravo ! Trouvé en", essai, "essai(s).")
        break
    print("Plus grand ↑" if guess < secret else "Plus petit ↓")
else:
    print(f"❌ Perdu. Le nombre était {secret}.")
```

### B2 — Filtre pair/impair
```python
s = input("Entrez des entiers séparés par des espaces : ")
pairs, impairs = [], []
for tok in s.split():
    try:
        n = int(tok)
    except ValueError:
        print(f"⏭️ Ignoré (non entier) : {tok}")
        continue
    (pairs if n % 2 == 0 else impairs).append(n)

print("Pairs  :", pairs)
print("Impairs:", impairs)
```

### B3 — Recherche dans une liste
```python
mots = ["python", "boucle", "condition", "liste", "chaine"]
cible = input("Mot à rechercher : ").strip().lower()

for i, m in enumerate(mots):
    if m == cible:
        print(f"✅ Trouvé : '{cible}' à l'index {i}.")
        break
else:
    print(f"🔎 '{cible}' introuvable.")
```

---

## 🎯 Récap Tips transversaux
- **Validez puis traitez** : évitez les crashs dus aux entrées utilisateur.
- **Cas limites d’abord** : vide, zéro, négatif, extrême.
- **Indentation stricte (4 espaces)** : structure obligatoire en Python.
- **Messages clairs** : l’utilisateur doit comprendre quoi saisir et pourquoi ça échoue.
- **Itération incrémentale** : code simple qui marche → améliorations (variantes, perfs, UX).

---
