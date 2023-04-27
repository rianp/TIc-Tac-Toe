from game import Game
from board import Board
from player import Player, ComputerPlayer
from validation import Validator
from players import Players
from console import Console


def setup_game(console, validator):
    console.print_greeting()
    console.print_instructions()
    choice = console.selector(
        "Let's pick your opponent!"
        "\nPress 1 for Human or press 2 for Computer: ", validator.validate_choice)
    if choice == 1:
        player_1 = Player("1", "x")
        player_2 = Player("2", "o")
    else:
        player_1 = ComputerPlayer("1", "x")
        player_2 = Player("2", "o")

    players = Players(player_1, player_2)

    board_size = console.selector(
        "Let's build a board! Pick an odd number from 1 to 7: ", validator.validate_size)
    board = Board(board_size)

    game = Game(board, players, console, validator)

    return game


def main():
    validator = Validator()
    console = Console()

    game = setup_game(console, validator)
    end_game_message = game.play_round()

    console.print_string(end_game_message)


if __name__ == "__main__":
    main()
