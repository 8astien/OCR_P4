class PlayerView:
    @staticmethod
    def get_player_info():
        first_name = input("Prénom: ")
        last_name = input("Nom de famille: ")
        birth_date = input("Date de naissance : ")
        national_chess_id = input("Identifiant national d'échecs : ")

        return first_name, last_name, birth_date, national_chess_id
