"""
This module defines a `Turn` class representing the turns for the Tic-Tac-Toe game.
"""


class Turn:
    """ A class representing a turn for a Tic-Tac-Toe game. """

    def __init__(self):
        self._turn = 1

    def change_turn(self):
        """ Changes player turn. """
        if self._turn == 1:
            self._turn = 2
        else:
            self._turn = 1

    def get_current_turn(self):
        """ Returns the current player turn. """
        return self._turn
