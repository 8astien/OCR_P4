import re


class View:

    def is_valid_date(self, date):
        return re.fullmatch(r'\d{2}/\d{2}/\d{4}', date) is not None

    def is_valid_id(self, id):
        return re.fullmatch(r'[A-Za-z]{2}\d{5}', id) is not None

    def is_valid_alpha(self, input_string):
        return re.fullmatch(r'[A-Za-z]{2,}', input_string) is not None

    def get_valid_date_input(self, prompt):
        while True:
            date = input(prompt)
            if self.is_valid_date(date):
                return date
            else:
                print("Date invalide. Réessayez.")

    def get_valid_alpha_input(self, prompt):
        while True:
            input_string = input(prompt)
            if self.is_valid_alpha(input_string):
                return input_string
            else:
                print("Entrée invalide. Réessayez avec au moins deux caractères alphabétiques.")

