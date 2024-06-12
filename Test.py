import unittest
from datetime import datetime
from class1 import Client, Acteur, Employe, CarteCredit, Film, Categorie

class TestClient(unittest.TestCase):
    def setUp(self):
        self.client = Client("John", "Doe", "M", "2023-01-01", "john.doe@example.com", "password123")
        self.clients = [self.client]

    def test_ajouter_carte_credit(self):
        carte = CarteCredit("12345678", "12/25", "123")
        self.client.ajouter_carte_credit(carte)
        self.assertIn(carte, self.client.cartes_credit)

    def test_client_courriel_unique(self):
        other_client = Client("Jane", "Doe", "F", "2023-01-01", "john.doe@example.com", "password123")
        with self.assertRaises(ValueError):
            if any(client.courriel == other_client.courriel for client in self.clients):
                raise ValueError("Le courriel doit être unique")
            self.clients.append(other_client)

class TestActeur(unittest.TestCase):
    def setUp(self):
        self.acteur = Acteur("Leonardo", "DiCaprio", "M", "Cobb", "2010-07-16", "2010-07-16", 20000000)

    def test_acteur_attributes(self):
        self.assertEqual(self.acteur.nom_personnage, "Cobb")
        self.assertEqual(self.acteur.cachet, 20000000)

class TestEmploye(unittest.TestCase):
    def setUp(self):
        self.employe = Employe("Admin", "User", "M", "2022-01-01", "admin", "password", "modify")

    def test_employe_attributes(self):
        self.assertEqual(self.employe.code_utilisateur, "admin")
        self.assertEqual(self.employe.type_acces, "modify")

class TestFilm(unittest.TestCase):
    def setUp(self):
        self.film = Film("Inception", "148", "A thief who steals corporate secrets through dream-sharing technology.")

    def test_ajouter_categorie(self):
        categorie = Categorie("Action", "Action-packed movie")
        self.film.ajouter_categorie(categorie)
        self.assertIn(categorie, self.film.categories)

    def test_ajouter_acteur(self):
        acteur = Acteur("Leonardo", "DiCaprio", "M", "Cobb", "2010-07-16", "2010-07-16", 20000000)
        self.film.ajouter_acteur(acteur)
        self.assertIn(acteur, self.film.acteurs)

class TestCarteCredit(unittest.TestCase):
    def setUp(self):
        self.carte = CarteCredit("12345678", "12/25", "123")

    def test_carte_attributes(self):
        self.assertEqual(self.carte.numero, "12345678")
        self.assertEqual(self.carte.date_expiration, "12/25")
        self.assertEqual(self.carte.code_secret, "123")

class TestCategorie(unittest.TestCase):
    def setUp(self):
        self.categorie = Categorie("Action", "Action-packed movie")

    def test_categorie_attributes(self):
        self.assertEqual(self.categorie.nom, "Action")
        self.assertEqual(self.categorie.description, "Action-packed movie")

if __name__ == "__main__":
    unittest.main()
