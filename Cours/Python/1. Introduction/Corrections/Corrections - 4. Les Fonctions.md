# <span style="color:red;">Les Fonctions en python : Corrections</span> 📘

> Solutions prêtes à exécuter (Python 3.x), avec docstrings, appels d’exemple et validations simples quand pertinent.

---

## <span style="color:red;">Correction — Exercices n°1 : Définir & Appeler une fonction</span> 📞

```python
def aire_rectangle(longueur: float, largeur: float) -> float:
    """
    Calcule et retourne l'aire d'un rectangle.

    Args:
        longueur (float): longueur du rectangle (≥ 0).
        largeur  (float): largeur du rectangle (≥ 0).
    Returns:
        float: aire = longueur * largeur.
    """
    return longueur * largeur

# Appels d'exemple (3 jeux de valeurs)
exemples = [(5, 3), (10.5, 2), (0, 7)]
for L, l in exemples:
    aire = aire_rectangle(L, l)
    print(f"Aire({L} x {l}) = {aire}")
```

---

## <span style="color:red;">Correction — Exercices n°2 : Paramètres & Arguments</span> 🧩

```python
def presenter(nom: str, age: int, ville: str = None) -> None:
    """
    Affiche une présentation simple. 'ville' peut être omise.

    Args:
        nom (str): prénom ou nom de la personne.
        age (int): âge en années.
        ville (str, optionnel): ville de résidence. Si None, n'est pas mentionnée.
    """
    if ville is None:
        print(f"Je m'appelle {nom} et j'ai {age} ans.")
    else:
        print(f"Je m'appelle {nom}, j'ai {age} ans et j'habite à {ville}.")

# Appel avec arguments positionnels
presenter("Alice", 30)

# Appel avec arguments mots-clés (ordre inversé)
presenter(age=25, nom="Bob")

# Variante avec valeur par défaut pour 'ville' (utilisation de la valeur par défaut)
presenter("Chloé", 22)

# Variante en fournissant une autre ville
presenter("David", 28, ville="Lyon")
```

---

## <span style="color:red;">Correction — Exercices n°3 : Avec et sans `return`</span> 🗣️

```python
def saluer(nom: str = "monde") -> None:
    """Affiche un message de salutation et ne retourne rien d'utile."""
    print(f"Bonjour, {nom} !")

def phrase_bienvenue(nom: str) -> str:
    """Retourne une phrase de bienvenue sans l'afficher."""
    return f"Bienvenue, {nom}."

# Différence d'usage
retour_saluer = saluer()                     # affiche "Bonjour, monde !"
print("Retour de saluer():", retour_saluer)  # None

msg = phrase_bienvenue("Nina")               # ne rien afficher ici
print(msg)                                   # affiche ensuite le résultat stocké
```

---

## <span style="color:red;">Correction — Exercices n°4 : Valeurs par défaut & signature</span> 🧱

```python
def prix_total(prix_unitaire: float, quantite: int = 1, remise: float = 0.0) -> float:
    """
    Calcule le total à payer.

    Args:
        prix_unitaire (float): prix d'un article (en €).
        quantite (int, optionnel): nombre d'articles (défaut = 1).
        remise (float, optionnel): taux de remise entre 0 et 1 (ex. 0.2 pour 20%).
    Returns:
        float: total = prix_unitaire * quantite * (1 - remise)
    """
    return prix_unitaire * quantite * (1 - remise)

# 1) Seulement avec prix_unitaire
print("Cas 1 (1 article, sans remise) :", prix_total(12.0), "€  → achat unitaire")

# 2) Avec prix_unitaire et quantite
print("Cas 2 (quantité)               :", prix_total(9.99, 3), "€  → achat en quantité")

# 3) Avec prix_unitaire et remise en mot-clé
print("Cas 3 (remise 15%)             :", prix_total(50.0, remise=0.15), "€  → promo ponctuelle")

# 4) Les trois paramètres, avec mot-clé
print("Cas 4 (quantité + remise)      :", prix_total(prix_unitaire=20.0, quantite=5, remise=0.1), "€  → lot en promotion")
```

---

## <span style="color:red;">Correction — Exercices n°5 : Portée (locale vs globale)</span> 🔍

```python
message = "global"

def demo_portee() -> None:
    message = "local"   # variable locale, masque la globale dans cette fonction
    print("Dans demo_portee() :", message)

demo_portee()
print("En dehors           :", message)

# Explication (commentaire) :
# La variable 'message' définie dans la fonction est locale à celle-ci et n'affecte pas la variable globale.
# À l'extérieur, 'message' reste "global".

# (Optionnel) Lecture de la globale et tentative de modification locale
def lire_globale() -> None:
    print("lire_globale() voit :", message)  # lit la globale

def tentative_modif_globale() -> None:
    message = "modif_locale"  # crée une nouvelle variable locale, ne modifie pas la globale
    print("tentative_modif_globale() :", message)

lire_globale()
tentative_modif_globale()
print("Après tentative     :", message)      # reste "global"
```

---

## <span style="color:red;">Correction — Exercices n°6 : Refactorisation</span> 🔁

```python
# --- Sans fonction (naïf / répétitif) ---
PU1, Q1, R1, PRO1 = 5.0, 2, 0.0, "Stylo"
PU2, Q2, R2, PRO2 = 12.5, 1, 0.1, "Carnet"
PU3, Q3, R3, PRO3 = 2.0, 10, 0.05, "Crayon"

# Ticket 1
sous_total = PU1 * Q1
total = sous_total * (1 - R1)
print(f"--- Ticket ---\nProduit: {PRO1}\nQté: {Q1} x {PU1}€\nRemise: {R1*100:.0f}%\nTotal: {total:.2f}€\n")

# Ticket 2
sous_total = PU2 * Q2
total = sous_total * (1 - R2)
print(f"--- Ticket ---\nProduit: {PRO2}\nQté: {Q2} x {PU2}€\nRemise: {R2*100:.0f}%\nTotal: {total:.2f}€\n")

# Ticket 3
sous_total = PU3 * Q3
total = sous_total * (1 - R3)
print(f"--- Ticket ---\nProduit: {PRO3}\nQté: {Q3} x {PU3}€\nRemise: {R3*100:.0f}%\nTotal: {total:.2f}€\n")

# --- Refactorisé avec une fonction réutilisable ---
def afficher_ticket(produit: str, prix_unitaire: float, quantite: int = 1, remise: float = 0.0) -> None:
    """
    Affiche un ticket de caisse formaté.

    Args:
        produit (str): libellé du produit.
        prix_unitaire (float): prix unitaire en €.
        quantite (int, optionnel): quantité (défaut 1).
        remise (float, optionnel): taux de remise entre 0 et 1.
    """
    sous_total = prix_unitaire * quantite
    total = sous_total * (1 - remise)
    print("--- Ticket ---")
    print(f"Produit : {produto if (produto := produit) else 'N/A'}")
    print(f"Qté     : {quantite} x {prix_unitaire:.2f}€")
    print(f"Remise  : {remise*100:.0f}%")
    print(f"Total   : {total:.2f}€\n")

# Remplacement des trois blocs par trois appels
afficher_ticket(PRO1, PU1, Q1, R1)
afficher_ticket(PRO2, PU2, Q2, R2)
afficher_ticket(PRO3, PU3, Q3, R3)
```

---

## <span style="color:red;">Correction — Exercices n°7 : Docstring claire</span> 📚

```python
def est_majeur(age: int) -> bool:
    """
    Indique si une personne est majeure selon l'âge.

    Args:
        age (int): âge en années (≥ 0).
    Returns:
        bool: True si age >= 18, sinon False.

    Exemple:
        >>> est_majeur(20)
        True
    """
    return age >= 18

# Tests d'appel
print("est_majeur(17) :", est_majeur(17))  # False
print("est_majeur(18) :", est_majeur(18))  # True
print("est_majeur(65) :", est_majeur(65))  # True
```

---

## <span style="color:red;">Correction — Exercices n°8 : Séparation I/O et logique</span> 🧪

```python
def moyenne(a: float, b: float, c: float) -> float:
    """
    Retourne la moyenne arithmétique de trois nombres.

    Args:
        a (float), b (float), c (float): valeurs numériques.
    Returns:
        float: (a + b + c) / 3
    """
    return (a + b + c) / 3

# --- Interaction utilisateur hors de la fonction ---
def lire_float(prompt: str) -> float:
    """Lit un nombre (float), redemande en cas d'erreur."""
    while True:
        s = input(prompt).strip().replace(",", ".")
        try:
            return float(s)
        except ValueError:
            print("⚠️ Entrez un nombre valide (ex. 12.5).")

x = lire_float("Entrez la première valeur : ")
y = lire_float("Entrez la deuxième valeur : ")
z = lire_float("Entrez la troisième valeur : ")

m = moyenne(x, y, z)
print(f"📈 Moyenne de ({x}, {y}, {z}) = {m:.2f}")
```

---

### ✅ Rappels rapides
- Une fonction **retourne** des valeurs (calcul) ; l’**affichage** se fait de préférence en dehors.  
- **Docstrings** courtes et utiles : but, paramètres, retour.  
- **Signatures** claires avec valeurs par défaut quand c’est pertinent.  
- **Tester plusieurs cas** (normaux et limites) pour valider le comportement.
