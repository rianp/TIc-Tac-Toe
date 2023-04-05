class Score:

    @staticmethod
    def get_game_status(board):

        for row in board:
            if all(elem == row[0] for elem in row):
                return True

        for col in range(len(board)):
            if len({row[col] for row in board}) == 1:
                return True

        if len({board[i][i] for i in range(len(board))}) == 1:
            return True

        if len({board[i][len(board) - i - 1] for i in range(len(board))}) == 1:
            return True

        if all(not isinstance(cell, int) for row in board for cell in row):
            return 'Tie'

        return False
