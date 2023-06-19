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

        # Afficher tous les tournois et demander à l'utilisateur d'en choisir un
        selected_tournament_id = self.tournamentView.select_tournament(tournaments)

        selected_tournament = None
        for tournament in tournaments:
            if tournament['id'] == selected_tournament_id:
                selected_tournament = tournament
                break

        if selected_tournament is None:
            print('Tournoi introuvable')
            return

        # Boucle pour la sélection du joueur
        while True:
            # Afficher tous les joueurs et demander à l'utilisateur d'en choisir un
            player_index = self.playerView.select_player(players)
            if player_index is not None:
                selected_player = players[player_index]

                # Ajouter le joueur sélectionné au tournoi
                if selected_player['id'] in [player['id'] for player in selected_tournament['player_list']]:
                    print('Joueur déjà enregistré pour ce tournoi')
                else:
                    selected_tournament['player_list'].append(selected_player)

                    # Mettre à jour le tournoi dans le fichier JSON
                    self.tournament.update_tournament(selected_tournament)

                    # Demander à l'utilisateur s'il souhaite ajouter un autre joueur
                    add_another = input("Souhaitez-vous ajouter un nouveau joueur à ce tournoi ? o/n: ")
                    if add_another.lower() != 'o':
                        break  # Sortir de la boucle après avoir ajouté le joueur


