class Menu:

    def __init__(self):
        self.choice = None

    def main_menu(self):
        print("\n========CHESS TOURNAMENT MANAGER========")
        print("\n--- MENU ---")
        print("1. Ajouter un joueur")
        print("2. Créer un tournoi")
        print("3. Ajouter des joueurs à un tournoi")
        print("0. Quitter")

        self.choice = input("\nEntrez le numéro correspondant à votre choix : ")

        return self.choice
