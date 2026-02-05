import data as d


def afficher_solde():
    print("\n===== VOTRE SOLDE =====\n")
    print(f"Principale : {d.s_principal} cfa")
    print(f"Internet : {d.s_internet}")
    print(f"Appelle : {d.s_appelle}\n")
    
def choix_forfait():
    while True:
        print("===== Portail forfait =====")
        print("1. Forfait internet")
        print("2. Forfait Appelle")
        print("3. Revenir au menu principal")

        while True:
                try:
                    choix = int(input("\nVotre choix : "))
                except ValueError:
                    print("\n❌ Erreur : Vous avez entré une LETTRE, veuillez entrer un CHIFFRE.")
                    continue

                match choix:
                    case 1:
                        f_internet()
                    case 2:
                        pass
                    case 3:
                        return
                    case  _:
                        print("❌ Erreur : Le chiffre doit être entre 1 et 3.")  
                        continue

            


def f_internet():
    while True:
        print("1. Jour")
        print("2. Semaine")
        print("3. Revenir")
        print("4. Revenir au menu principal")

        try:
            choix = int(input("\nVotre choix : "))
        except ValueError:
            print("\n❌ Erreur : Vous avez entré une LETTRE, veuillez entrer un CHIFFRE.")
            continue

        match choix:
            case 1: 
                i_jour()
            case 2:
                i_semaine()
            case 3:
                choix_forfait()
            case 4:
                break
            case _:
                print("❌ Erreur : Le chiffre doit être entre 1 et 4.")  
                continue

    
def i_jour():
            while True:
                print("\n===== FORFAIT JOUR =====\n")
                print("1. 50 Mo (100 F)")
                print("2. 600 Mo (500 F)")
                print("3. Revenir")
                try:
                    choix = int(input("\nVotre choix : "))
                except ValueError:
                    print("\n❌ Erreur : Vous avez entré une LETTRE, veuillez entrer un CHIFFRE.")
                    continue
                if choix == 1:
                    if d.s_principal < 100:
                        print("\n❌ Erreur : Votre solde est inssufisantt pour souscrire a cet forfait")
                    else:
                        d.s_internet +=  50
                        d.s_principal -= 100
                        print(f"Félicitation, vous avez souscrit avec succés au forfait jour de 100F, votre solde internet est {d.s_internet} Mo, principal {d.s_principal} cfa.\n")
                
                elif choix == 2:
                    if d.s_principal < 500:
                        print("\n❌ Erreur : Votre solde est inssufisantt pour souscrire a cet forfait")
                    else:
                        d.s_internet +=  600
                        d.s_principal -= 500
                        print(f"Félicitation, vous avez souscrit avec succés au forfait jour de 500F, votre solde internet est {d.s_internet} Mo, principal {d.s_principal} cfa.\n")
                
                elif choix == 3:
                     f_internet()
                
                else:
                     print("\n❌ Erreur : Le chiffre doit être entre 1 et 3.")
                     continue
                break
            return



def i_semaine():
            print("\n===== FORFAIT SEMAINE =====\n")
            print("1. 600 Mo (500 F)")
            print("2. 1 Go (1000 F)")
 