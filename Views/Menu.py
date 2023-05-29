from Controllers.PlayerController import PlayerController


class Menu:

    def __init__(self):
        self.choice = None

    def main_menu(self):
        print("\n========CHESS TOURNAMENT MANAGER========")
        print("\n--- MENU ---")
        print("1. Ajouter un joueur")
        print("2. ItemMenu2")
        print("3. ItemMenu3")
        print("0. Quitter")

        self.choice = input("\nEntrez le numéro correspondant à votre choix : ")

        player_controller = PlayerController()

        if self.choice == '1':
            player_controller.add_player()
            self.main_menu()

        elif self.choice == '2':
            pass
        elif self.choice == '3':
            pass

        elif self.choice == '0':
            print("Au revoir!")
            exit()
        else:
            print("Choix non valide. Veuillez entrer un chiffre valide.")
            self.main_menu()

