import os

SCORES_FILE_NAME = "scores.txt"
BAD_RETURN_CODE = -1


def print_bye():
    print("Good game, Bye :)")


def print_right_guess():
    print(
        f"{bcolors.OKGREEN}WOOHOO{bcolors.OKBLUE} you guess correct{bcolors.ENDC}")


def print_wrong_guess():
    print(f"{bcolors.WARNING}OOPS your guess was wrong{bcolors.ENDC}")


def play_another_game():
    play_another_game_msg = """Do you want to play another game?
1.Yes
2.No
3.Switch Game
"""
    return get_input_from_user_as_number_in_range(limit_number_1=1, limit_number_2=3,
                                                  input_msg=play_another_game_msg)


def get_input_from_user_as_number_in_range(limit_number_1, limit_number_2, input_msg):
    while True:
        user_input = input(f"{input_msg} {os.linesep}Enter your choice: ")
        if not user_input.isdigit():
            print(f"{bcolors.FAIL}Enter an integer !{bcolors.ENDC}")
            continue

        user_input = int(user_input)
        if not limit_number_1 <= user_input <= limit_number_2:
            print(
                f"{bcolors.FAIL}Enter a number between {limit_number_1} to {limit_number_2} !{bcolors.ENDC}")
            continue

        return user_input


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
