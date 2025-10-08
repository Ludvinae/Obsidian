# <span style="color:red;">Introduction aux Conditions et Boucles en JavaScript : Exercices</span> 📘

---

## <span style="color:red;">Exercice n°1</span> 🧮  
**Condition simple : Vérification de l’âge**

Déclarez une variable `age` contenant votre âge.  
Écrivez une condition `if` pour afficher :
- `"Vous êtes majeur"` si `age >= 18`
- `"Vous êtes mineur"` sinon.

💡 **Tips pour apprenants :**  
> Testez avec plusieurs valeurs (par exemple 15, 18, 25) pour bien comprendre le comportement du `if...else`.

---

## <span style="color:red;">Exercice n°2</span> ⚙️  
**Note d’évaluation avec `if...else if...else`**

Créez une variable `note` (valeur entre 0 et 100).  
Affichez un message selon la note :
- `note >= 90` → `"Excellent !"`
- `note >= 80` → `"Très bien !"`
- `note >= 70` → `"Bien."`
- sinon → `"À améliorer."`

💡 **Tips pour apprenants :**  
> Utilisez les opérateurs de comparaison (`>=`, `<`) dans le bon ordre pour éviter que certaines conditions soient ignorées.

---

## <span style="color:red;">Exercice n°3</span> 🔢  
**Boucle `for` : Compteur simple**

Écrivez une boucle `for` qui affiche les nombres de **1 à 10** dans la console.

💡 **Tips pour apprenants :**  
> Rappelez-vous la structure :  
> `for (initialisation; condition; incrémentation) { ... }`  
> Exemple : `for (let i = 0; i < 5; i++)`.

---

## <span style="color:red;">Exercice n°4</span> 🔁  
**Boucle et Condition : Nombres pairs et impairs**

Écrivez une boucle `for` qui parcourt les nombres de **1 à 20**.  
Pour chaque nombre :
- Affiche `"X est pair"` si le nombre est pair.  
- Affiche `"X est impair"` sinon.

💡 **Tips pour apprenants :**  
> Utilisez l’opérateur modulo `%` pour vérifier si un nombre est pair :  
> `if (nombre % 2 === 0)`

---

## <span style="color:red;">Exercice n°5</span> 🧠  
**Boucle `while` : Compte à rebours**

Créez une variable `compteur = 10`.  
À l’aide d’une boucle `while`, affichez les nombres de 10 à 1.  
À la fin, affichez `"Décollage 🚀"`.

💡 **Tips pour apprenants :**  
> N’oubliez pas de **décrémenter** votre compteur (`compteur--`) à chaque itération pour éviter une boucle infinie.

---

## <span style="color:red;">Exercice n°6</span> 🧩  
**Boucle `for...of` : Parcourir un tableau**

Créez un tableau `fruits = ["Pomme", "Banane", "Fraise", "Mangue"]`.  
Utilisez une boucle `for...of` pour afficher dans la console :  
`"J’aime le fruit : [nom du fruit]"`

💡 **Tips pour apprenants :**  
> `for...of` est plus lisible qu’un `for` classique quand on parcourt un tableau.

---

## <span style="color:red;">Exercice n°7</span> 🎯  
**Combinaison : Boucle et Condition**

Écrivez un programme qui affiche tous les nombres de **1 à 30**.  
Mais :
- Si le nombre est divisible par 3 → affiche `"Fizz"`  
- Si le nombre est divisible par 5 → affiche `"Buzz"`  
- Si le nombre est divisible par **3 et 5** → affiche `"FizzBuzz"`

💡 **Tips pour apprenants :**  
> Commencez par vérifier le cas **3 et 5** avant les autres, sinon il sera ignoré !
