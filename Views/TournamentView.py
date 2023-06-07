class TournamentView:
    def get_tournament_info(self):
        name = input("Nom du tournoi: ")
        location = input("Lieu: ")
        start_date = input("Date de début (JJ/MM/AAAA): ")
        end_date = input("Date de fin (JJ/MM/AAAA): ")
        rounds = input("Nombre de tours (défaut à 4): ") or 4  # IF EMPTY, SET TO 4
        description = input("Description du tournoi: ")

        return name, location, start_date, end_date, rounds, description
