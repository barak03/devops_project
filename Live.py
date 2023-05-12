import os
import utils
from MemoryGame import MemoryGame
from GuessGame import GuessGame
from CurrencyRouletteGame import CurrencyRouletteGame
import Score
import MainScores
import threading


def welcome(player_name):
    return f"Hello {player_name} and welcome to the World Of Games (WOG) {os.linesep}" \
           f"Here you can find many cool games to play"


def load_game():
    p = threading.Thread(target=lambda: MainScores.app.run('0.0.0.0', port=30000, debug=False, use_reloader=False))
    p.daemon = True
    p.start()
    game, difficulty_level = get_game()
    while True:
        if game.play():
            MainScores.save_score(Score.add_score(difficulty_level))

        user_choice = utils.play_another_game()
        if user_choice == 2:
            utils.clear_screen()
            utils.print_bye()
            raise KeyboardInterrupt
        elif user_choice == 3:
            utils.clear_screen()
            game, difficulty_level = get_game()



def get_game():
    game = None
    chosen_game_msg = """Please choose a game to play
1.Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back.
2.Guess Game - guess a number and see if you choose like the computer.
3.Currency Rollet - try nd guess thr value of a random amount of USD in ILS
4.Quit
"""
    difficulty_level_msg = "Choose difficulty level 1, 2, 3, 4, 5"
    chosen_game = utils.get_input_from_user_as_number_in_range(limit_number_1=1, limit_number_2=4,
                                                               input_msg=chosen_game_msg)
    utils.clear_screen()
    if chosen_game == 4:
        raise KeyboardInterrupt

    utils.clear_screen()
    difficulty_level = utils.get_input_from_user_as_number_in_range(limit_number_1=1, limit_number_2=5,
                                                                    input_msg=difficulty_level_msg)
    if chosen_game == 1:
        game = MemoryGame(difficulty_level_number=difficulty_level)
    elif chosen_game == 2:
        game = GuessGame(difficulty_level_number=difficulty_level)
    elif chosen_game == 3:
        game = CurrencyRouletteGame(difficulty_level_number=difficulty_level)

    utils.clear_screen()
    return game, difficulty_level
