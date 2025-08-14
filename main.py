from personne import Etudiant, Gestionnaire
from equipement import Equipement
from systeme import SystemeGestionLaboratoire
from menus import menu

# Création du système
systeme = SystemeGestionLaboratoire()

# Création des équipements
eq1 = Equipement("Microscope", "EQ001", 5, "Optique")
eq2 = Equipement("Oscilloscope", "EQ002", 3, "Électronique")
eq3 = Equipement("Balance", "EQ003", 10, "Chimie")
systeme.equipements.extend([eq1, eq2, eq3])

# Création des étudiants et gestionnaire
etudiant1 = Etudiant("Lukemba", "John", "jean.ngoma@ulc.cd", "E001")
etudiant2 = Etudiant("Miradi", "Malolo", "marie.kabasele@ulc.cd", "E002")
etudiants_existants = [etudiant1, etudiant2]
gestionnaire = Gestionnaire("Lukamba", "Nathan", "nathan@gmail.com")

# --- Menu interactif ---
menu(etudiants_existants, systeme, gestionnaire)
