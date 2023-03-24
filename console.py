"""
This module defines a `Console` class representing a console interface for the Tic-Tac-Toe game.
"""


class Console:
    """ A class representing a console interface for a Tic-Tac-Toe game. """

    @staticmethod
    def print_string(string):
        """  Prints string. """
        print(string)

    @staticmethod
    def prompt_input(string):
        """ Prompts user for a string input. """
        result = input(string)
        return result
