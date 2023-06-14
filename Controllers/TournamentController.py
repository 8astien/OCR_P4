from Models.Player import Player
from Models.Tournament import Tournament
from Views.TournamentView import TournamentView
from Views.PlayerView import PlayerView


class TournamentController:
    def __init__(self):
        self.tournament = Tournament(None, None, None, None, None, None)
        self.player = Player(None, None, None, None)
        self.tournamentView = TournamentView()
        self.playerView = PlayerView()

    def create_tournament(self):
        name, location, start_date, end_date, rounds, description = self.tournamentView.get_tournament_info()
        self.tournament = Tournament(name, location, start_date, end_date, rounds, description)
        self.tournament.save_tournament()

    def add_player_to_tournament(self):
        # Récupérer tous les tournois
        tournaments = self.tournament.get_tournaments()
        # Récupérer tous les joueurs
        players = self.player.get_players()
        print(tournaments)
        print(players)
        # Afficher tous les tournois et demander à l'utilisateur d'en choisir un
        tournament_index = self.tournamentView.select_tournament(tournaments)
        if tournament_index is not None:
            selected_tournament = tournaments[tournament_index]

            # Afficher tous les joueurs et demander à l'utilisateur d'en choisir un
            player_index = self.playerView.select_player(players)
            if player_index is not None:
                selected_player = players[player_index]

                # Ajouter le joueur sélectionné au tournoi
                selected_tournament['player_list'].append(selected_player)

                # Mettre à jour le tournoi dans le fichier JSON
                self.tournament.update_tournament(selected_tournament)
