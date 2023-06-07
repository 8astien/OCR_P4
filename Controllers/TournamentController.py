from Models.Tournament import Tournament
from Views.TournamentView import TournamentView

class TournamentController:
    def __init__(self):
        self.tournamentView = TournamentView()

    def create_tournament(self):
        name, location, start_date, end_date, rounds, description = self.tournamentView.get_tournament_info()
        self.tournament = Tournament(name, location, start_date, end_date, rounds, description)
        print(name, location, start_date, end_date, rounds, description)
        self.tournament.save_tournament()
        return self.tournament
