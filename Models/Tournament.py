import os
import json
from Models.Model import Model

class Tournament(Model):
    def __init__(self, name, location, start_date, end_date, rounds=4, current_round=1,
                 round_list=[], player_list=[], description=""):
        self.id = self.get_new_id('data/tournament/tournaments.json')
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.rounds = rounds
        self.current_round = current_round
        self.round_list = round_list
        self.player_list = player_list
        self.description = description
    
    def save_tournament(self):
        new_tournament = self.__dict__

        # S'assurer que le dossier 'data/tournament' existe
        if not os.path.exists('data/tournament'):
            os.makedirs('data/tournament')

        # Créer le chemin du fichier avec le nom du tournoi
        file_path = 'data/tournament/tournaments.json'

        if not os.path.exists(file_path):
            with open(file_path, 'w') as file:
                json.dump([new_tournament], file, indent=4)
        else:
            with open(file_path, 'r+') as file:
                existing_tournaments = json.load(file)
                existing_tournaments.append(new_tournament)
                file.seek(0)
                file.truncate()
                json.dump(existing_tournaments, file, indent=4)

    def get_tournaments(self):
        file_path = 'data/tournament/tournaments.json'
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                tournaments = json.load(file)
                return tournaments
        else:
            return print('Le fichier tournaments.json est introuvable')

    def update_tournament(self, updated_tournament):
        if os.path.exists('data/tournament/tournaments.json'):
            with open('data/tournament/tournaments.json', 'r') as file:
                tournaments = json.load(file)
            for i, tournament in enumerate(tournaments):
                # On utilise maintenant l'ID pour vérifier le bon tournoi
                if tournament['id'] == updated_tournament['id']:
                    tournaments[i] = updated_tournament
                    break
            else:
                print("Tournoi introuvable")
                return

            with open('data/tournament/tournaments.json', 'w') as file:
                json.dump(tournaments, file, indent=4)
        else:
            print('Fichier tournaments.json introuvable')

