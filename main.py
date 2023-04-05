from game import *
from board import *
from player import *
from turn import *
from validation import *
from players import *

def main():
    player_1 = Player("1", "x")
    player_2 = Player("2", "o")
    players = Players(player_1, player_2)
    game = Game(Board(), Turn(), Validator(), players.get_players())
    game.play()


if __name__ == "__main__":
    main()
