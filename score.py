"""
This module defines a `Score` class representing a board for the Tic-Tac-Toe game.
"""


class Score:
    """ A class representing the score for a Tic-Tac-Toe game. """

    @staticmethod
    def get_game_status(board):
        """ Gets the current state of the game. """

        for row in board:
            if all(elem == row[0] for elem in row):
                return row[0]

        for col in range(len(board)):
            if len({row[col] for row in board}) == 1 and not isinstance(board[0][col], int):
                return board[0][col]

        if len({board[i][i] for i in range(len(board))}) == 1 and not isinstance(board[0][0], int):
            return board[0][0]

        if len({board[i][len(board) - i - 1] for i in range(len(board))}) == 1 and not isinstance(
                board[0][len(board) - 1], int):
            return board[0][len(board) - 1]

        if all(not isinstance(cell, int) for row in board for cell in row):
            return 'Tie'

        return False
