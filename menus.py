from equipement import Equipement


def menu(etudiants_existants, systeme, gestionnaire):

    while True:
        print("\n--- Système de Gestion de Laboratoire ---")
        print("1. Étudiant")
        print("2. Gestionnaire")
        print("3. Quitter")
        choix = input("Choisissez votre rôle : ")

        if choix == "1":
            menu_etudiant(etudiants_existants, systeme)
        elif choix == "2":
            menu_gestionnaire(systeme, gestionnaire)
        elif choix == "3":
            print("Au revoir !")
            break
        else:
            print("Choix invalide, réessayez.")

def menu_etudiant(etudiants_existants, systeme):
    print("\n--- Menu Étudiant ---")
    print("Étudiants existants :")
    for idx, etu in enumerate(etudiants_existants):
        print(f"{idx+1}. {etu.nom} {etu.prenom} ({etu.matricule})")
    choix = input("Choisissez votre numéro d'étudiant : ")
    try:
        etu = etudiants_existants[int(choix)-1]
    except:
        print("Étudiant invalide.")
        return

    while True:
        print(f"\n--- Actions pour {etu.nom} {etu.prenom} ---")
        print("1. Réserver un équipement")
        print("2. Lister mes réservations")
        print("3. Retour au menu principal")
        action = input("Choisissez une action : ")

        if action == "1":
            print("\nÉquipements disponibles :")
            for idx, eq in enumerate(systeme.equipements):
                print(f"{idx+1}. {eq.nom} (Stock: {eq.stock})")
            choix_eq = input("Numéro de l'équipement : ")
            qte = input("Quantité : ")
            try:
                eq = systeme.equipements[int(choix_eq)-1]
                etu.reserver_equipement(systeme, eq, int(qte))
            except:
                print("Erreur lors de la réservation.")
        elif action == "2":
            systeme.rechercher_reservation_par_etudiant(etu.matricule)
        elif action == "3":
            break
        else:
            print("Action invalide.")

def menu_gestionnaire(systeme, gestionnaire):
    while True:
        print("\nActions disponibles :")
        print("1. Ajouter un équipement")
        print("2. Supprimer un équipement")
        print("3. Rechercher un équipement")
        print("4. Valider toutes les réservations en attente")
        print("5. Lister équipements disponibles")
        print("6. Retour au menu principal")
        action = input("Choisissez une action : ")

        if action == "1":
            nom = input("Nom de l'équipement : ")
            ref = input("Référence : ")
            stock = int(input("Stock initial : "))
            cat = input("Catégorie : ")
            eq = Equipement(nom, ref, stock, cat)
            gestionnaire.ajouter_equipement(systeme, eq)
        elif action == "2":
            ref = input("Référence de l'équipement à supprimer : ")
            gestionnaire.supprimer_equipement(systeme, ref)
        elif action == "3":
            nom = input("Nom de l'équipement à rechercher : ")
            gestionnaire.rechercher_equipement(systeme, nom)
        elif action == "4":
            for res in systeme.reservations:
                if res.statut == "En attente":
                    gestionnaire.valider_reservation(res)
        elif action == "5":
            systeme.lister_equipements_disponibles()
        elif action == "6":
            break
        else:
            print("Action invalide.")
