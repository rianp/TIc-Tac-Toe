class Board:
    def __init__(self):
        self._board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    def get_board(self):
        return self._board

    def get_board_range(self):
        board_range = range(1, len(self._board) * len(self._board))
        return board_range

    def update_board(self, player, cell_number):
        for row_idx, row in enumerate(self._board):
            for col_idx, cell in enumerate(row):
                if cell == cell_number:
                    self._board[row_idx][col_idx] = player


    def __str__(self):
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
