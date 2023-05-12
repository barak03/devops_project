import random
import utils
from Game import Game


class GuessGame(Game):
    def __init__(self, difficulty_level_number):
        super().__init__(difficulty_level_number)
        self._secret_number = None

    def generate_number(self):
        self._secret_number = random.randint(1, self._difficulty_level_number)

    def get_guess_from_user(self):
        user_guess = input("Guess a number: ")
        while not user_guess.isdigit():
            user_guess = input(f"{utils.bcolors.OKBLUE}Please enter your guessed number: {utils.bcolors.ENDC}")

        return int(user_guess)

    def compare_results(self):
        if self.get_guess_from_user() == self._secret_number:
            utils.print_right_guess()
            return True
        else:
            utils.print_wrong_guess()
            return False

    def play(self):
        self.generate_number()
        return self.compare_results()
