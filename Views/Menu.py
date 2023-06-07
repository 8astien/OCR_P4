from Controllers.PlayerController import PlayerController
from Controllers.TournamentController import TournamentController

class Menu:

    def __init__(self):
        self.choice = None

    def main_menu(self):
        print("\n========CHESS TOURNAMENT MANAGER========")
        print("\n--- MENU ---")
        print("1. Ajouter un joueur")
        print("2. Créer un tournoi")
        print("3. ItemMenu3")
        print("0. Quitter")

        self.choice = input("\nEntrez le numéro correspondant à votre choix : ")

        player_controller = PlayerController()
        tournament_controller = TournamentController()

        match self.choice:
            case '1':
                player_controller.add_player()
                self.main_menu()
            case '2':
                tournament_controller.create_tournament()
                self.main_menu()
            case '3':
                pass
            case '0':
                print("Au revoir!")
                exit()
            case _:
                print("Choix non valide. Veuillez entrer un chiffre valide.")
                self.main_menu()



