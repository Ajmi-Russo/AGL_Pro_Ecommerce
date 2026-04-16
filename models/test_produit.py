# Fichier : test_produit.py

# Import de la classe Produit depuis le dossier models
from produit import Produit

# =========================
# TEST DU PROGRAMME
# =========================

# Création d’un objet Produit
# (id, nom, prix, quantité en stock)
produit1 = Produit(1, "Souris Logitech", 29.99, 50)

# Appel de la méthode pour afficher les détails du produit
produit1.afficher_details()

# Vérification de la disponibilité du produit
# Retourne True si stock > 0, sinon False
print("Disponible :", produit1.verifier_disponibilite())