"""
This module defines a `Validation` class representing a validator for the Tic-Tac-Toe game.
"""


class Validation:
    """ Validates user inputs and search results. """

    @staticmethod
    def validate_selection(choice, board):
        """ Validates number selection. """
        return any(int(choice) in row for row in board)
