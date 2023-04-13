class Validator:
    @staticmethod
    def is_on_board(choice, board):
        return any(choice in row for row in board)

    @staticmethod
    def is_in_range(choice, board):
        return choice in range(1, len(board) * len(board) + 1)

    @staticmethod
    def is_valid_integer(string):
        try:
            int(string)
            return True
        except ValueError:
            return False
