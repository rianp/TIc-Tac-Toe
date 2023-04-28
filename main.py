from validation import Validator
from console import Console
from setup_game import SetUp


def main():
    console = Console()

    game = SetUp(console, Validator()).setup_game()
    end_game_message = game.play_round()

    console.print_string(end_game_message)


if __name__ == "__main__":
    main()
