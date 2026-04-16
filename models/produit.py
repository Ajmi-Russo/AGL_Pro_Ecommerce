# Fichier : models/produit.py
# Basé sur le diagramme UML AGL_Pro_Classes.puml

# Définition de la classe Produit (représente un article du e-commerce)
class Produit:

    # Constructeur : appelé automatiquement lors de la création d'un objet Produit
    def __init__(self, id: int, nom: str, prix: float, quantite_stock: int):
        self.id = id  # identifiant unique du produit
        self.nom = nom  # nom du produit (ex: PC, souris...)
        self.prix = prix  # prix du produit en dinars (DT)
        self.quantite_stock = quantite_stock  # quantité disponible en stock

    # Méthode pour afficher les informations du produit
    def afficher_details(self):
        # Affiche les infos de manière lisible
        print(f"Produit: {self.nom}, Prix: {self.prix}DT, Stock: {self.quantite_stock}")

    # Méthode pour vérifier si le produit est disponible en stock
    def verifier_disponibilite(self) -> bool:
        # Retourne True si stock > 0, sinon False
        return self.quantite_stock > 0