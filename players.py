"""
This module defines a `Player` class representing a board for the Tic-Tac-Toe game.
"""


class Players:
    """ A class representing players for a Tic-Tac-Toe game. """
    def __init__(self):
        self._players = ("Player 1", "Player 2")

    def get_players(self):
        """ Gets player. """
        return self._players
