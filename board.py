class Board:
    def __init__(self):
        self._board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    def get_board(self):
        """ Gets the current state of the board. """
        return self._board

    def update_board(self, player, cell_number):
        """Updates the state of the board."""
        for row_idx, row in enumerate(self._board):
            for col_idx, cell in enumerate(row):
                if cell == cell_number:
                    self._board[row_idx][col_idx] = player


    def __str__(self):
        """ Returns a formatted string representation of the board. """
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

        formatted_board = board_layout.format(*[elem for row in self._board for elem in row])
        return formatted_board
