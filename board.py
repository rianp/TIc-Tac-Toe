"""
This module defines a `Board` class representing a board for the Tic-Tac-Toe game.
"""


class Board:
    """ A class representing a board for a Tic-Tac-Toe game. """
    def __init__(self):
        self._board = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}

    def get_board(self):
        """  Gets board. """
        return self._board

    def __str__(self):
        """ Returns a formatted string version of a book object instance. """
        board_str = "************************\n"\
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
        formatted_board = board_str.format(*[self._board[num] for num in range(1, 10)])   # refactor range to be dynamic
        return formatted_board


# board = Board()
# print(board.get_board())
# print(str(board))

