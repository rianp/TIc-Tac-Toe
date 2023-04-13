class Validator:
    @staticmethod
    def is_on_board(choice, board):
        return any(choice in row for row in board)

    @staticmethod
    def is_in_range(choice, range):
        return choice in range

    @staticmethod
    def is_valid_integer(string):
        try:
            int(string)
            return True
        except ValueError:
            return False
