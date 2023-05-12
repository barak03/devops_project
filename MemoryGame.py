import random
import utils
from Game import Game
import time


class MemoryGame(Game):
    def __init__(self, difficulty_level_number):
        super().__init__(difficulty_level_number)
        self._random_numer_list = []
        self._player_numer_list = []

    def generate_sequence(self):
        self._random_numer_list = random.choices(range(1, 101), k=self._difficulty_level_number)

    def get_list_from_user(self):
        for i in range(self._difficulty_level_number):
            user_input = input(f"Enter the number you remember in {i + 1} position ")
            while not user_input.isdigit():
                user_input = input(f"Enter the number (integer) you remember in {i + 1} position ")

            self._player_numer_list.append(int(user_input))

    def is_list_equal(self):
        for i in range(self._difficulty_level_number):
            if self._random_numer_list[i] != self._player_numer_list[i]:
                return False

        return True

    def play(self):
        self._player_numer_list.clear()
        self.generate_sequence()
        print(f"Remember this list: {self._random_numer_list}")
        time.sleep(0.7)
        utils.clear_screen()
        self.get_list_from_user()
        if self.is_list_equal():
            utils.print_right_guess()
            return True
        else:
            utils.print_wrong_guess()
            return False
