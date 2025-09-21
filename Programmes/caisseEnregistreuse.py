produits = {}


def enregistrer():
    while True:
        print()
        print("----- Enregistrez un nouveau produit -----")
        print("Laissez le champ du nom vide pour finir l'enregistrement de produits.")
        nomProduit = input("Quel est le nom du produit? : ").lower()
        if nomProduit == "":
            break
        elif nomProduit in produits:
            print("Attention, le produit existe déjà. Voulez-vous changer le prix de cet article?")
            changeProduit = input("Tapez OUI pour continuer : ").lower()
            if changeProduit != "oui":
                continue
        prixProduit = input("Quel est le prix du produit? : ")
        prixProduit = verifierInt(prixProduit)
        if prixProduit != None:
            produits[nomProduit] = prixProduit
        else:
            print("Format du prix incorrect, opération annulée.")

def commander():
    commande = {}
    while True:
        print()
        print("----- Commandez un nouveau produit -----")
        print("Laissez le champ du nom vide pour finir votre commande.")
        afficherProduits()
        nom = input("Quel produit voulez-vous acheter? : ").lower()
        if nom == "":
            break
        elif not nom in produits:
            print("Ce produit n'existe pas.")
            continue
        if nom in commande:
            print("Attention, le produit est déjà dans la commande. Voulez-vous ajouter cet article?")
            changeProduit = input("Tapez OUI pour continuer : ").lower()
            if changeProduit != "oui":
                continue
        quantité = input("Combien d'exemplaires souhaitez-vous acheter? : ")
        quantité = verifierInt(quantité)
        if quantité != None:
            if nom in commande:
                commande[nom] += quantité
            else:
                commande[nom] = quantité    
        else:
            print("Format de quantité incorrect, veuillez recommencer.")
    afficherTicket(commande)

def verifierInt(nombreAVerifier):
    if nombreAVerifier.isdigit():
        return int(nombreAVerifier)
    else:
        return None
    
def afficherProduits():
    print("Produits disponibles : ", end="* ")
    for produit in produits:
        print(produit, end=" * ")
    print()

def afficherTicket(commande):
    total = 0
    print()
    print("----- Voici votre commande -----")
    for produit in commande:
        prix = commande[produit] * produits[produit]
        total += prix
        print(f"* {produit} : {commande[produit]} x {produits[produit]} = {prix} €")
    print("Prix total de votre commande : " + str(total) + " €.")


while True:
    print()
    print("----- Veuillez choisir votre action -----")
    menuPrincipal = input("Entrez 1 pour enregistrer un produit, 2 pour passer une commande, 3 pour quitter le programme: ")
    match menuPrincipal:
        case "1": enregistrer()
        case "2": commander()
        case "3": break
        case _: 
            print("Commande non reconnue.")
            continue



    

    