"""
This module defines a `Player` class representing a board for the Tic-Tac-Toe game.
"""


class Player:
    """ A class representing players for a Tic-Tac-Toe game. """
    def __init__(self, name, mark):
        self._player_name = name
        self._player_mark = mark

    def get_player_name(self):
        """ Gets player name. """
        return self._player_name

    def get_player_mark(self):
        """ Gets player mark. """
        return self._player_mark

