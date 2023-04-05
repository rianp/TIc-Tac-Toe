class Validator:
    @staticmethod
    def validate_selection(choice, board):
        if not isinstance(choice, int):
            return False

        return any(choice in row for row in board)
