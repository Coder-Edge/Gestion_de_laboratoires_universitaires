class Reservation:

    def __init__(self, etudiant, equipement, quantite):
        self.etudiant = etudiant
        self.equipement = equipement
        self.quantite = quantite
        self.statut = "En attente"

    def changer_statut(self, statut):
        self.statut = statut
