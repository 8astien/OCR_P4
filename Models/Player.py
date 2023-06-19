import json
import os
from Models.Model import Model


class Player(Model):
    def __init__(self, first_name, last_name, birth_date, national_chess_id):
        self.id = self.get_new_id('data/players.json')
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.national_chess_id = national_chess_id

    def save_player(self):
        new_player = self.__dict__
        if not os.path.exists('data/players.json'):
            with open('data/players.json', 'w') as file:
                json.dump([new_player], file, indent=4)
        else:
            with open('data/players.json', 'r+') as file:
                players = json.load(file)
                players.append(new_player)
                file.seek(0)
                file.truncate()
                json.dump(players, file, indent=4)

    def get_players(self):
        file_path = 'data/players.json'
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                players = json.load(file)
                return players
        else:
            return print('Fichier players.json introuvable')
