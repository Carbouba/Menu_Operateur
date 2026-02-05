# Importation des données des differents fichiers
import fonctions as f 




# Programme principal

""" 
Ce fichier se lance une fois le programme 
est executé.

Il affiche d'abord l'état de compte de l'utilisateur 
tel que : le solde et le forfait actif.

Ensuite il affiche le menu principal

 """


# Menu principal (bouclé)
while True:
    print("\n===== BIENVENUE AU MENU =====\n")
    print("Que souhaitez vous faire ?\n")
    print("1. Voir mon solde")
    print("2. Acheter un forfait")
    print("3. Quitter")
    print("====================")

    try:
        choix = int(input("\nVotre choix : "))
    except ValueError:
        print("\n❌ Erreur : Vous avez entré une LETTRE, veuillez entrer un CHIFFRE.")
        continue

    match choix:
        case 1: 
            f.afficher_solde()
        case 2:
            f.choix_forfait()
        case 3:
            break
        case _:
            print("❌ Erreur : Le chiffre doit être entre 1 et 3.")  
            continue

# Rien a ajouter apres cette ligne

