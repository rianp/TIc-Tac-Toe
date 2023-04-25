from enum import Enum


class WinnerStatus(Enum):
    WINNER_X = 1
    WINNER_O = 2
    DRAW = 3
    ONGOING = 4


class Board:
    def __init__(self, board_size=3):
        self._board_size = board_size
        self._board = self.build_board()

    def build_board(self):
        board = []
        count = 1

        for i in range(self._board_size):
            row = []
            for j in range(self._board_size):
                row.append(count)
                count += 1
            board.append(row)

        return board

    def get_size(self):
        return self._board_size * self._board_size

    def get_board(self):
        return self._board

    def get_board_range(self):
        board_range = range(1, len(self._board) * len(self._board) + 1)
        return board_range

    def get_board_winner_status(self):
        board = self._board
        size = len(board)

        for row in board:
            if all(cell == row[0] for cell in row):
                return WinnerStatus.WINNER_X if row[0] == 'x' else WinnerStatus.WINNER_O

        for col in range(size):
            if all(board[row][col] == board[0][col] for row in range(size)):
                return WinnerStatus.WINNER_X if board[0][col] == 'x' else WinnerStatus.WINNER_O

        if all(board[i][i] == board[0][0] for i in range(size)):
            return WinnerStatus.WINNER_X if board[0][0] == 'x' else WinnerStatus.WINNER_O

        if all(board[i][size - i - 1] == board[0][size - 1] for i in range(size)):
            return WinnerStatus.WINNER_X if board[0][size - 1] == 'x' else WinnerStatus.WINNER_O

        if all(isinstance(cell, str) for row in board for cell in row):
            return WinnerStatus.DRAW

        return WinnerStatus.ONGOING

    def update_board(self, player, cell_number):
        for row_idx, row in enumerate(self._board):
            for col_idx, cell in enumerate(row):
                if cell == cell_number:
                    self._board[row_idx][col_idx] = player
