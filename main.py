from game import Game
from board import Board
from player import Player
from validation import Validator
from players import Players
from console import Console



def main():
    board = Board()
    player_1 = Player("1", "x")
    player_2 = Player("2", "o")
    players = Players(player_1, player_2)
    validator = Validator()
    console = Console()

    console.print_greeting()
    console.print_instructions()
    board_size = console.prompt_input("Let's build a board! Pick an odd number from 3 to 5: ")
    board.build_board(board_size)

    game = Game(board, players, console, validator)
    end_game_message = game.play_round()

    console.print_string(end_game_message)


if __name__ == "__main__":
    main()
