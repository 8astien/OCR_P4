import re


class PlayerView:

    def __init__(self):
        self.national_chess_id = None
        self.birth_date = None
        self.last_name = None
        self.first_name = None

    def get_player_info(self):
        self.first_name = input("Prénom: ")
        self.last_name = input("Nom de famille: ")

        # J'utilise des boucles While ici pour isoler les questions utilisateur
        # et ne pas devoir recommencer l'intégralité de la boucle en cas d'errer d'input
        while True:
            self.birth_date = input("Date de naissance (JJ/MM/AAAA): ")
            if self.is_valid_date(self.birth_date):
                break
            else:
                print("Date de naissance invalide. Réessayez.")

        while True:
            self.national_chess_id = input("Identifiant national d'échecs (AB12345) : ")
            if self.is_valid_id(self.national_chess_id):
                break
            else:
                print("Identifiant national d'échecs invalide. Réessayez.")

        return self.first_name, self.last_name, self.birth_date, self.national_chess_id

    def is_valid_date(self, date):
        return re.fullmatch(r'\d{2}/\d{2}/\d{4}', date) is not None

    def is_valid_id(self, id):
        return re.fullmatch(r'[A-Za-z]{2}\d{5}', id) is not None
