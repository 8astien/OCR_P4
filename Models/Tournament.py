import os
import json

class Tournament:
    def __init__(self, name, location, start_date, end_date, rounds=4, current_round=1,
                 round_list=[], player_list=[], description=""):
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
        file_path = 'data/tournament/{}.json'.format(self.name)

        # Enregistrer le tournoi dans un fichier JSON
        with open(file_path, 'w') as file:
            json.dump(new_tournament, file, indent=4)
