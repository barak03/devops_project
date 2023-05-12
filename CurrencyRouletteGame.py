import random
import utils
from Game import Game
from currency_converter import CurrencyConverter


class CurrencyRouletteGame(Game):
    def __init__(self, difficulty_level_number):
        super().__init__(difficulty_level_number)
        self._usd_to_ils_rate = None
        self._money = None
        self._money_interval = None
        self.get_usd_to_ils_rate()

    def get_usd_to_ils_rate(self):
        c = CurrencyConverter()
        self._usd_to_ils_rate = c.convert(1, 'USD', 'ILS')

    def get_money_interval(self):
        self._money_interval = (((self._money * self._usd_to_ils_rate) - (5 - self._difficulty_level_number)),
                                ((self._money * self._usd_to_ils_rate) + (5 - self._difficulty_level_number)))

    def get_guess_from_user(self):
        user_guess = input(f"Guess how much ${self._money} is in ILS: ")
        while not user_guess.isdigit():
            user_guess = input(f"{utils.bcolors.OKBLUE}Please enter your guessed amount: {utils.bcolors.ENDC}")

        return float(user_guess)

    def play(self):
        self._money = random.randint(1, 100)
        self.get_money_interval()
        user_guess_amount = self.get_guess_from_user()
        if self._money_interval[0] < user_guess_amount < self._money_interval[1]:
            utils.print_right_guess()
            return True
        else:
            utils.print_wrong_guess()
            return False
