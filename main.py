from game import Game
from board import Board
from player import Player
from validation import Validator
from players import Players
from console import Console
from game_start import GameStart


def main():
    board = Board()
    player_1 = Player("1", "x")
    player_2 = Player("2", "o")
    players = Players(player_1, player_2)
    validator = Validator()
    console = Console()

    start = GameStart()
    start.start_game(console)

    game = Game()
    game.play_round(board, players, console, validator)


if __name__ == "__main__":
    main()