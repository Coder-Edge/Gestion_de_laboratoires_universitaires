from abc import ABC

class Personne(ABC):
    def __init__(self, nom, prenom, email):
        self._nom = nom
        self._prenom = prenom
        self._email = email

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, value):
        self._nom = value

    @property
    def prenom(self):
        return self._prenom

    @prenom.setter
    def prenom(self, value):
        self._prenom = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

class Etudiant(Personne):
    def __init__(self, nom, prenom, email, matricule):
        super().__init__(nom, prenom, email)
        self.matricule = matricule

    def reserver_equipement(self, systeme, equipement, quantite):
        if equipement.est_disponible(quantite):
            from reservation import Reservation
            reservation = Reservation(self, equipement, quantite)
            systeme.ajouter_reservation(reservation)
            print(f"Réservation de {quantite} {equipement.nom} par {self.nom} {self.prenom} en attente.")
        else:
            print(f"Échec : {equipement.nom} ne dispose pas de stock suffisant.")

class Gestionnaire(Personne):
    def __init__(self, nom, prenom, email):
        super().__init__(nom, prenom, email)

    def valider_reservation(self, reservation):
        if reservation.equipement.est_disponible(reservation.quantite):
            reservation.changer_statut("Validée")
            reservation.equipement.changer_stock(-reservation.quantite)
            print(f"Réservation validée : {reservation.equipement.nom} pour {reservation.etudiant.nom}.")
        else:
            reservation.changer_statut("Rejetée")
            print(f"Réservation rejetée : {reservation.equipement.nom} stock insuffisant.")

    def ajouter_equipement(self, systeme, equipement):
        systeme.equipements.append(equipement)
        print(f"Équipement ajouté : {equipement.nom}")

    def rechercher_equipement(self, systeme, nom):
        for eq in systeme.equipements:
            if eq.nom.lower() == nom.lower():
                eq.afficher_details()
                return eq
        print("Équipement non trouvé.")
        return None

    def supprimer_equipement(self, systeme, reference):
        for eq in systeme.equipements:
            if eq.reference == reference:
                systeme.equipements.remove(eq)
                print(f"Équipement supprimé : {eq.nom}")
                return
        print("Équipement introuvable.")
