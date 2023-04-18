class Validator:
    @staticmethod
    def is_on_board(choice, board):
        return any(choice in row for row in board)

    @staticmethod
    def is_in_range(choice, board_range):
        return choice in board_range

    @staticmethod
    def is_valid_integer(string):
        try:
            int(string)
            return True
        except ValueError:
            return False

    @staticmethod
    def is_there_whitespace(string):
        return len(string.strip()) == len(string)

    def validate_move(self, user_input, board):
        if not self.is_valid_integer(user_input):
            return False, "Eek! That's not even a number! "

        move = int(user_input)

        if not self.is_in_range(move, board.get_board_range()):
            return False, "Whoa friend! This is outta bounds! "

        if not self.is_on_board(move, board.get_board()):
            return False, "Rats! Someone already snagged this one! "

        return True, ""
