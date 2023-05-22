import json
import os

from Models.Player import Player
from Views.PlayerView import PlayerView


class PlayerController:

    @staticmethod
    def generate_id():
        if not os.path.exists("players.json") or os.stat("players.json").st_size == 0:
            return 1  # si le fichier est vide ou n'existe pas, l'ID du premier joueur sera 1
        else:
            with open('players.json', 'r') as file:
                players = json.load(file)
                if players:  # vérifier si la liste n'est pas vide
                    last_player = players[-1]
                    return last_player["id"] + 1
                else:  # si la liste est vide (le fichier existait mais aucun joueur n'a encore été ajouté)
                    return 1

    @staticmethod
    def add_player():
        # Récupérer les informations du joueur
        first_name, last_name, birth_date, national_chess_id = PlayerView.get_player_info()

        # Générer un id unique
        id = PlayerController.generate_id()

        # Créer un nouveau joueur
        new_player = Player(first_name, last_name, birth_date, national_chess_id, id)

        # Ajouter le joueur à la base de données
        if not os.path.exists('players.json'):
            with open('players.json', 'w') as file:
                json.dump([new_player.__dict__], file, indent=4)
        else:
            with open('players.json', 'r+') as file:
                players = json.load(file)
                players.append(new_player.__dict__)
                file.seek(0)
                json.dump(players, file, indent=4)
