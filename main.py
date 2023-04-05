from game import *
from board import *
from player import *
from turn import *
from validation import *
from players import *


def main():
    board = Board()
    player_1 = Player("1", "x")
    player_2 = Player("2", "o")
    players = Players(player_1, player_2).get_players()
    turn = Turn()
    validator = Validator()
    game = Game(board, turn, validator, players)
    game.play()


if __name__ == "__main__":
    main()
