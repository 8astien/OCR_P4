class PlayerView:

    def __init__(self):
        self.national_chess_id = None
        self.birth_date = None
        self.last_name = None
        self.first_name = None

    def get_player_info(self):
        self.first_name = input("Prénom: ")
        self.last_name = input("Nom de famille: ")
        self.birth_date = input("Date de naissance : ")
        self.national_chess_id = input("Identifiant national d'échecs : ")

        return self.first_name, self.last_name, self.birth_date, self.national_chess_id
