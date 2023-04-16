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

    @staticmethod
    def is_there_whitespace(string):
        return len(string.strip()) == len(string)

    def validate_move(self, user_input, board, console):

        if not self.is_valid_integer(user_input):
            console.print_string("Eek! That's not even a number! ")
            return False

        move = int(user_input)

        if not self.is_in_range(move, board.get_board_range()):
            console.print_string("Whoa friend! This is outta bounds! ")
            return False

        if not self.is_on_board(move, board.get_board()):
            console.print_string("Rats! Someone already snagged this one! ")
            return False

        return True
