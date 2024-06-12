import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton,
                             QVBoxLayout, QHBoxLayout, QMessageBox, QTableWidget,
                             QTableWidgetItem, QAbstractItemView)
from datetime import datetime
from class1 import *

# Classe pour la fenêtre de login
class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.setGeometry(100, 100, 280, 150)

        # Utilisateurs prédéfinis pour la connexion
        self.users = {
            "admin": Employe("Admin", "User", "M", "2022-01-01", "admin", "password", "modify"),
            "test": Employe("Test", "User", "F", "2022-01-01", "test", "password", "read")
        }

        # Titre de la fenêtre de login
        self.title = QLabel("NEFFIX", self)
        self.title.setStyleSheet("font-size: 24px; font-weight: bold; color: red;")

        # Champs pour le code utilisateur
        self.usernameLabel = QLabel("Code utilisateur :", self)
        self.usernameLineEdit = QLineEdit(self)

        # Champs pour le mot de passe
        self.passwordLabel = QLabel("Mot de passe :", self)
        self.passwordLineEdit = QLineEdit(self)
        self.passwordLineEdit.setEchoMode(QLineEdit.Password)

        # Boutons de connexion et de sortie
        self.connexionButton = QPushButton("Connexion", self)
        self.exitButton = QPushButton("Exit", self)

        # Disposition de la fenêtre de login
        layout = QVBoxLayout()
        layout.addWidget(self.title)

        # Disposition des champs utilisateur
        usernameLayout = QHBoxLayout()
        usernameLayout.addWidget(self.usernameLabel)
        usernameLayout.addWidget(self.usernameLineEdit)
        layout.addLayout(usernameLayout)

        # Disposition des champs mot de passe
        passwordLayout = QHBoxLayout()
        passwordLayout.addWidget(self.passwordLabel)
        passwordLayout.addWidget(self.passwordLineEdit)
        layout.addLayout(passwordLayout)

        # Disposition des boutons
        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(self.connexionButton)
        buttonLayout.addWidget(self.exitButton)
        layout.addLayout(buttonLayout)

        self.setLayout(layout)

        # Connexion des boutons à leurs fonctions respectives
        self.connexionButton.clicked.connect(self.handle_login)
        self.exitButton.clicked.connect(self.close)

        # Création des listes de clients et films
        self.clients = self.create_sample_clients()
        self.films = self.create_sample_films()

    # Fonction pour gérer la connexion
    def handle_login(self):
        code_utilisateur = self.usernameLineEdit.text()
        password = self.passwordLineEdit.text()

        # Vérification des infos de connexion
        if code_utilisateur in self.users and self.users[code_utilisateur].password == password:
            access_type = self.users[code_utilisateur].type_acces
            self.main_menu = MainMenu(access_type=access_type, clients=self.clients, films=self.films)
            self.main_menu.show()
            self.close()
        else:
            QMessageBox.warning(self, "Erreur de connexion", "Nom d'utilisateur ou mot de passe incorrect")

    # Création d'exemples de clients
    def create_sample_clients(self):
        clients = [
            Client("John", "Doe", "M", "2023-01-01", "john.doe@example.com", "password123"),
            Client("Jane", "Smith", "F", "2023-01-01", "jane.smith@example.com", "password123")
        ]
        # Ajout de cartes de crédit aux clients
        clients[0].ajouter_carte_credit(CarteCredit("12345678", "12/25", "123"))
        clients[1].ajouter_carte_credit(CarteCredit("87654321", "11/24", "321"))
        return clients

    # Création d'exemples de films
    def create_sample_films(self):
        films = []

        # Film 1: Inception
        film1 = Film("Inception", "148",
                     "Un voleur qui dérobe des secrets d'entreprise grâce à la technologie de partage de rêves se voit offrir l'inverse : implanter une idée dans l'esprit d'un C.E.O.")
        categorie1 = Categorie("Action", "Film d'action")
        categorie2 = Categorie("Sci-Fi", "Film de science-fiction")
        film1.ajouter_categorie(categorie1)
        film1.ajouter_categorie(categorie2)
        acteur1 = Acteur("Leonardo", "DiCaprio", "M", "Cobb", "2010-07-16", "2010-07-16", 20000000)
        acteur2 = Acteur("Joseph", "Gordon-Levitt", "M", "Arthur", "2010-07-16", "2010-07-16", 10000000)
        film1.ajouter_acteur(acteur1)
        film1.ajouter_acteur(acteur2)
        films.append(film1)

        # Film 2: The Matrix
        film2 = Film("The Matrix", "136",
                     "Un pirate informatique apprend des rebelles mystérieux la véritable nature de sa réalité et son rôle dans la guerre contre ses contrôleurs.")
        categorie3 = Categorie("Action", "Film d'action")
        categorie4 = Categorie("Sci-Fi", "Film de science-fiction")
        film2.ajouter_categorie(categorie3)
        film2.ajouter_categorie(categorie4)
        acteur3 = Acteur("Keanu", "Reeves", "M", "Neo", "1999-03-31", "1999-03-31", 15000000)
        acteur4 = Acteur("Laurence", "Fishburne", "M", "Morpheus", "1999-03-31", "1999-03-31", 10000000)
        film2.ajouter_acteur(acteur3)
        film2.ajouter_acteur(acteur4)
        films.append(film2)

        # Film 3: The Dark Knight
        film3 = Film("The Dark Knight", "152",
                     "Lorsqu'un sinistre nouveau criminel connu sous le nom de Joker émerge, il plonge Gotham dans le chaos et force Batman à approcher la ligne fine entre héros et justicier.")
        categorie5 = Categorie("Action", "Film d'action")
        categorie6 = Categorie("Thriller", "Film de thriller")
        film3.ajouter_categorie(categorie5)
        film3.ajouter_categorie(categorie6)
        acteur5 = Acteur("Christian", "Bale", "M", "Bruce Wayne", "2008-07-18", "2008-07-18", 20000000)
        acteur6 = Acteur("Heath", "Ledger", "M", "Joker", "2008-07-18", "2008-07-18", 15000000)
        film3.ajouter_acteur(acteur5)
        film3.ajouter_acteur(acteur6)
        films.append(film3)

        # Film 4: Interstellar
        film4 = Film("Interstellar", "169",
                     "Un groupe d'explorateurs interstellaires part à la recherche d'un nouveau foyer pour l'humanité.")
        categorie7 = Categorie("Sci-Fi", "Film de science-fiction")
        categorie8 = Categorie("Aventure", "Film d'aventure")
        film4.ajouter_categorie(categorie7)
        film4.ajouter_categorie(categorie8)
        acteur7 = Acteur("Matthew", "McConaughey", "M", "Cooper", "2014-11-07", "2014-11-07", 20000000)
        acteur8 = Acteur("Anne", "Hathaway", "F", "Brand", "2014-11-07", "2014-11-07", 15000000)
        film4.ajouter_acteur(acteur7)
        film4.ajouter_acteur(acteur8)
        films.append(film4)

        # Film 5: Gladiator
        film5 = Film("Gladiator", "155",
                     "Un général romain trahi cherche à se venger des conspirateurs qui ont assassiné sa famille et l'ont réduit en esclavage.")
        categorie9 = Categorie("Action", "Film d'action")
        categorie10 = Categorie("Drame", "Film dramatique")
        film5.ajouter_categorie(categorie9)
        film5.ajouter_categorie(categorie10)
        acteur9 = Acteur("Russell", "Crowe", "M", "Maximus", "2000-05-05", "2000-05-05", 20000000)
        acteur10 = Acteur("Joaquin", "Phoenix", "M", "Commodus", "2000-05-05", "2000-05-05", 15000000)
        film5.ajouter_acteur(acteur9)
        film5.ajouter_acteur(acteur10)
        films.append(film5)

        return films


# Classe pour le menu principal
class MainMenu(QWidget):
    def __init__(self, access_type, clients, films):
        super().__init__()

        # Titre de la fenêtre principale
        self.title = QLabel("NEFFIX", self)
        self.title.setStyleSheet("font-size: 24px; font-weight: bold; color: red;")

        self.setWindowTitle("Menu Principal")
        self.setGeometry(100, 100, 300, 200)
        self.access_type = access_type
        self.clients = clients
        self.films = films

        # Boutons de gestion des utilisateurs et des films, et boutons de déconnexion et quitter
        self.userManagementButton = QPushButton("Gérer les utilisateurs", self)
        self.viewFilmsButton = QPushButton("Voir les films", self)
        self.logoutButton = QPushButton("Déconnexion", self)
        self.quitButton = QPushButton("Quitter", self)

        # Disposition de la fenêtre principale
        layout = QVBoxLayout()
        layout.addWidget(self.userManagementButton)
        layout.addWidget(self.viewFilmsButton)
        layout.addWidget(self.logoutButton)
        layout.addWidget(self.quitButton)

        self.setLayout(layout)

        # Connexion des boutons à leurs fonctions respectives
        self.userManagementButton.clicked.connect(self.open_user_management)
        self.viewFilmsButton.clicked.connect(self.open_view_films)
        self.logoutButton.clicked.connect(self.logout)
        self.quitButton.clicked.connect(self.close)

    # Fonction pour ouvrir la gestion des utilisateurs
    def open_user_management(self):
        self.main_window = MainWindow(access_type=self.access_type, clients=self.clients, films=self.films)
        self.main_window.show()
        self.close()

    # Fonction pour ouvrir la gestion des films
    def open_view_films(self):
        self.film_window = FilmWindow(access_type=self.access_type, clients=self.clients, films=self.films)
        self.film_window.show()
        self.close()

    # Fonction pour se déconnecter
    def logout(self):
        self.login_window = LoginWindow()
        self.login_window.clients = self.clients  # Mise à jour des clients
        self.login_window.show()
        self.close()


# Classe pour la gestion principale des clients
class MainWindow(QWidget):
    def __init__(self, access_type, clients, films):
        super().__init__()
        self.setWindowTitle("Fenêtre Principale")
        self.setGeometry(100, 100, 600, 400)
        self.access_type = access_type
        self.clients = clients
        self.films = films

        # Tableau pour afficher les clients
        self.clientTable = QTableWidget(self)
        self.clientTable.setColumnCount(5)
        self.clientTable.setHorizontalHeaderLabels(["Nom", "Prénom", "Courriel", "Cartes de Crédit", "Date d'expiration"])
        self.clientTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.clientTable.setSelectionMode(QAbstractItemView.SingleSelection)

        # Boutons pour créer, modifier, supprimer des clients, et retour au menu
        self.createClientButton = QPushButton("Créer Client", self)
        self.modifyClientButton = QPushButton("Modifier Client", self)
        self.deleteClientButton = QPushButton("Supprimer Client", self)
        self.returnButton = QPushButton("Retour au Menu", self)

        # Désactiver les boutons de modification et suppression pour l'utilisateur en lecture seule
        if self.access_type == "read":
            self.createClientButton.setEnabled(False)
            self.modifyClientButton.setEnabled(False)
            self.deleteClientButton.setEnabled(False)

        # Disposition de la fenêtre principale
        layout = QVBoxLayout()
        layout.addWidget(self.clientTable)

        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(self.createClientButton)
        buttonLayout.addWidget(self.modifyClientButton)
        buttonLayout.addWidget(self.deleteClientButton)
        buttonLayout.addWidget(self.returnButton)
        layout.addLayout(buttonLayout)

        self.setLayout(layout)

        # Connexion des boutons et double-clic à leurs fonctions
        self.createClientButton.clicked.connect(self.open_create_client_window)
        self.modifyClientButton.clicked.connect(self.open_modify_client_window)
        self.deleteClientButton.clicked.connect(self.confirm_delete_client)
        self.returnButton.clicked.connect(self.return_to_menu)
        self.clientTable.itemDoubleClicked.connect(self.handle_double_click)

        self.load_clients()

    # Fonction pour gérer le double-clic sur un utilisateur
    def handle_double_click(self, item):
        if self.access_type != "read":
            self.open_modify_client_window()

    # Fonction pour charger les clients dans le tableau
    def load_clients(self):
        self.clientTable.setRowCount(0)  # Vider les lignes existantes
        for client in self.clients:
            self.add_client_to_table(client)

    # Fonction pour ouvrir la fenêtre de création de client
    def open_create_client_window(self):
        self.create_client_window = CreateClientWindow(self)
        self.create_client_window.show()

    # Fonction pour ouvrir la fenêtre de modification de client
    def open_modify_client_window(self):
        selected_row = self.clientTable.currentRow()
        if selected_row >= 0:
            client = self.clients[selected_row]
            self.modify_client_window = ModifyClientWindow(self, client)
            self.modify_client_window.show()

    # Fonction pour confirmer la suppression du client
    def confirm_delete_client(self):
        selected_row = self.clientTable.currentRow()
        if selected_row >= 0:
            reply = QMessageBox.question(self, 'Confirmation',
                                         "Êtes-vous sûr de vouloir supprimer ce client ?",
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.delete_client(selected_row)

    # Fonction pour supprimer le client sélectionné
    def delete_client(self, row):
        self.clients.pop(row)
        self.clientTable.removeRow(row)

    # Fonction pour ajouter un client à la liste et au tableau
    def add_client(self, client):
        self.clients.append(client)
        self.add_client_to_table(client)

    # Fonction pour ajouter un client au tableau
    def add_client_to_table(self, client):
        row = self.clientTable.rowCount()
        self.clientTable.insertRow(row)
        self.clientTable.setItem(row, 0, QTableWidgetItem(client.nom))
        self.clientTable.setItem(row, 1, QTableWidgetItem(client.prenom))
        self.clientTable.setItem(row, 2, QTableWidgetItem(client.courriel))
        self.clientTable.setItem(row, 3, QTableWidgetItem(", ".join([cc.numero for cc in client.cartes_credit])))
        self.clientTable.setItem(row, 4, QTableWidgetItem(", ".join([cc.date_expiration for cc in client.cartes_credit])))

    # Fonction pour retourner au menu principal
    def return_to_menu(self):
        self.main_menu = MainMenu(access_type=self.access_type, clients=self.clients, films=self.films)
        self.main_menu.show()
        self.close()


# Classe de base pour les fenêtres de client (création et modification)
class BaseClientWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 300, 300)

        # Champs de saisie pour les informations du client
        self.nomLabel = QLabel("Nom :", self)
        self.nomLineEdit = QLineEdit(self)

        self.prenomLabel = QLabel("Prénom :", self)
        self.prenomLineEdit = QLineEdit(self)

        self.courrielLabel = QLabel("Courriel :", self)
        self.courrielLineEdit = QLineEdit(self)

        self.passwordLabel = QLabel("Mot de passe :", self)
        self.passwordLineEdit = QLineEdit(self)
        self.passwordLineEdit.setEchoMode(QLineEdit.Password)

        self.cardNumberLabel = QLabel("Numéro de carte (8 chiffres) :", self)
        self.cardNumberLineEdit = QLineEdit(self)

        self.expirationDateLabel = QLabel("Date d'expiration (MM/YY) :", self)
        self.expirationDateLineEdit = QLineEdit(self)

        self.securityCodeLabel = QLabel("Code de sécurité (3 chiffres) :", self)
        self.securityCodeLineEdit = QLineEdit(self)

        # Disposition des champs
        layout = QVBoxLayout()
        layout.addWidget(self.nomLabel)
        layout.addWidget(self.nomLineEdit)
        layout.addWidget(self.prenomLabel)
        layout.addWidget(self.prenomLineEdit)
        layout.addWidget(self.courrielLabel)
        layout.addWidget(self.courrielLineEdit)
        layout.addWidget(self.passwordLabel)
        layout.addWidget(self.passwordLineEdit)
        layout.addWidget(self.cardNumberLabel)
        layout.addWidget(self.cardNumberLineEdit)
        layout.addWidget(self.expirationDateLabel)
        layout.addWidget(self.expirationDateLineEdit)
        layout.addWidget(self.securityCodeLabel)
        layout.addWidget(self.securityCodeLineEdit)
        self.setLayout(layout)

    # Fonction pour valider la date au format MM/YY
    def validate_date(self, date_str):
        try:
            datetime.strptime(date_str, "%m/%y")
            return True
        except ValueError:
            return False

    # Fonction pour valider les données du client
    def validate_client_data(self):
        password = self.passwordLineEdit.text()
        if len(password) < 8:
            QMessageBox.warning(self, "Erreur", "Le mot de passe doit contenir au moins 8 caractères.")
            return False

        courriel = self.courrielLineEdit.text()
        for client in self.main_window.clients:
            if client.courriel == courriel and (not hasattr(self, 'client') or client != self.client):
                QMessageBox.warning(self, "Erreur", "Le courriel doit être unique.")
                return False

        card_number = self.cardNumberLineEdit.text()
        if not card_number.isdigit() or len(card_number) != 8:
            QMessageBox.warning(self, "Erreur", "Le numéro de carte doit être composé de 8 chiffres.")
            return False

        expiration_date = self.expirationDateLineEdit.text()
        if not self.validate_date(expiration_date):
            QMessageBox.warning(self, "Erreur", "Mauvaise date d'expiration. Format attendu: MM/YY")
            return False

        security_code = self.securityCodeLineEdit.text()
        if not security_code.isdigit() or len(security_code) != 3:
            QMessageBox.warning(self, "Erreur", "Le code de sécurité doit être composé de 3 chiffres.")
            return False

        return True


# Classe pour la création de clients
class CreateClientWindow(BaseClientWindow):
    def __init__(self, main_window):
        super().__init__()
        self.setWindowTitle("Créer Client")
        self.main_window = main_window

        self.saveButton = QPushButton("Enregistrer", self)
        self.layout().addWidget(self.saveButton)

        # Connexion du bouton d'enregistrement à la fonction de sauvegarde
        self.saveButton.clicked.connect(self.save_client)

    # Fonction pour sauvegarder le nouveau client
    def save_client(self):
        if not self.validate_client_data():
            return

        nom = self.nomLineEdit.text()
        prenom = self.prenomLineEdit.text()
        courriel = self.courrielLineEdit.text()
        password = self.passwordLineEdit.text()

        # Création du client
        client = Client(nom, prenom, "M/F", "2023-01-01", courriel, password)

        card_number = self.cardNumberLineEdit.text()
        expiration_date = self.expirationDateLineEdit.text()
        security_code = self.securityCodeLineEdit.text()

        # Ajout de la carte de crédit au client
        carte_credit = CarteCredit(card_number, expiration_date, security_code)
        client.ajouter_carte_credit(carte_credit)

        # Ajout du client à la liste et fermeture de la fenêtre
        self.main_window.add_client(client)
        self.close()


# Classe pour la modification de clients
class ModifyClientWindow(BaseClientWindow):
    def __init__(self, main_window, client):
        super().__init__()
        self.setWindowTitle("Modifier Client")
        self.setGeometry(100, 100, 300, 400)
        self.main_window = main_window
        self.client = client

        self.nomLineEdit.setText(client.nom)
        self.prenomLineEdit.setText(client.prenom)
        self.courrielLineEdit.setText(client.courriel)
        self.passwordLineEdit.setText(client.password)
        self.cardNumberLineEdit.setText(client.cartes_credit[0].numero if client.cartes_credit else "")
        self.expirationDateLineEdit.setText(client.cartes_credit[0].date_expiration if client.cartes_credit else "")
        self.securityCodeLineEdit.setText(client.cartes_credit[0].code_secret if client.cartes_credit else "")

        self.saveButton = QPushButton("Enregistrer", self)
        self.layout().addWidget(self.saveButton)

        # Connexion du bouton d'enregistrement à la fonction de sauvegarde
        self.saveButton.clicked.connect(self.save_client)

    # Fonction pour sauvegarder les modifications du client
    def save_client(self):
        if not self.validate_client_data():
            return

        new_courriel = self.courrielLineEdit.text()
        for client in self.main_window.clients:
            if client.courriel == new_courriel and client != self.client:
                QMessageBox.warning(self, "Erreur", "Le courriel doit être unique.")
                return

        self.client.nom = self.nomLineEdit.text()
        self.client.prenom = self.prenomLineEdit.text()
        self.client.courriel = new_courriel
        self.client.password = self.passwordLineEdit.text()

        card_number = self.cardNumberLineEdit.text()
        expiration_date = self.expirationDateLineEdit.text()
        security_code = self.securityCodeLineEdit.text()

        # Mise à jour de la carte de crédit du client
        if self.client.cartes_credit:
            self.client.cartes_credit[0].numero = card_number
            self.client.cartes_credit[0].date_expiration = expiration_date
            self.client.cartes_credit[0].code_secret = security_code
        else:
            self.client.ajouter_carte_credit(CarteCredit(card_number, expiration_date, security_code))

        # Mise à jour des informations dans le tableau
        selected_row = self.main_window.clientTable.currentRow()
        self.main_window.clientTable.setItem(selected_row, 0, QTableWidgetItem(self.client.nom))
        self.main_window.clientTable.setItem(selected_row, 1, QTableWidgetItem(self.client.prenom))
        self.main_window.clientTable.setItem(selected_row, 2, QTableWidgetItem(self.client.courriel))
        self.main_window.clientTable.setItem(selected_row, 3, QTableWidgetItem(
            ", ".join([cc.numero for cc in self.client.cartes_credit])))
        self.main_window.clientTable.setItem(selected_row, 4, QTableWidgetItem(
            ", ".join([cc.date_expiration for cc in self.client.cartes_credit])))
        self.close()


# Classe pour la gestion des films
class FilmWindow(QWidget):
    def __init__(self, access_type, clients, films):
        super().__init__()
        self.setWindowTitle("Films")
        self.setGeometry(100, 100, 600, 400)
        self.access_type = access_type
        self.clients = clients
        self.films = films

        # Tableau pour afficher les films
        self.filmTable = QTableWidget(self)
        self.filmTable.setColumnCount(3)
        self.filmTable.setHorizontalHeaderLabels(["Nom", "Durée", "Description"])
        self.filmTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.filmTable.setSelectionMode(QAbstractItemView.SingleSelection)

        # Bouton pour retourner au menu principal
        self.returnButton = QPushButton("Retour au Menu", self)

        # Disposition de la fenêtre de gestion des films
        layout = QVBoxLayout()
        layout.addWidget(self.filmTable)
        layout.addWidget(self.returnButton)

        self.setLayout(layout)

        # Connexion du bouton de retour et du double-clic à leurs fonctions
        self.returnButton.clicked.connect(self.return_to_menu)
        self.populate_films()

    # Fonction pour charger les films dans le tableau
    def populate_films(self):
        self.filmTable.setRowCount(0)  # Vider les lignes existantes
        for film in self.films:
            row = self.filmTable.rowCount()
            self.filmTable.insertRow(row)
            self.filmTable.setItem(row, 0, QTableWidgetItem(film.nom))
            self.filmTable.setItem(row, 1, QTableWidgetItem(film.duree))
            self.filmTable.setItem(row, 2, QTableWidgetItem(film.description))

        self.filmTable.itemDoubleClicked.connect(self.view_film_details)

    # Fonction pour afficher les détails du film sélectionné
    def view_film_details(self, item):
        selected_row = item.row()
        film = self.films[selected_row]
        details = f"Nom: {film.nom}\nDurée: {film.duree}\nDescription: {film.description}\nCatégories:\n"
        for categorie in film.categories:
            details += f"- {categorie.nom} ({categorie.description})\n"
        details += "Acteurs:\n"
        for acteur in film.acteurs:
            details += f"- {acteur.nom} {acteur.prenom} (Personnage: {acteur.nom_personnage})\n"
        QMessageBox.information(self, "Détails du film", details)

    # Fonction pour retourner au menu principal
    def return_to_menu(self):
        self.main_menu = MainMenu(access_type=self.access_type, clients=self.clients, films=self.films)
        self.main_menu.show()
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec_())
