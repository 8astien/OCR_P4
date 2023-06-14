from Controllers.PlayerController import PlayerController
from Controllers.TournamentController import TournamentController
from Views.Menu import Menu


class MenuController:
    def __init__(self):
        self.menu = Menu()
        self.player_controller = PlayerController()
        self.tournament_controller = TournamentController()

    def user_choice(self):
        choice = self.menu.main_menu()

        match choice:
            case '1':
                self.player_controller.add_player()
                self.user_choice()
            case '2':
                self.tournament_controller.create_tournament()
                self.user_choice()
            case '3':
                self.tournament_controller.add_player_to_tournament()
                self.user_choice()
            case '0':
                print("Au revoir!")
                exit()
            case _:
                print("Choix non valide. Veuillez entrer un chiffre valide.")
                self.user_choice()
