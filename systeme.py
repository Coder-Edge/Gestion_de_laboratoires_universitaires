class SystemeGestionLaboratoire:

    def __init__(self):
        self.equipements = []
        self.reservations = []

    def ajouter_reservation(self, reservation):
        self.reservations.append(reservation)

    def lister_reservations(self):
        for res in self.reservations:
            print(f"Étudiant: {res.etudiant.nom}, Équipement: {res.equipement.nom}, Quantité: {res.quantite}, Statut: {res.statut}")

    def lister_equipements_disponibles(self):

        print("Équipements disponibles :")
        for eq in self.equipements:
            if eq.stock > 0:
                eq.afficher_details()

    def rechercher_reservation_par_etudiant(self, matricule):
        print(f"Réservations pour l'étudiant {matricule} :")
        for res in self.reservations:
            if hasattr(res.etudiant, 'matricule') and res.etudiant.matricule == matricule:
                print(f"Équipement: {res.equipement.nom}, Quantité: {res.quantite}, Statut: {res.statut}")
