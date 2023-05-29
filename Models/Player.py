import json
import os


class Player:
    def __init__(self, first_name, last_name, birth_date, national_chess_id):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.national_chess_id = national_chess_id


    def save_player(self):
        new_player = self.__dict__
        if not os.path.exists('players.json'):
            with open('players.json', 'w') as file:
                json.dump([new_player], file, indent=4)
        else:
            with open('players.json', 'r+') as file:
                players = json.load(file)
                players.append(new_player)
                file.seek(0)
                file.truncate()
                json.dump(players, file, indent=4)
