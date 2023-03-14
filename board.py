"""
This module defines a `Board` class representing a board for the Tic-Tac-Toe game.
"""


class Board:
    """ A class representing a board for a Tic-Tac-Toe game. """
    def __init__(self, size=10):
        self._board = {i: str(i) for i in range(1, size)}

    def get_board(self):
        """  Gets board. """
        return self._board

    def __str__(self):
        """ Returns a formatted string version of a book object instance. """
        board_layout = "************************\n"\
                    "*    Current Board!    *\n"\
                    "************************\n"\
                    "*                      *\n"\
                    "*    {}  |  {}  |  {}     *\n"\
                    "*  ------------------  *\n"\
                    "*    {}  |  {}  |  {}     *\n"\
                    "*  ------------------  *\n"\
                    "*    {}  |  {}  |  {}     *\n"\
                    "*                      *\n"\
                    "************************"

        formatted_board = board_layout.format(*[self._board[num] for num in range(1, len(self._board)+1)])
        return formatted_board
