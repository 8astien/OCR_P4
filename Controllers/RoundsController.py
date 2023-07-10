from Models.Tournament import Tournament
from Views.TournamentView import TournamentView
import random

class RoundsController:
    def __init__(self):
        self.tournament = Tournament(None, None, None, None, None, None)
        self.tournamentView = TournamentView()
        

    def play_round(self):
        tournaments = self.tournament.get_tournaments()
        selected_tournament_id = self.tournamentView.select_tournament(tournaments)
        selected_tournament = None
        for tournament in tournaments:
            if tournament['id'] == selected_tournament_id:
                selected_tournament = tournament
                break

        if selected_tournament is None:
            print('Tournoi introuvable')
            return
        
        # Verification du nombre de joueurs
        registered_players = len(selected_tournament['player_list'])
        max_players = selected_tournament['rounds'] * 2
        if registered_players < max_players:
            print('Nombre de joueurs insuffisants pour lancer le round')
            return

        # Trier les joueurs randomly
        random.shuffle(selected_tournament['player_list'])
        rand_players_list = selected_tournament['player_list']
        
        # Create matches
        matches = []
        for i in range(0, len(rand_players_list), 2):
            match = ([rand_players_list[i], 0], [rand_players_list[i+1], 0])
            matches.append(match)

        # Create a round
        round = {
            "name": f"Round {selected_tournament['current_round']}",
            "start_date": None,
            "end_date": None,
            "matches": matches
        }
        selected_tournament['round_list'].append(round)
        print(matches)
