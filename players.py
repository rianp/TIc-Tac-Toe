"""
This module defines a `Player` class representing a board for the Tic-Tac-Toe game.
"""


class Players:
    """ A class representing players for a Tic-Tac-Toe game. """
    def __init__(self):
        self._players = ("x", "o")

    def get_player(self, player):
        """ Gets player. """
        return self._players[player - 1]
