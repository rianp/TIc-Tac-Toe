"""
This module defines a `Validation` class representing a validator for the Tic-Tac-Toe game.
"""


class Validation:
    """ Validates user inputs and search results. """

    @staticmethod
    def validate_selection(choice, board):
        """ Validates number selection. """
        for row in board:
            if int(choice) in row:
                return True
        return False
