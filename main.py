"""
This module contains the `main` function that creates any
necessary objects and calls functions to execute the program's logic.
"""
from game import *


def main():
    game = Game()
    game.play()


if __name__ == "__main__":
    main()
