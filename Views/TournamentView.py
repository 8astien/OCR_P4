from Views.View import View


class TournamentView(View):
    def __init__(self):
        self.description = None
        self.rounds = None
        self.end_date = None
        self.start_date = None
        self.location = None
        self.name = None

    def get_tournament_info(self):
        self.name = self.get_valid_alpha_input("Nom du tournoi: ")
        self.location = self.get_valid_alpha_input("Lieu: ")

        # Appel de la méthode présente dans View.py
        self.start_date = self.get_valid_date_input("Date de début (JJ/MM/AAAA): ")
        self.end_date = self.get_valid_date_input("Date de fin (JJ/MM/AAAA): ")

        self.rounds = input("Nombre de tours (optionnel, défaut à 4): ") or 4  # IF EMPTY, SET TO 4
        self.description = input("Description du tournoi (optionnel): ")

        return self.name, self.location, self.start_date, self.end_date, self.rounds, self.description

    def select_tournament(self, tournaments):
        print("\nSélectionnez un tournoi : ")
        tournaments_reversed = list(reversed(tournaments))
        for i, tournament in enumerate(tournaments_reversed):
            print(f"{i+1}. {tournament['name']} - {tournament['location']} - {tournament['start_date']} - {tournament['end_date']} - Rounds: {tournament['rounds']}")

        while True:
            try:
                tournament_index = int(input("\nEntrez le numéro du tournoi que vous voulez sélectionner : ")) - 1
                if tournament_index < 0 or tournament_index >= len(tournaments):
                    print("Numéro de tournoi invalide. Veuillez entrer un numéro de tournoi valide.")
                else:
                    return tournament_index
            except ValueError:
                print("Entrée invalide. Veuillez entrer un numéro.")