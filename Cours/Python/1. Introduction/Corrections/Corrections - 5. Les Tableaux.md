# <span style="color:red;">Les Tableaux (Listes) en Python : Corrections</span> 📘

> Solutions Python 3.x prêtes à exécuter. Chaque exercice inclut du code clair et autonome.

---

## <span style="color:red;">Correction — Exercice n°1 : Accès & Slicing</span> ✂️

```python
# Exercice 1 — Accès & Slicing
nombres = [10, 20, 30, 40, 50, 60, 70]

premier = nombres[0]
dernier = nombres[-1]
milieu = nombres[len(nombres) // 2]  # ici 40 (indice 3)

sous_2_4 = nombres[2:5]   # indices 2..4 (fin exclue) → [30, 40, 50]
trois_premiers = nombres[:3]
trois_derniers = nombres[-3:]
un_sur_deux = nombres[::2]
inversee = nombres[::-1]

print("Premier :", premier)
print("Dernier :", dernier)
print("Milieu  :", milieu)
print("2..4    :", sous_2_4)
print("3 premiers :", trois_premiers)
print("3 derniers :", trois_derniers)
print("Un sur deux :", un_sur_deux)
print("Inversée :", inversee)
```

---

## <span style="color:red;">Correction — Exercice n°2 : Ajouts & Suppressions</span> ➕➖

```python
# Exercice 2 — Ajouts & Suppressions
L = [10, 20, 30]
print("Départ     :", L)

L.append(40)
print("append(40) :", L)

L.insert(1, 15)
print("insert(1,15):", L)

L.extend([41, 42])
print("extend([41,42]):", L)

if 15 in L:
    L.remove(15)
print("remove(15) :", L)

dernier = L.pop()
print("pop() →", dernier, "| L =", L)

del L[1]
print("del L[1]  :", L)

L.clear()
print("clear()   :", L)
```

---

## <span style="color:red;">Correction — Exercice n°3 : Recherche, Comptage & Tri</span> 🔎🗂️

```python
# Exercice 3 — Recherche, Comptage & Tri
couleurs = ["rouge", "vert", "bleu", "Bleu", "jaune", "bleu"]
print("Départ :", couleurs)

# 2) Présence & comptage
print('"vert" présent ? →', "vert" in couleurs)
print('count("bleu")    →', couleurs.count("bleu"))

# 3) Indices 1ère et 2e occurrence de "bleu"
prem = couleurs.index("bleu")            # 1ère occurrence
print("index('bleu')     →", prem)
# chercher après 'prem'
suiv = couleurs.index("bleu", prem + 1)  # 2e occurrence
print("index('bleu', start=prem+1) →", suiv)

# 4) Tri EN PLACE (sensible à la casse)
couleurs_originales = couleurs[:]  # on garde une copie de l'état avant
couleurs.sort()
print("sort() (en place) →", couleurs)

# 5) Nouvelle liste triée SANS tenir compte de la casse (original conservé ici)
sans_casse = sorted(couleurs_originales, key=str.lower)
print("sorted(key=str.lower) →", sans_casse)
print("Original conservé     →", couleurs_originales)

# 6) Inverser EN PLACE
couleurs.reverse()
print("reverse() (en place) →", couleurs)
```

---

## <span style="color:red;">Correction — Exercice n°4 : Listes 2D (création sûre & accès)</span> 🧭

```python
# Exercice 4 — Listes 2D
# 1) Création sûre (4 lignes × 3 colonnes)
grille = [[0] * 3 for _ in range(4)]
print("Grille initiale :")
for lig in grille:
    print(lig)

# 2) Remplacer [0][0] par 1
grille[0][0] = 1
print("\nAprès grille[0][0] = 1 :")
for lig in grille:
    print(lig)

# 3) Somme de chaque ligne
print("\nSommes par ligne :")
for i, lig in enumerate(grille):
    print(f"Ligne {i} → somme = {sum(lig)}")

# 4) Extraire la première colonne
col0 = [lig[0] for lig in grille]
print("\nPremière colonne :", col0)

# 5) Copie ligne par ligne (sous-listes indépendantes)
copie = [lig[:] for lig in grille]
copie[0][1] = 9  # on modifie la copie pour vérifier
print("\nCopie modifiée   :")
for lig in copie:
    print(lig)
print("Original inchangé :")
for lig in grille:
    print(lig)
```

---

## <span style="color:red;">Correction — Exercice n°5 : Compréhensions & Agrégats</span> ⚡🧮

```python
# Exercice 5 — Compréhensions & Agrégats
vals = [3, -1, 5, -7, 2, 0, 9]

positives = [v for v in vals if v >= 0]
carres = [v * v for v in vals]
as_str = [str(v) for v in vals]

print("positives :", positives)
print("carres    :", carres)
print("as_str    :", as_str)

mat = [[1, 2], [3, 4], [5]]
plat = [x for ligne in mat for x in ligne]
print("\nplat :", plat)

print("len(plat) :", len(plat))
print("sum(plat) :", sum(plat))
print("min(plat) :", min(plat))
print("max(plat) :", max(plat))
print("all(v > 0 for v in plat) :", all(v > 0 for v in plat))
print("any(v % 2 == 0 for v in plat) :", any(v % 2 == 0 for v in plat))
```

---

## <span style="color:red;">Correction — BONUS : Mini “Pacman” Console (Listes uniquement)</span> 👾🎮

```python
# Mini "Pacman" console — listes de listes uniquement
# Contrôles: z (haut), s (bas), q (gauche), d (droite), ENTER pour valider
# Victoire: plus de '.' | Défaite: collision avec 'G'

import os
import random
import time

# --- Carte (toutes les lignes même longueur) ---
carte_str = [
    "#############",
    "#P..   .....#",
    "# ### ### # #",
    "#   #     # #",
    "# # ### ### #",
    "# #   G     #",
    "# ######### #",
    "#.........  #",
    "#############",
]

# Conversion en liste de listes (mutable)
grille = [list(ligne) for ligne in carte_str]

HAUT, BAS, GAUCHE, DROITE = (-1, 0), (1, 0), (0, -1), (0, 1)
COMMANDES = {"z": HAUT, "s": BAS, "q": GAUCHE, "d": DROITE}

def effacer():
    os.system("cls" if os.name == "nt" else "clear")

def afficher(grille, score):
    print("\n".join("".join(l) for l in grille))
    print(f"\nScore: {score}   (z/q/s/d pour bouger, 'x' pour quitter)")

def trouver(grille, cible):
    for i, lig in enumerate(grille):
        for j, c in enumerate(lig):
            if c == cible:
                return (i, j)
    return None

def compter_pacgommes(grille):
    total = 0
    for lig in grille:
        for c in lig:
            if c == ".":
                total += 1
    return total

def case_valide(grille, pos):
    i, j = pos
    return 0 <= i < len(grille) and 0 <= j < len(grille[0])

def est_mur(grille, pos):
    i, j = pos
    return grille[i][j] == "#"

def deplacer_si_possible(grille, pos, direction):
    """Retourne la nouvelle position si non mur, sinon l'ancienne."""
    di, dj = direction
    ni, nj = pos[0] + di, pos[1] + dj
    if not case_valide(grille, (ni, nj)):
        return pos
    if est_mur(grille, (ni, nj)):
        return pos
    return (ni, nj)

# Positions initiales
pac = trouver(grille, "P")
ghost = trouver(grille, "G")
score = 0

# On considère que sous P/G il n'y a pas de pac-gomme (cases libres)
grille[pac[0]][pac[1]] = "P"
grille[ghost[0]][ghost[1]] = "G"

def deplacement_alea_ghost(grille, ghost, pac):
    """Un pas aléatoire valide (ne traverse pas les murs)."""
    directions = [HAUT, BAS, GAUCHE, DROITE]
    random.shuffle(directions)
    for d in directions:
        nxt = deplacer_si_possible(grille, ghost, d)
        if nxt != ghost:
            return nxt
    return ghost

# Boucle de jeu
while True:
    effacer()
    afficher(grille, score)

    # Conditions de fin (victoire)
    if compter_pacgommes(grille) == 0:
        print("\n🎉 Victoire ! Plus de pac-gommes.")
        break

    # Lecture commande joueur
    cmd = input("> ").strip().lower()
    if cmd == "x":
        print("Fin de partie.")
        break
    if cmd not in COMMANDES:
        print("Utilisez z/q/s/d (ou 'x' pour quitter).")
        time.sleep(0.6)
        continue

    # --- Déplacer Pacman ---
    d = COMMANDES[cmd]
    new_pac = deplacer_si_possible(grille, pac, d)

    # Collision si la nouvelle position est celle du ghost
    if new_pac == ghost:
        effacer()
        grille[pac[0]][pac[1]] = " "   # P quitte l'ancienne case
        grille[new_pac[0]][new_pac[1]] = "X"  # marque la collision
        afficher(grille, score)
        print("\n💀 Défaite ! Touché par le fantôme.")
        break

    # Manger pac-gomme si présente
    if grille[new_pac[0]][new_pac[1]] == ".":
        score += 10

    # Mettre à jour la grille pour Pacman (l'ancienne case devient vide)
    grille[pac[0]][pac[1]] = " "
    pac = new_pac
    grille[pac[0]][pac[1]] = "P"

    # --- Déplacer le Fantôme ---
    new_ghost = deplacement_alea_ghost(grille, ghost, pac)

    # Collision si le fantôme va sur Pacman
    if new_ghost == pac:
        grille[ghost[0]][ghost[1]] = " "  # l'ancienne case du ghost devient vide
        ghost = new_ghost
        grille[ghost[0]][ghost[1]] = "X"  # marque la collision
        effacer()
        afficher(grille, score)
        print("\n💀 Défaite ! Le fantôme vous a attrapé.")
        break

    # Mettre à jour la grille pour Ghost
    grille[ghost[0]][ghost[1]] = " "
    ghost = new_ghost
    # Par simplicité, les cases du ghost sont considérées comme des espaces
    grille[ghost[0]][ghost[1]] = "G"

    # Petite pause pour la lisibilité (optionnel)
    # time.sleep(0.05)
```

---

### ✅ Conseils rapides
- Lisez le code et **exécutez** chaque cellule pour voir l’effet étape par étape.  
- Pour le “Pacman” : commencez par **afficher la grille** puis ajoutez les **déplacements** progressivement.  
- Évitez les **alias involontaires** (`B = A`) quand vous vouliez une copie (`B = A[:]`).  
- Vérifiez les **indices** et les **bornes** pour éviter `IndexError`.
