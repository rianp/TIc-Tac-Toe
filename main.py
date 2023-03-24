"""
This module contains the `main` function that calls the game module
"""


from game import *


def main():
    """ Initializes and starts the Tic Tac Toe game. """
    game = Game()
    game.play()


if __name__ == "__main__":
    main()
