class Equipement:

    def __init__(self, nom, reference, stock, categorie):
        self.nom = nom
        self.reference = reference
        self.stock = stock
        self.categorie = categorie

    def afficher_details(self):
        print(f"Nom: {self.nom}, Réf: {self.reference}, Stock: {self.stock}, Catégorie: {self.categorie}")

    def changer_stock(self, quantite):
        self.stock += quantite

    def est_disponible(self, quantite):
        return self.stock >= quantite
