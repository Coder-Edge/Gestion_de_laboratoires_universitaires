from personne import Etudiant, Gestionnaire
from equipement import Equipement
from systeme import SystemeGestionLaboratoire

# Création du système
systeme = SystemeGestionLaboratoire()

# Création des équipements
eq1 = Equipement("Microscope", "EQ001", 5, "Optique")
eq2 = Equipement("Oscilloscope", "EQ002", 3, "Électronique")
eq3 = Equipement("Balance", "EQ003", 10, "Chimie")
systeme.equipements.extend([eq1, eq2, eq3])

# Création des étudiants et gestionnaire
etudiant1 = Etudiant("Ngoma", "Jean", "jean.ngoma@ulc.cd", "E001")
etudiant2 = Etudiant("Kabasele", "Marie", "marie.kabasele@ulc.cd", "E002")
etudiants_existants = [etudiant1, etudiant2]
gestionnaire = Gestionnaire("Mbemba", "Paul", "paul.mbemba@ulc.cd")

# --- Menu interactif ---
from menus import menu
menu(etudiants_existants, systeme, gestionnaire)
