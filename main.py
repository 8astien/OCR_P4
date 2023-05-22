from Models.Player import Player
from Views.PlayerView import PlayerView
from Controllers.PlayerController import PlayerController

def main():
    while True:
        # Demander à l'utilisateur s'il souhaite ajouter un joueur
        add_player = input("Souhaitez-vous ajouter un joueur ? (O/N): ")

        # Si l'utilisateur veut ajouter un joueur
        if add_player.lower() == 'o':
            PlayerController.add_player()
        else:
            break

if __name__ == '__main__':
    main()

